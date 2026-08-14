# 生产资产与技术交接

用户确认视觉方向后读取。概念阶段只规划，不提前切全套生产资源。

## 1. 视觉事实源

每个事实源必须包含：Character/IP ID、版本、批准日期、批准人、可编辑母版、导出件、Identity Lock、允许变化、废弃方向和 provenance。

## 2. 技术路线

根据实际产品选择：

- 原生矢量 / SF Symbols 风格资产
- 静态 PNG / WebP / HEIF（以平台支持为准）
- Lottie / Rive
- Spine
- 序列帧
- 程序化几何或原生动画

先用首页或最高频页面的最小资产验证尺寸、性能和动效，再扩展全套。

## 3. 交接内容

- Canonical front / side / 3/4 masters（适用时）
- Skeleton、anchor points、骨架复用等级
- State matrix 与责任主体
- Expression / component layers
- Outfit tiers、遮挡和碰撞规则
- Light / dark / background variants
- Icon artwork master、Icon Composer source、兼容导出和 QA
- Visual DNA Card 与货架板
- Store screenshot script、可编辑母版、Locale/placement exports
- Preview storyboard、真实录屏、overlays、poster frame 和 disclosures
- 动效时长、循环规则、打断行为、reduced-motion fallback
- 文件命名、版本和 rights/provenance log

正式字段使用 `deliverable-templates.md`。

## 4. 命名与版本

建议结构：

```text
[ip-id]_[asset]_[state-or-theme]_[appearance]_[locale]_[platform]_v[major.minor.patch]
```

- Major：身份或骨架变化。
- Minor：状态、主题或载体扩展。
- Patch：不改变身份的局部修正。

用户确认的版本才能成为 canonical source。旧方向降级为探索或材质参考，不删除生成历史。

## 5. 最终验证

按适用范围执行：

- 剪影、灰阶、32/64/96pt、浅/深背景
- 状态不依赖颜色和文案的理解测试
- 无非结构装饰身份测试
- 换装/主题身份与骨架成本测试
- 动效干扰、打断、VoiceOver、reduced motion
- Icon 代表尺寸、模糊、货架、appearance 和工具链测试
- 商店图前三张、单页独立性、Locale、claims、disclosure 和设备匹配
- Preview 静音、真实操作、poster frame、付费/登录披露
- 原创性、商标、版权和来源记录

标记每项为：已验证 / 基于输入推断 / 待工具执行 / 待用户确认。