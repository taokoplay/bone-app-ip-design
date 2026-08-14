# App Icon 与视觉系统

只在请求涉及 App Icon、图标型 IP 或跨载体 Visual DNA 时读取。案例证据可再读取 `before-click-patterns.md`；输出格式读取 `deliverable-templates.md`。

## 1. 先核验平台与货架

开始前记录目标平台、OS/Xcode、Icon Composer 或 Asset Catalog 路径，并核验当前 Apple HIG、Icon Composer 和提交规范。平台规则必须带可访问来源 URL 与实际核验时间 `checked_at`；只有本轮确实打开或抓取官方来源后才能填写日期。无法联网或未实际访问时写 `checked_at: N/A（待官方核验）`，不要用当前日期冒充已核验，也不要把历史规则当当前事实。

抽样同品类货架，记录主色/明度、主体类型、构图密度、常见陈词和空缺机会。趋势只提供语境，不替代产品策略。

## 2. 三种策略方向

1. **品类直读**：一眼理解用途。
2. **品牌反转**：在同品类形成相反明度、构图、媒介或态度。
3. **IP 世界观**：用 Character、Object、System 或 Typography 建立长期资产。

方向先比较策略；选中候选后再比较 Flat、材质化或其他表现媒介，不默认 2.5D。

## 3. 小尺寸识别预算

默认只保留一个主识别机制、最多一个辅助动作/功能物和一个背景关系。一个机制可由多个互相依赖的结构构成。

确保小尺寸有稳定主色关系和清晰块面，但不机械限定 60% 占比或 2–3 色；摄影、游戏、渐变和系统材质可有理由突破。禁止缩小 UI、无关道具堆叠和复杂场景。

角色型通常用脸或半身；允许自然裁切，但不得非等比拉伸。文字型 Icon 只有在字形本身即 Logo、代表尺寸下仍形成图形块时成立。

## 4. Visual DNA

Icon、UI、IP 与商店图至少共享：

- 一项**核心身份 DNA**：超级符号、轮廓、核心物件或独特空间关系；
- 一项**表现 DNA**：颜色职责、材质、字体语气、笔触或动效节奏。

填写跨载体仍可识别的最小集合、允许变化和 Never change。

## 5. 资产层级

不要把“正式母版”统一等同于一张无透明 PNG。

1. **Canonical artwork master**：可编辑、可分层；不烘焙系统圆角和系统效果。
2. **Icon Composer source**：按目标平台配置层级、背景和 appearance；核验当前支持的 Default / Dark / Clear / Tinted 组合。
3. **Flattened compatibility export**：仅在当前工具链或 Asset Catalog 路径需要时输出；PNG、Alpha、颜色空间和背景以目标平台当前规范为准。

不得让需要不透明背景的最终导出意外透明，也不得把跨平台 Alpha 规则写成统一硬要求。

## 6. QA

1024 / 180 / 87 / 60 / 40 / 29px 仅作为 **iPhone representative rendered-size QA**，不是上传尺寸清单。最终尺寸、遮罩和 appearance 由目标平台及当前工具链决定；iPad、Mac、Watch、TV、visionOS 分别验证。

至少检查：

- 代表尺寸识别
- 16–24px 模糊块面
- 灰阶和非颜色编码
- 浅/深桌面
- 系统圆角/遮罩裁切
- 竞品货架差异
- 身份保真
- appearance 与层级效果
- 目标平台实际工具链预览

没有实际生成预览时，只能输出 QA 计划。

## 7. 迭代与交付

先出三方向货架板并选择方向；定方向后可用多模型探索，但不是硬要求。保存 Prompt、母版、模型、版本、用户结论、官方来源和核验日期。生产交接读取 `production-handoff.md`。