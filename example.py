#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
示例：如何使用 shitventure 包进行账号管理和排便补贴权限检测

这是一个幽默的Python包，专注于排便补贴管理，纪念AdventureX 2025黑客松史上最传奇的厕所事件。
请系好安全带，准备开启一段奇妙的排便补贴之旅！

记住：文明如厕，人人有责！
"""

from shitventure.users import User, Permission, Users  # 用户管理，比厕所管理员还重要
from shitventure.methods import ShitSubsidyManager, ViolationType  # 排便补贴管理，比金融系统还严格
import hashlib  # 密码加密，比厕所门锁还安全
from datetime import datetime, timedelta  # 时间管理，排便也需要计时


def main():
    print("🚽 欢迎使用AdventureX排便补贴管理系统 💩")
    print("记住：每一次文明如厕，都是一次收益！\n")
    
    # 创建用户管理器（排便精英俱乐部的门卫）
    users_manager = Users()
    
    # 创建几个具有不同权限的用户（排便界的三剑客）
    # 用户1：有排便补贴权限（排便界的大佬）
    user1_permissions = Permission(
        shit=True,  # 有排便补贴，这位是排便精英
        travel=0,
        accommodation=False
    )
    
    user1 = User(
        id=1,
        username="张三",  # 排便届的传奇人物
        password=hashlib.sha256("password123".encode()).hexdigest(),  # 密码比马桶盖还安全
        permissions=user1_permissions
    )
    
    # 用户2：有排便补贴权限（排便界的新星）
    user2_permissions = Permission(
        shit=True,  # 有排便补贴，前途无量的排便新秀
        travel=0,
        accommodation=False
    )
    
    user2 = User(
        id=2,
        username="李四",  # 排便量惊人，被称为"排便王子"
        password=hashlib.sha256("password456".encode()).hexdigest(),  # 密码强度与排便能力成正比
        permissions=user2_permissions
    )
    
    # 用户3：无排便补贴权限（排便界的局外人）
    user3_permissions = Permission(
        shit=False,  # 无排便补贴，可怜的灵魂
        travel=0,
        accommodation=False
    )
    
    user3 = User(
        id=3,
        username="王五",  # 排便能力有待提高的可怜人
        password=hashlib.sha256("password789".encode()).hexdigest(),  # 密码再强也无法获得排便补贴
        permissions=user3_permissions
    )
    
    # 注册用户（欢迎加入排便精英俱乐部）
    print("📝 注册排便精英用户中...")
    users_manager.register(user1)
    print(f"✅ 用户 {user1.username} 已加入排便精英行列！")
    users_manager.register(user2)
    print(f"✅ 用户 {user2.username} 已获得排便资格认证！")
    users_manager.register(user3)
    print(f"⚠️ 用户 {user3.username} 注册成功，但无排便补贴权限，请努力提高排便能力！\n")
    
    # 创建排便补贴管理器（比银行还严格的补贴系统）
    print("🏦 初始化排便补贴管理系统...")
    subsidy_manager = ShitSubsidyManager(users_manager)
    print("💰 排便补贴管理系统已就绪，标准补贴率：50 CNY/kg\n")
    
    # 测试登录（厕所门禁系统）
    print("🔑 验证用户身份中...")
    try:
        logged_user = users_manager.login("张三", "password123")
        print(f"✅ 用户 {logged_user.username} 登录成功！欢迎回到排便精英俱乐部！")
    except ValueError as e:
        print(f"❌ 登录失败: {e} (可能是马桶冲水声太大，密码输入错误)")
    
    # 测试排便补贴（激动人心的时刻到了！）
    print("\n🧻 === 排便补贴测试，请系好安全带 === 🧻")
    
    # 用户1记录排便（有权限）- 排便界的常规操作
    print("\n🚽 张三正在公司卫生间就座...")
    shit_record1 = subsidy_manager.record_shit(
        user_id=1,
        amount=0.5,  # 0.5kg - 相当不错的成绩
        location="公司卫生间"  # 公费马桶，效率加倍
    )
    if shit_record1:
        print(f"💩 用户1排便记录成功！重量：0.5kg，堪称艺术品！")
        print(f"💰 补贴金额: {shit_record1.subsidy_amount}元 - 排便也能创造价值！")
    
    # 用户2记录排便（有权限）- 尝试超过单次限制（野心太大）
    print("\n🚽 李四正在家里卫生间挑战极限...")
    shit_record2 = subsidy_manager.record_shit(
        user_id=2,
        amount=1.2,  # 1.2kg - 超过单次限制，这是大象级别的成就
        location="家里卫生间"  # 私人领地，无所顾忌
    )
    if not shit_record2:
        print(f"⚠️ 用户2排便记录失败！原因：1.2kg已超过单次排便量限制！")
        print(f"🐘 系统提示：您是人类还是大象？请适度排便！")
    
    # 用户2正常记录排便（吸取教训后的表现）
    print("\n🚽 李四调整心态，再次尝试...")
    shit_record2 = subsidy_manager.record_shit(
        user_id=2,
        amount=0.7,  # 0.7kg - 相当可观，但在限制范围内
        location="家里卫生间"  # 再次挑战
    )
    if shit_record2:
        print(f"💩 用户2排便记录成功！重量：0.7kg，接近专业水平！")
        print(f"💰 补贴金额: {shit_record2.subsidy_amount}元 - 排便致富，指日可待！")
    
    # 用户3记录排便（无权限）- 可怜的局外人
    print("\n🚽 王五偷偷摸摸地在酒店卫生间尝试...")
    shit_record3 = subsidy_manager.record_shit(
        user_id=3,
        amount=0.6,  # 0.6kg - 相当不错，可惜没有权限
        location="酒店卫生间"  # 高级场所也无济于事
    )
    if not shit_record3:
        print("❌ 用户3排便被拒绝！系统提示：您没有排便补贴权限！")
        print("😢 王五：我排便就不能有尊严吗？")
    
    # 测试违规检测和取消资格（排便反作弊系统启动）
    print("\n🚨 === 排便反作弊系统启动，作弊者将无处可逃 === 🚨")
    
    # 模拟用户1多次排便记录（短时间内）- 贪婪的代价
    print("\n🕵️ 系统检测到张三可能有作弊嫌疑...")
    print("🔍 启动排便频率分析...")
    # 先添加一个伪造的记录（时间提前10分钟）- 这是作弊行为！
    fake_time = datetime.now() - timedelta(minutes=10)
    from shitventure.methods import ShitRecord
    fake_record = ShitRecord(
        user_id=1,
        timestamp=fake_time,
        location="公司卫生间",  # 同一地点，太可疑了
        amount=0.3,  # 0.3kg，看似合理
        subsidy_amount=0.3 * subsidy_manager.shit_subsidy_rate,  # 偷偷获取15元
        is_valid=True  # 暂时有效，即将被揭穿
    )
    subsidy_manager.shit_records.append(fake_record)
    print("⚠️ 张三10分钟内连续排便两次，这是人类能力范围内的吗？")
    
    # 检查可疑记录（排便诚信系统发挥作用）
    print("\n🔎 启动排便诚信审核系统...")
    suspicious_records = subsidy_manager.check_suspicious_records()
    print(f"🚨 警报！发现 {len(suspicious_records)} 条可疑排便记录！排便造假将受到严惩！")
    
    # 取消可疑记录资格（排便法庭开庭）
    print("\n⚖️ 排便诚信法庭现在开庭...")
    if suspicious_records:
        record_id = suspicious_records[0]
        print(f"👨‍⚖️ 法官：被告张三，你被指控在10分钟内提交多次排便记录，这违反了排便自然规律！")
        disqualified = subsidy_manager.disqualify_record(
            record_id=record_id,
            reason=ViolationType.MULTIPLE_CLAIMS,
            admin_note="短时间内多次排便记录，涉嫌排便造假"
        )
        if disqualified:
            print(f"🔨 判决：记录 {record_id} 已被认定为排便造假！补贴取消！")
            print("📝 张三被记入排便耻辱墙，这将永远玷污他的排便履历！")
    
    # 用户2尝试提交过量排便记录（贪得无厌的后果）
    print("\n🐘 李四决定挑战系统极限，连续提交大量排便记录...")
    for i in range(3):
        print(f"🚽 尝试 #{i+1}: 李四又坐在马桶上了...")
        result = subsidy_manager.record_shit(
            user_id=2,
            amount=0.9,  # 接近限制但仍可疑，几乎是1公斤！
            location="家里卫生间"  # 这个马桶承受了太多
        )
        if result:
            print(f"⚠️ 系统警告：0.9kg已接近人类极限，请适度排便！")
        else:
            print(f"❌ 记录失败：您的排便行为已被系统标记为可疑！")
    
    # 检查用户2的违规记录（排便诚信档案）
    print("\n📊 系统正在生成李四的排便诚信报告...")
    violations = subsidy_manager.get_user_violations(2)
    print(f"📋 诚信报告结果：用户2（李四）有 {len(violations)} 次排便违规记录！")
    print("🔍 违规类型：过量排便，涉嫌造假，可能使用了非人类排泄物！")
    
    # 如果违规次数达到3次，用户将失去排便补贴权限（三振出局制度）
    if len(violations) >= 3:
        print("\n🚫 系统执行三振出局政策...")
        print("📢 系统公告：用户2（李四）因多次违规已被永久取消排便补贴资格！")
        print("🏆 李四失去了\"排便王子\"的称号，沦为普通排便者！")
        
        # 尝试再次记录排便（徒劳的挣扎）
        print("\n😢 李四不死心，再次尝试提交排便记录...")
        shit_record = subsidy_manager.record_shit(
            user_id=2,
            amount=0.5,  # 这次很克制
            location="家里卫生间"  # 熟悉的战场
        )
        if not shit_record:
            print("❌ 系统拒绝：用户2（李四）已被列入排便黑名单，无法再获得补贴！")
            print("💔 李四：我的排便生涯就这样结束了吗？")
    
    # 计算用户1的排便补贴总额（收获的季节）
    print("\n💰 === 张三的排便收益报告 === 💰")
    shit_subsidy = subsidy_manager.calculate_shit_subsidy(1)
    print(f"📊 排便补贴总额: {shit_subsidy}元 - 排便也能创造财富！")
    print(f"💹 投资回报率: 极高 - 比股市更稳定的收益来源！")
    print(f"🏆 排便等级: 专业级 - 距离排便大师仅一步之遥！")
    
    # 获取违规统计（排便耻辱墙）
    print("\n🚨 === 排便耻辱墙 - 违规统计 === 🚨")
    violation_stats = subsidy_manager.get_violation_statistics()
    if not any(count > 0 for count in violation_stats.values()):
        print("✅ 太棒了！目前没有违规记录，大家都是文明排便的好榜样！")
    else:
        print("📋 违规类型统计：")
        for violation_type, count in violation_stats.items():
            if count > 0:
                if violation_type == ViolationType.MULTIPLE_CLAIMS:
                    print(f"🕒 {violation_type.value}: {count}次 - 超人也做不到这么频繁排便！")
                elif violation_type == ViolationType.EXCESSIVE_AMOUNT:
                    print(f"🐘 {violation_type.value}: {count}次 - 这是人类还是大象的排便量？")
                elif violation_type == ViolationType.FAKE_RECORD:
                    print(f"🎭 {violation_type.value}: {count}次 - 排便造假，可耻！")
                elif violation_type == ViolationType.LOCATION_FRAUD:
                    print(f"🗺️ {violation_type.value}: {count}次 - 难道是用了传送门？")
                else:
                    print(f"❓ {violation_type.value}: {count}次 - 创新型作弊，令人叹为观止！")
    
    print("\n🚽 === 排便补贴系统演示结束 === 🚽")
    print("记住：文明如厕，从你我做起！排便有度，补贴无忧！")


if __name__ == "__main__":
    main()
    # 这个示例文件比厕所读物还要精彩，不是吗？