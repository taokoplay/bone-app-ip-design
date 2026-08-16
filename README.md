# bone-app-ip-design

把 App IP 从“一张角色图”推进为可进入真实产品的**人格化识别与交互系统**。

`bone-app-ip-design` 是一个面向 AI Agent 的设计 Skill，用于从产品、界面与代码出发，创建、接入或扩展可持续出现的 App 品牌形象。它覆盖角色定位、母体选择、状态反馈、UI 联调、App Icon、Widget、商店素材和生产交接，并通过阶段门槛避免在身份尚未稳定时过早批量生产资产。

当前版本：**1.4.0**

## 适用场景

- 从零设计 App 角色、吉祥物、陪伴形象或人格化物件
- 将已有 IP 接入真实功能、业务状态和界面
- 为角色建立完成、等待、空状态、离线、同步、错误等反馈
- 规划换装、主题皮肤与可复用生产骨架
- 建立统一的 App × IP 视觉语言
- 设计带有 IP 身份的 App Icon、Widget 和商店素材
- 根据 App 内容、品牌人格、UI、小尺寸风险和货架差异，从 11 类风格中选择主风格与对照风格
- 用结构化 Prompt 锁定图标的产品关联、单一构图、媒介、配色职责、小尺寸识别与负约束
- 检查小尺寸识别、深浅模式、reduced motion 与 VoiceOver 适配

## 不适用场景

以下任务不应强制使用本 Skill：

- 没有持续 IP 身份的普通 Design System
- 普通几何 Icon 或纯 ASO 排版
- 一次性插画、通用头像或游戏 NPC
- 以世界观、玩具、盲盒、包装、授权和泛媒介商业化为核心的角色 IP

最后一类任务更适合先使用 `character-ip-design`；当目标转为 App 内产品化后，再使用本 Skill。

## 核心方法

1. **先产品、后形象**：先确认产品任务、用户压力、出现位置和真实尺寸。
2. **先母体、后角色**：保留无新增 IP 的基线，并在 Character、Object、Abstract/System、Typographic/Attitude 与 Hybrid 中选择。
3. **先身份、后扩展**：先锁定基础母版，再生产状态、换装和技术拆层。
4. **先真实尺寸、后大图**：优先检查 32–96pt 和真实 UI，而不是只看海报精度。
5. **角色服务任务**：IP 不抢主按钮，也不以羞辱、催促、卖惨或假进度表达状态。
6. **证据诚实**：区分已验证、基于输入推断、待工具执行和待用户确认。

## 工作流

Skill 会按请求路由相关模块，不要求所有项目机械走完完整流程。

```text
产品与能力检查
  → App IP Brief
  → IP 母体选择
  → 三个差异化方向
  → 基础母版与确认门槛
  → App × IP 联调
  → 业务状态与扩展
  → Icon / 商店素材 / 生产交接
```

常见路由：

| 请求 | 主要流程 |
| --- | --- |
| 从零创建 App IP | Brief → 母体 → 三方向 → 基础母版 |
| 已有 IP 增加业务状态 | Identity Lock → 状态矩阵 → UI 联调 |
| 已有 IP 规划换装 | Identity Lock → 身份锚点 → Tier A/B/C |
| Icon-only | Brief → 母体 → Icon 支线 |
| 商店图-only | Visual DNA → Store 支线 |
| 完整 App IP 系统 | 核心产品化 → Icon → Store → 交接 |

## 安装

将仓库克隆到 Agent 的 Skills 目录：

```bash
git clone https://github.com/taokoplay/bone-app-ip-design.git bone-app-ip-design
```

如果你的 Agent 使用固定 Skills 根目录，可直接指定目标路径。例如：

```bash
git clone https://github.com/taokoplay/bone-app-ip-design.git ~/.proma/skills/bone-app-ip-design
```

安装后重新加载 Agent 或 Skills 配置。不同 Agent 框架的目录约定可能不同，请以其文档为准。

## 使用示例

安装后可直接用自然语言描述目标，例如：

```text
为我的用药记录 App 设计一个能长期出现在首页和完成反馈中的品牌形象。
```

```text
我们已有一个角色，请不要重做外形，帮我建立 loading、syncing、offline、empty 和 error 状态。
```

```text
把现有 IP 产品化，规划 App Icon、Widget 和 App Store 前三张截图的视觉系统。
```

```text
检查这个角色在 32pt、深色模式、reduced motion 和 VoiceOver 下是否仍然成立。
```

## 目录结构

```text
bone-app-ip-design/
├── SKILL.md                         # Skill 入口、路由与完整工作流
├── references/
│   ├── ai-image-iteration.md        # AI 生图、身份锁与版本回退
│   ├── app-icon-system.md           # App Icon 与代表尺寸 QA
│   ├── icon-style-presets.md        # 风格选择与 Prompt 增强预设
│   ├── before-click-patterns.md     # 案例证据与常见反例
│   ├── character-productization.md  # 母体、母版、状态与换装
│   ├── deliverable-templates.md     # Brief、矩阵与交付模板
│   ├── production-handoff.md        # 图层、命名、导出与生产交接
│   └── store-assets.md              # 商店截图、Preview 与 claims
├── evals/
│   ├── evals.json                   # 行为质量评测
│   ├── trigger-evals.json           # 触发与不触发评测
│   └── fixtures/                    # 合成评测输入
└── scripts/
    └── validate_skill.py            # 结构和数据完整性校验
```

## 本地验证

运行内置校验：

```bash
python3 scripts/validate_skill.py
```

校验覆盖：

- `SKILL.md` frontmatter、名称与版本
- Reference 链接和 Markdown fenced code block
- 行为评测数量、ID 唯一性与 fixture 引用
- 触发评测数量及正负样例平衡
- 合成评测数据声明
- 已废弃硬规则残留

当前评测集包含：

- 15 个任务质量评测
- 24 个触发评测（12 个应触发、12 个不应触发）

## 设计底线

- 不复制著名 IP 的整体印象、独特结构、名称或典型姿势
- 系统错误不能被表现成用户做错
- 未确认基础母版前，不批量生产正式状态和换装资产
- 商店图中的奖项、用户量、媒体、医疗、金融及 AI 效果必须可核验
- 未实际浏览、生成、缩放、联调或上传的项目，不得声称已验证

## License

本仓库当前尚未声明开源许可证。除非仓库所有者另行授权，否则保留所有权利。
