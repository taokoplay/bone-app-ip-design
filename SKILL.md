---
name: bone-app-ip-design
description: >-
  凡用户希望在 App 中创建、接入或扩展一个可持续出现的品牌形象，优先使用本 Skill。包括从产品与代码出发设计角色/吉祥物/陪伴形象/桌宠/人格化物件/抽象 IP，将已有 IP 产品化，或建立统一的 App × IP 视觉语言；也包括让形象承担导航、陪伴、品牌识别及完成、失败、空状态、天气、同步等反馈，并适配 UI、深浅模式、小尺寸、动效、换装、reduced motion、VoiceOver、App Icon、Widget、App Store 截图与 Preview。即使用户只说“给应用设计一个形象”“让角色进入真实功能”或仅要求规划已有 IP 的商店资产，也应触发。不用于没有持续 IP 身份的普通 Design System、几何 Icon、纯 ASO 排版、一次性插画、通用头像、游戏 NPC，或以玩具、包装、授权和世界观为核心的线下/泛媒介 IP；后者优先 character-ip-design。
version: "1.3.0"
---

# App IP Design

App IP 不是一张漂亮角色图，而是运行在产品中的**人格化识别与交互系统**。先确认它替 App 做什么，再决定它是否需要脸、身体、材质或世界观。

## 核心原则

1. **先产品、后形象**：产品任务、用户压力和出现位置先于画风。
2. **先母体、后角色**：允许 Character、Object、Abstract/System、Typographic/Attitude 或无新增 IP。
3. **先身份、后扩展**：先锁定基础母版，再批量做状态、换装和生产拆层。
4. **先真实尺寸、后大图**：32–96pt、真实 UI 和操作层级优先于海报精度。
5. **默认一个主变量**：允许一个强耦合从变量，但要说明因果和判断标准。
6. **角色服务任务**：不抢主按钮，不用羞辱、催促、卖惨或假进度表达产品状态。
7. **证据诚实**：未实际浏览、生成、缩放、联调或上传的项目，不得声称已验证。
8. **商店视觉卖结果**：标题提供承诺，IP/品牌提供感觉，真实 UI 和数据负责证明。

## 与其他 Skill 的边界

- App 内状态、Icon、UI 和技术资产是主要成功标准：使用本 Skill。
- 世界观、内容运营、授权、玩具、盲盒和泛媒介商业化是主要成功标准：使用 `character-ip-design`。
- 两者都要：先明确本轮交付阶段，不默认同时加载两个完整流程；商业定位完成后，再用本 Skill 做 App 产品化。
- 普通无 IP Icon、商店截图排版或 ASO metadata：路由到对应设计/ASO流程，不强加角色。

## 第一步：能力检查与证据状态

先检查用户提供的代码仓库、设计稿、UI 截图、品牌规范、现有角色母版、业务状态和目标平台。只追问会实质改变方向的问题；信息不足但可合理推断时，列出假设继续。

全程使用四种状态：

- **已验证**：已用工具或真实输入完成检查。
- **基于输入推断**：有依据，但未做实物测试。
- **待工具执行**：缺浏览、生图、图像处理、上传环境或真实 UI。
- **待用户确认**：涉及方向选择或事实源升级。

需要正式输出格式时读取 [`references/deliverable-templates.md`](references/deliverable-templates.md)。该文件是 Brief、状态矩阵、Visual DNA、Icon QA、商店图脚本和交付矩阵的唯一格式事实源；不要在其他文件另造冲突字段。

## 第二步：请求路由

只执行与请求有关的模块，禁止为了“完整”强迫用户走全流程。

| 请求 | 执行模块 | 跳过/延后 |
|---|---|---|
| 从零做 App IP | Brief → 母体 → 三方向 → 基础母版 | 未确认前不批量做状态/换装 |
| 已有 IP 做状态 | Identity Lock → 业务状态 → UI 联调 | 不重做已确认母题 |
| 已有 IP 做换装 | Identity Lock → 身份锚点 → Tier A/B/C | 不要求重做基础母版 |
| Icon-only / 图标型 IP | Brief → 母体 → Icon 支线 | 不强制角色职位、状态、换装 |
| 商店图-only，已有 IP | Visual DNA → Store 支线 | 不强制裸模流程 |
| 完整 App IP 系统 | 核心产品化 → Icon → Store → 交接 | 按检查点分阶段确认 |
| 普通无 IP branding/ASO | 不执行本 Skill | 路由相邻流程 |

### 按需读取

- 母体、基础母版、状态、换装、原创性：[`references/character-productization.md`](references/character-productization.md)
- App Icon、Visual DNA、Icon Composer 和代表尺寸 QA：[`references/app-icon-system.md`](references/app-icon-system.md)
- 商店图、Preview、Locale、claims、PPO/CPP：[`references/store-assets.md`](references/store-assets.md)
- AI 生图/改图、身份锁和版本回退：[`references/ai-image-iteration.md`](references/ai-image-iteration.md)
- 用户确认后的技术资产与交接：[`references/production-handoff.md`](references/production-handoff.md)
- 需要案例证据与反例时才读：[`references/before-click-patterns.md`](references/before-click-patterns.md)

不要无差别读取全部 reference。

## 第三步：App IP Brief

从产品和真实页面提取：

- 产品一句话、目标用户与核心任务
- 用户压力与失败语义
- App 名称、品牌资产和绝对禁用项
- 首页/高频页面、出现位置、真实尺寸和手势遮挡
- 已有业务状态、成功/错误责任主体
- 角色/IP 最多三个任务
- 首发资产范围与目标平台

使用模板输出精简 Brief，不把探索性想法包装成已确认事实。

## 第四步：选择 IP 母体

先保留“无新增 IP”作为基线，再选择一个主母体：

- **Character**：身份来自轮廓、脸、姿势和人格。
- **Object**：核心物件被英雄化，身份来自部件和功能动作。
- **Abstract/System**：身份来自形状、空间、节奏和运动语法。
- **Typographic/Attitude**：身份来自字形、名称、语气或反品类立场。
- **Hybrid**：一个主母体加一个辅助母体，必须明确主次。

非 Character 不执行眼鼻嘴、肢体、服装和角色骨架步骤。详细分支读取 `character-productization.md`。

## 第五步：三方向与选择

方向必须跨越不同联想距离：

1. 直译型：核心物件或行为；
2. 隐喻型：用户心理、关系或结果；
3. 系统/反常识型：抽象规则、矛盾组合或品牌态度。

每个方向说明：为何属于这个 App、为何不是品类默认答案、主识别机制、次级确认特征、适合场景、误读风险、小尺寸预判、扩展成本和原创风险。

一个主识别机制可由 1–3 个彼此依赖的结构组成，但不能有多个互抢中心。先按项目目标设权重，再评分；不要机械套同一排序。

用户未要求立即生图时先给概念。要求都画出来时生成有编号的方向板，但仍标记为探索。

## 第六步：基础母版与确认门槛

基础母版是**去除非结构性装饰后的身份事实源**：

- 装饰配件应移除后验证；
- 壳、容器、面罩、共生结构可作为身体不变量；
- 功能道具要分别验证有/无道具身份。

正式批量状态、换装和生产拆层必须等待母版确认。概念阶段允许做一个高风险状态和一个极端扩展探针，用于提前发现失败，但不能成为正式资产。

需要生成图片时读取 `ai-image-iteration.md`，每个版本保存 Prompt、输入、输出和用户结论。

## 第七步：App × IP 联调

按产品选择表现媒介，不默认 2.5D 或潮玩。颜色按品牌、主体、结构、表面和状态职责定义，不要求品牌色涂满 IP。

至少规划并按能力执行：浅/深界面、品牌色卡片、32/64/96pt、灰阶、非颜色状态编码、按钮与文本层级、手势遮挡、reduced motion 和 VoiceOver。

只有实际执行的项目标记已验证。

## 第八步：业务状态与扩展

状态先区分：

- 用户结果：completed / skipped / missed / milestone
- 系统执行：loading / syncing / offline / error / blocked
- 内容：empty / no-result / first-use
- 关系：idle / returning / waiting

系统错误不能表现成用户做错。每个状态写责任主体、触发条件、用户下一步、IP 表达、UI/文案职责和禁止行为。

换装按成本分级：Tier A 轻装、Tier B 主题装、Tier C 变体形态。骨架复用是成本决策，不是绝对创意禁令；核心状态反馈不能被付费破坏。

## 第九步：Icon、商店图与生产交接

- 涉及 Icon：读取 `app-icon-system.md`。当前平台规则必须核验并记录日期；不要把单张无透明 PNG 当所有平台的统一正式源。
- 涉及商店图/Preview：读取 `store-assets.md`。真实 App footage、当前版本功能、设备匹配、付费/登录披露、poster frame、Locale fallback 和 claims 必须检查。
- 用户最终确认后：读取 `production-handoff.md`，再制定骨架、图层、导出、命名、版本和 provenance。

## 原创性与权利底线

不复制著名 IP 的整体印象、独特结构组合、名称、典型姿势或受保护造型。对同品类 App、角色、玩具、商标和用户点名参考做可追溯筛查；中风险重构，高风险停止。快速筛查不替代法律意见。

商店图中的奖项、用户量、媒体、医疗、金融和 AI 效果必须可核验，不得为了转化虚构或隐藏重要访问条件。

## 最终质量关

按适用范围回答：

- 为什么它只属于这个 App？
- 32–64pt 靠什么识别？
- 去掉非结构装饰后是否仍有身份？
- 用户成功、等待、未完成和系统错误如何不同表达？
- 是否服务操作而不抢主层级？
- 新主题是否保留身份，成本属于哪个 Tier？
- Icon 在代表尺寸与货架中是否有核心身份 DNA？
- 商店图前三张是否讲清利益、差异和可信理由？
- IP 是否推动真实功能，而不是贴纸？
- 所有平台、claim、披露和权利是否已核验或明确标记待执行？

任一关键问题答不清，就不要进入正式生产。