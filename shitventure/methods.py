from .users import User, Permission, Users
from dataclasses import dataclass
from typing import Optional, Dict, List
from datetime import datetime
from enum import Enum


class ViolationType(Enum):
    """违规类型"""
    FAKE_RECORD = "伪造记录"  # 伪造排便记录
    EXCESSIVE_AMOUNT = "过量申报"  # 申报过量排便
    LOCATION_FRAUD = "地点欺诈"  # 地点欺诈
    MULTIPLE_CLAIMS = "重复申报"  # 同一次排便重复申报
    OTHER = "其他违规"  # 其他违规行为


@dataclass
class ShitRecord:
    """排便记录"""
    user_id: int
    timestamp: datetime
    location: str
    amount: float  # 排便量(kg)
    subsidy_amount: float  # 补贴金额
    is_valid: bool = True  # 记录是否有效（未被取消资格）
    disqualify_reason: Optional[str] = None  # 取消资格原因


class ShitSubsidyManager:
    """排便补贴管理器"""
    def __init__(self, users_manager: Users):
        self.users_manager = users_manager
        self.shit_records: List[ShitRecord] = []
        
        # 补贴标准
        self.shit_subsidy_rate = 50.0  # 每kg补贴50元
        
        # 违规记录
        self.violations: Dict[int, List[ViolationType]] = {}  # 用户ID -> 违规类型列表
        
        # 排便量限制
        self.daily_amount_limit = 2.0  # 每日最大排便量限制(kg)
        self.single_record_limit = 1.0  # 单次排便最大限制(kg)
    
    def record_shit(self, user_id: int, amount: float, location: str) -> Optional[ShitRecord]:
        """记录排便并计算补贴"""
        try:
            user = self.users_manager.get_user(user_id)
            
            # 检查用户是否有排便补贴权限
            if not user.permissions.check_shit_permission():
                print(f"用户 {user.username} 没有排便补贴权限")
                return None
            
            # 检查用户是否有违规记录
            if user_id in self.violations and len(self.violations[user_id]) >= 3:
                print(f"用户 {user.username} 因多次违规已被永久取消排便补贴资格")
                return None
            
            # 检查排便量是否超过单次限制
            if amount > self.single_record_limit:
                print(f"单次排便量 {amount}kg 超过限制 {self.single_record_limit}kg")
                self._add_violation(user_id, ViolationType.EXCESSIVE_AMOUNT)
                return None
            
            # 检查当日排便总量是否超过限制
            today = datetime.now().date()
            today_records = [r for r in self.shit_records 
                            if r.user_id == user_id and r.timestamp.date() == today and r.is_valid]
            today_amount = sum(r.amount for r in today_records)
            
            if today_amount + amount > self.daily_amount_limit:
                print(f"当日排便总量 {today_amount + amount}kg 超过限制 {self.daily_amount_limit}kg")
                self._add_violation(user_id, ViolationType.EXCESSIVE_AMOUNT)
                return None
            
            # 计算补贴金额
            subsidy = amount * self.shit_subsidy_rate
            
            # 创建记录
            record = ShitRecord(
                user_id=user_id,
                timestamp=datetime.now(),
                location=location,
                amount=amount,
                subsidy_amount=subsidy,
                is_valid=True
            )
            
            # 保存记录
            self.shit_records.append(record)
            return record
            
        except ValueError as e:
            print(f"记录排便失败: {e}")
            return None
    
    def _add_violation(self, user_id: int, violation_type: ViolationType) -> None:
        """添加违规记录"""
        if user_id not in self.violations:
            self.violations[user_id] = []
        
        self.violations[user_id].append(violation_type)
        
        # 如果违规次数达到3次，取消用户排便补贴权限
        if len(self.violations[user_id]) >= 3:
            try:
                user = self.users_manager.get_user(user_id)
                user.permissions.shit = False
                print(f"用户 {user.username} 因多次违规已被永久取消排便补贴资格")
            except ValueError:
                pass
    
    def disqualify_record(self, record_id: int, reason: ViolationType, admin_note: str = "") -> bool:
        """取消某条排便记录的资格"""
        for i, record in enumerate(self.shit_records):
            if i == record_id and record.is_valid:  # 使用索引作为记录ID
                # 标记记录为无效
                record.is_valid = False
                record.disqualify_reason = f"{reason.value}: {admin_note}"
                
                # 添加违规记录
                self._add_violation(record.user_id, reason)
                
                print(f"已取消记录 {record_id} 的资格，原因: {reason.value} {admin_note}")
                return True
        
        print(f"未找到记录 {record_id} 或记录已被取消资格")
        return False
    
    def check_suspicious_records(self) -> List[int]:
        """检查可疑的排便记录，返回可疑记录的ID列表"""
        suspicious_records = []
        
        for i, record in enumerate(self.shit_records):
            if not record.is_valid:
                continue
            
            # 检查是否有异常大的排便量
            if record.amount > 0.8:  # 超过0.8kg视为可疑
                suspicious_records.append(i)
                continue
            
            # 检查是否有短时间内多次排便记录
            user_records = [r for r in self.shit_records if r.user_id == record.user_id and r.is_valid]
            user_records.sort(key=lambda r: r.timestamp)
            
            for j in range(len(user_records) - 1):
                if user_records[j] == record:
                    time_diff = (user_records[j+1].timestamp - record.timestamp).total_seconds() / 3600
                    if time_diff < 2:  # 2小时内多次排便视为可疑
                        suspicious_records.append(i)
                        break
        
        return suspicious_records
    
    def get_user_shit_records(self, user_id: int, include_invalid: bool = False) -> List[ShitRecord]:
        """获取用户的排便记录"""
        if include_invalid:
            return [record for record in self.shit_records if record.user_id == user_id]
        else:
            return [record for record in self.shit_records if record.user_id == user_id and record.is_valid]
    
    def get_user_violations(self, user_id: int) -> List[ViolationType]:
        """获取用户的违规记录"""
        return self.violations.get(user_id, [])
    
    def calculate_shit_subsidy(self, user_id: int) -> float:
        """计算用户的排便补贴总金额"""
        return sum(record.subsidy_amount for record in self.get_user_shit_records(user_id))
    
    def get_violation_statistics(self) -> Dict[ViolationType, int]:
        """获取各类违规的统计数据"""
        stats = {vtype: 0 for vtype in ViolationType}
        
        for violations in self.violations.values():
            for violation in violations:
                stats[violation] += 1
        
        return stats