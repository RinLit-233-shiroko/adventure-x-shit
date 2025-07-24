# Adventure-X-Shit 💩

一个幽默的Python包，专注于排便补贴管理，纪念AdventureX 2025黑客松史上最传奇的厕所事件。具有账号系统、权限检测和违规处理功能，让您的排便补贴管理既严谨又有趣！

## 事件背景 📰

在AdventureX 2025黑客松现场，发生了一起震惊整个技术圈的厕所事件：

- 🚽 某位神秘程序员在厕所"释放"了超越人类极限的"作品"
- 🤰 一名孕妇参赛者不幸中招，当场呕吐不止
- 😱 现场一片混乱，活动几乎中断
- 💰 主办方紧急推出排便补贴计划，鼓励文明如厕
- 🕵️ 同时建立严格的违规检测系统，防止补贴欺诈

## 功能特点 ✨

- 用户账号管理（注册、登录、删除）
- 排便补贴权限管理系统（谁配拥有这项权利？）
- 精确的排便记录和补贴计算（每千克50元，物有所值！）
- 智能违规检测和处理机制（想作弊？没门！）
- 用户违规记录统计（三次违规，永久拉黑！）

## 安装 📦

```bash
# 克隆仓库（请确保您的厕所已冲洗干净）
git clone https://github.com/yourusername/adventure-x-shit.git
cd adventure-x-shit

# 安装依赖（比安装马桶还简单！）
pip install -e .

# 或者直接从PyPI安装
pip install shitventure
```

安装完成后，您将拥有世界上最先进的排便补贴管理系统！请文明使用，不要尝试欺骗系统，我们的违规检测算法比您想象的更聪明！

## 使用方法 🚀

### 基本用法（如厕指南）

```python
from shitventure.users import User, Permission, Users
from shitventure.methods import ShitSubsidyManager, ViolationType

# 创建用户管理器（毕竟不是谁都有资格获得排便补贴）
users_manager = Users()

# 创建权限（您配拥有这项特权吗？）
permission = Permission(
    shit=True  # 排便补贴权限，True表示"有资格放屁"
)

# 创建用户（一位勇敢的排便者）
user = User(
    id=1,
    username="张三",  # 这位仁兄即将创造历史
    password="password123",  # 会自动进行SHA256哈希，比马桶水箱还安全
    permissions=permission
)

# 注册用户（欢迎加入排便精英俱乐部）
users_manager.register(user)

# 创建排便补贴管理器（严格把关每一份补贴）
subsidy_manager = ShitSubsidyManager(users_manager)

# 记录排便并获取补贴（诚实记录，轻松获取）
shit_record = subsidy_manager.record_shit(
    user_id=1,
    amount=0.5,  # 0.5kg，相当于一只小猫的重量
    location="公司卫生间"  # 请不要在同事的桌子下面...
)

print(f"恭喜您完成了一次光荣的排便！补贴金额: {shit_record.subsidy_amount}元")

# 检查可疑记录（我们的AI比您想象的更聪明）
suspicious_records = subsidy_manager.check_suspicious_records()
if suspicious_records:
    # 取消可疑记录资格（作弊者将被无情揭露）
    subsidy_manager.disqualify_record(
        record_id=suspicious_records[0],
        reason=ViolationType.FAKE_RECORD,
        admin_note="伪造排便记录，这不是您的杰作，请诚实面对自己的排便能力"
    )
```

### 完整示例

查看 `example.py` 文件获取完整的使用示例。这个例子比任何厕所读物都精彩！

## 权限系统 🔑

系统支持以下权限类型（经过严格筛选的特权）：

- `shit`: 是否有排便补贴权限（不是每个人都配拥有这项荣誉）

获取权限的方式：
1. 通过严格的排便能力测试
2. 获得现有排便精英的推荐
3. 证明您有能力创造超越常人的"杰作"

## 补贴标准 💰

- 排便补贴：每千克50元（比黄金还值钱的排泄物）
- 单次排便量限制：1.0kg（超过这个重量，请咨询医生或吉尼斯世界纪录）
- 每日排便总量限制：2.0kg（您真的能超过这个限制吗？如果能，请联系我们的研究团队）

## 违规类型 🚨

系统支持以下违规类型检测（我们的AI比您想象的更聪明）：

- `FAKE_RECORD`: 伪造排便记录（用猫砂或其他替代品充数？我们能识别！）
- `EXCESSIVE_AMOUNT`: 过量申报排便（除非您是大象，否则1.2kg的单次记录令人怀疑）
- `LOCATION_FRAUD`: 地点欺诈（在同事桌子下申报？我们会知道的）
- `MULTIPLE_CLAIMS`: 同一次排便重复申报（一份"作品"只能申报一次补贴）
- `OTHER`: 其他违规行为（我们的AI能识别各种创新的作弊方式）

## 违规处理机制 ⚖️

- 违规记录会被标记为无效，不计入补贴（您的"杰作"将被无情地抹去）
- 用户累计3次违规将被永久取消排便补贴资格（三振出局，永不录用）
- 系统自动检测可疑记录（如短时间内多次排便、异常大的排便量等）
- 严重违规者将被公开展示在我们的"排便耻辱墙"上（请不要成为第一个）

## 使用场景 🎭

1. **公司福利系统**
   - 为员工提供额外的排便补贴，提高工作满意度
   - "老板，我需要去趟卫生间，这可是为公司创收！"

2. **研究机构**
   - 收集排便数据用于健康研究
   - "我们的研究表明，程序员在Debug时排便量增加50%"

3. **黑客松活动**
   - 在编程马拉松中提供排便补贴，鼓励健康如厕
   - "我不是去摸鱼，我是去为团队赚取额外补贴！"

4. **家庭应用**
   - 跟踪家庭成员的排便情况，奖励健康习惯
   - "儿子，如果你今天按时排便，爸爸会给你买冰淇淋"

## 贡献指南 🤝

我们欢迎所有形式的贡献，无论是代码、文档还是创意！

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m '添加了一些惊人的特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个Pull Request

请注意：所有与排便相关的笑话必须既幽默又不过分粗俗。我们追求的是会心一笑，而非引起不适。

## 免责声明 ⚠️

本项目纯属娱乐和教育目的，不鼓励任何不当的厕所使用行为。请在使用公共设施时保持基本的文明和礼貌。我们不对因使用本软件而导致的任何尴尬情况负责。

记住：文明如厕，人人有责！

## 许可证 📄

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

---

> "在代码的世界里，我们追求完美；在现实的世界里，我们追求文明如厕。" - AdventureX格言