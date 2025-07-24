from dataclasses import dataclass
import hashlib


@dataclass
class Permission:
    shit: bool  # 排便补贴
    travel: int  # 出行补贴单位cny
    accommodation: bool  # 住宿补贴
    meal: bool = True  # 餐食
    
    def check_shit_permission(self) -> bool:
        """检查是否有排便补贴权限"""
        return self.shit


@dataclass
class User:
    id: int
    username: str
    password: str  #sha256 hash
    permissions: Permission

    def set_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest()


class Users:
    users: list[User] = []
    
    def __init__(self):
        if not self.users:
            # 初始化一些默认用户作为示例
            self.users = []
    
    def register(self, user: User):
        """注册新用户"""
        # 检查用户ID是否已存在
        for existing_user in self.users:
            if existing_user.id == user.id:
                raise ValueError(f"User ID {user.id} already exists")
            if existing_user.username == user.username:
                raise ValueError(f"Username {user.username} already exists")
        
        self.users.append(user)
        return user

    def login(self, username: str, password: str):
        """用户登录"""
        for user in self.users:
            if user.username == username:
                if user.password == hashlib.sha256(password.encode()).hexdigest():
                    return user
        raise ValueError("Username or password incorrect")

    def delete(self, user_id: int):
        """删除用户"""
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
        
    def get_user(self, user_id: int) -> User:
        """根据ID获取用户"""
        for user in self.users:
            if user.id == user_id:
                return user
        raise ValueError(f"User with ID {user_id} not found")
        
    def update_permissions(self, user_id: int, permissions: Permission) -> User:
        """更新用户权限"""
        user = self.get_user(user_id)
        user.permissions = permissions
        return user
