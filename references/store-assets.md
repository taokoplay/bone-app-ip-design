# App Store 商店图与 App Preview

只在请求涉及商店图、Preview、IP 商店视觉或产品页实验时读取。案例证据可读取 `before-click-patterns.md`；正式格式读取 `deliverable-templates.md`。

## 1. 能力与规范核验

开始前核验当前 App Store Connect、App Review、截图和 Preview 官方规范，记录可访问来源 URL 与实际核验时间 `checked_at`；只有本轮确实访问官方来源后才能填写日期，否则写 `checked_at: N/A（待官方核验）`。探测目标账户/地区是否已开放 Product Page Header、Search Results creative、Asset Library 等能力；未开放或未实际探测则只做 future-ready 规划。

具体像素、文件格式、时长和数量上限以当次官方规范为准。创意上默认只制作 3–8 个强命题，但这不是平台上限；强五张优于弱八张。

## 2. 输入与 ASO 接口

收集目标用户、下载动机、主承诺、差异点、可信证据、核心闭环、隐私/安全机制、长期价值、IP 职责、可用 UI/设备/结果素材、目标 Locale 和访问条件。

本 Skill 不替代完整 ASO。需要关键词和 metadata 时建立 ASO Intent Card，并路由专门流程；视觉必须与已确认的搜索意图、App name/subtitle 承诺和 CPP 落点一致。

## 3. Caption-first 脚本

先写单句卡片，再选画面。每张只承担一个主要销售任务：用户情境、用户结果标题、真实证明画面、IP 职责、构图类型和下一张理由。

标题卖结果，品牌层提供感觉，真实 UI/数据负责证明。默认控制三种信息职责；若更多元素仍保持唯一视觉中心，可有理由突破。

## 4. 首屏与序列

- 新产品：主利益 + 最强结果。
- 强奖项/用户量：可信证据 + 品牌。
- 陪伴型 IP：关系承诺 + 真实互动。
- 创作工具：先展示结果。
- 健康/金融/AI：主利益后尽早给具体安全、隐私或限制证据。

推荐序列按需取 3–8 张：Hook → Difference → Proof → Core Loop A/B → Personalization → Expansion → Growth/Freshness。不是固定模板；每张必须有独立销售任务。

IP 若出现，至少承担主角、执行者、反馈者、进度载体、导游或社交媒介之一。删除 IP 后故事仍完全成立，说明它只是贴纸。

## 5. 构图与节奏

按命题选：完整设备、无框 UI、局部设备、无设备结果/证据、或多设备组合。多设备只能有一个第一视觉中心。

可用连续品牌场或章节变色。连续画布只能奖励滑动，不能让单页失去理解。不要让所有页面都成为同尺寸手机模板。

## 6. Claims、权利与访问披露

奖项、评价、用户量、医生/专家、健康、金融和 AI 效果都需要来源、日期、适用地区、当前版本支持和复核期限。第三方商标、人物、内容和设备画面要有权利依据。

每张截图和 Preview 功能记录：

- Free
- Account required
- Subscription required
- In-App Purchase required
- Region / device / OS restricted
- Disclosure placement

不得为了转化隐藏门槛或展示当前提交版本不存在的能力。

## 7. App Preview

以目标设备上捕获的真实 App footage 为主体。IP 动画、文字和图形只能解释或强化真实体验，不得替代核心操作或制造不存在的行为。

创意参考：0–3 秒最强结果；3–8 秒核心操作；8–15 秒结果/反馈；后续展示差异、个性化和长期价值。时长以当前官方规格为准，常见 15–30 秒仅作经验参考。

默认不使用独立 Logo 片头；若品牌是核心动机，Logo 与首个产品结果同步出现，不消耗前几秒等待。静音必须可理解。

第一帧不等于 poster frame。0–3 秒内准备强关键帧，并在 App Store Connect 显式选择和检查 poster frame；记录变更是否需要重新审核。

## 8. 本地化与 fallback

本地化是重新写作和排版，不是替换字符串。同步 UI、日期、数字、货币、单位、名字和对白。RTL 检查阅读顺序、角色视线、气泡、手势和跨页关系。

每个 Locale 记录截图源语言、Preview 源语言、fallback 是否允许、fallback 结果、UI 与 metadata 语言是否一致。敏感市场不允许未经人工检查的 Preview fallback。

## 9. PPO、CPP 与数据迭代

- **PPO**：测试默认产品页 Icon、截图或 Preview。先定义单一假设，避免同时改变无法归因的多个变量。
- **CPP**：针对受众、关键词、广告或功能入口；保持素材承诺、deep link 和 App 内落点一致。

达到预设最低 impressions/downloads 或实验置信度后复盘；2–4 周只是高流量项目的运营参考。记录假设、主指标、护栏指标、停止条件和结论。

## 10. 提交 QA

逐平台、设备族、尺寸桶、方向、Placement、Locale 核验：当前版本功能、设备 UI 匹配、像素/格式/时长、claim、权利、披露、fallback、poster frame 和审核状态。没有实际上传或预览，标记“待工具执行”，不能写成已通过。