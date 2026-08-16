# App Icon 风格选择与 Prompt 预设

只在请求涉及图标生成、图标风格选择或同一概念的跨风格比较时读取。本文件提供**表现媒介预设**，不替代 Brief、母体、Visual DNA、构图或平台规范。先在 `app-icon-system.md` 确定产品关联与主识别机制，再选择风格。

## 1. 证据边界

以下三类来自 2026-08-16 实际浏览的小红书视频笔记《2026 VibeCoding 创意｜APP 图标提示词》，属于“已验证笔记示例”：

- 3D 拟物 / 新拟物
- 极简扁平
- 高饱和波普艺术

其余预设是基于 App Icon 产品化原则整理的“系统扩展”，不是该笔记原文。不要把参考笔记的具体相机、火苗、猫或糖果主体复制到其他 App；只吸收媒介、构图、光影和负约束方法。

## 2. 先选风格，不先套风格

根据六个维度筛选候选：

1. **产品语义**：严肃工具、效率、金融、健康、陪伴、娱乐、创意或游戏；
2. **品牌人格**：克制、可信、温暖、活泼、叛逆、怀旧或未来感；
3. **母体与身份**：Character、Object、Abstract/System、Typographic；
4. **UI 一致性**：App 内是扁平卡片、系统材质、真实质感还是强插画；
5. **小尺寸预算**：主识别机制在 40–60px 是否依赖纹理、文字或细碎高光；
6. **差异机会**：同品类货架是同质化还是存在可用的反转空间。

默认推荐 **1 个主风格 + 1 个对照风格**。只有用户要求探索板时才给 3 个；不要把十种预设全部塞进一次生成。风格不是装饰滤镜：若改变媒介会破坏已确认身份，优先保持 Identity Lock。

## 3. 风格预设

### S01 极简扁平（已验证笔记示例）

- **适合**：效率、记账、提醒、工具、轻量陪伴；Character / Object / Abstract 均可。
- **选择信号**：UI 卡片简洁、需要强小尺寸识别、品牌希望清爽直接。
- **Prompt 增强块**：`minimal flat vector icon, bold geometric color masses, crisp silhouette, controlled solid or subtle gradient background, high figure-ground contrast, no outline unless it is identity-critical, no cast shadow, no volumetric rendering`
- **构图/光影**：正视或轻微 3/4；单一主体；不依赖光源塑形。
- **负约束**：`no 3D, no glossy plastic, no realistic texture, no complex scenery, no thin decorative lines, no tiny UI`
- **主要风险**：过度通用、像素材库；必须用独特轮廓或空间关系补足身份。

### S02 3D 拟物 / 新拟物（已验证笔记示例）

- **适合**：相机、音乐、创作、设备控制、生活方式；Object 母体优先。
- **选择信号**：核心物件本身有熟悉结构，品牌需要“可触摸、精工、复古工业”感觉。
- **Prompt 增强块**：`premium modern skeuomorphic object icon, front-facing or controlled three-quarter view, restrained realistic materials, finely modeled functional parts, soft studio key light, gentle contact shadow, isolated product rendering, tactile but simplified`
- **构图/光影**：物件居中；真实结构只保留能在小尺寸形成块面的部件；柔和棚拍光。
- **负约束**：`no busy scene, no floating accessories, no excessive micro-detail, no photoreal background, no brand marks, no text, no harsh chrome glare`
- **主要风险**：细节在 40–60px 糊成噪声、像电商产品图；需把真实物件英雄化而非完整复刻。

### S03 高饱和波普艺术（已验证笔记示例）

- **适合**：娱乐、社交、创意、活动、年轻化消费产品；Character / Object / Typographic。
- **选择信号**：品牌需要强货架冲击、幽默或反品类态度，UI 能承接高能量视觉。
- **Prompt 增强块**：`high-saturation pop-art app icon, bold black contour, halftone print texture, radial burst or speech-bubble geometry, punchy complementary colors, simplified central symbol, retro comic energy, screen-print finish`
- **构图/光影**：中心爆发式构图；轮廓粗；半调网点只作表现 DNA，不遮蔽主形。
- **负约束**：`no realistic depth, no soft luxury gradient, no delicate pastel palette, no crowded captions, no illegible comic text, no multiple competing bursts`
- **主要风险**：文字生成错误、货架噪声过高；除非字形就是确认 Logo，否则优先无文字符号。

### S04 软胶 / 黏土 2.5D（系统扩展）

- **适合**：陪伴、习惯、儿童、宠物、健康激励；Character / Object。
- **选择信号**：已有 IP 依赖体积、圆润轮廓与亲和触感，App 内也使用柔和卡片和角色反馈。
- **Prompt 增强块**：`soft 2.5D mascot icon, rounded molded form, matte soft-touch silicone or clay surface, broad simple planes, subtle ambient occlusion, diffused studio light, warm approachable volume, compact half-body composition`
- **构图/光影**：脸或核心结构优先；大曲面、少接缝；柔光而非高亮塑料。
- **负约束**：`no plush fibers, no wet glossy plastic, no porcelain skin, no toy-box scene, no tiny costume details, no dramatic cinematic lighting`
- **主要风险**：萌感同质化、材质漂移；必须锁定脸部坐标、轮廓和表面粗糙度。

### S05 玻璃 / 半透明系统材质（系统扩展）

- **适合**：AI、天气、系统工具、数据流、冥想；Abstract/System / Object 优先。
- **选择信号**：品牌强调流动、层级、智能或环境响应，目标平台工具链支持相应分层表现。
- **Prompt 增强块**：`translucent layered glass icon, one bold core symbol suspended in controlled depth, frosted and clear material contrast, edge refraction, restrained spectral highlight, readable silhouette, dark-and-light appearance compatible`
- **构图/光影**：最多 2–3 个层级；核心符号不能靠透明度才能成立；边缘高光受控。
- **负约束**：`no glass shards, no excessive rainbow caustics, no transparent-on-transparent loss, no illegible thin layers, no generic glowing orb, no sci-fi scene`
- **主要风险**：透明层在浅色/深色背景消失，生成图与真实 Icon Composer 行为不一致；必须分别做 appearance QA。

### S06 几何渐变 / 抽象系统（系统扩展）

- **适合**：生产力、金融、数据、安全、开发者工具；Abstract/System / Typographic。
- **选择信号**：不需要脸和物件直译，品牌希望成熟、可扩展到状态与动效。
- **Prompt 增强块**：`abstract geometric app icon, one proprietary spatial relationship, large interlocking shapes, controlled brand gradient, precise optical balance, clean negative space, scalable system mark, crisp silhouette at small size`
- **构图/光影**：靠形状咬合、切口、轨道或负空间识别；渐变服务空间层级而非装饰。
- **负约束**：`no generic infinity loop, no random blob, no generic AI sparkle, no excessive glow, no thin line network, no stock-logo symmetry unless identity-critical`
- **主要风险**：像通用 SaaS Logo；必须说明为何结构只属于该产品，并做同品类相似性筛查。

### S07 纸艺 / 剪纸分层（系统扩展）

- **适合**：阅读、教育、旅行、自然、文化内容；Object / Character / Abstract。
- **选择信号**：品牌需要人文、手作、故事感，但仍需保持清晰块面。
- **Prompt 增强块**：`layered paper-cut app icon, bold cut-paper silhouettes, limited stacked depth, subtle paper grain, soft directional shadow between layers, handcrafted but precise edges, editorial color palette`
- **构图/光影**：少量厚层；阴影只用于分层；主识别轮廓不能依赖纸纹。
- **负约束**：`no torn messy edges, no scrapbook clutter, no tiny paper pieces, no photoreal desk, no handwritten caption, no excessive layer count`
- **主要风险**：层数过多、像活动海报；限制为一个中心关系和少量层级。

### S08 线刻 / 印章 / 单色徽记（系统扩展）

- **适合**：专业工具、户外、汽车、知识、传统文化、高可信服务；Object / Typographic。
- **选择信号**：品牌强调可靠、耐久、专业，且核心轮廓可用单色成立。
- **Prompt 增强块**：`bold monoline or engraved emblem icon, one compact proprietary mark, controlled stroke weight, strong negative space, single-color-first design, subtle print or stamped character only if retained at 40px`
- **构图/光影**：先单色，再决定是否加入轻微纸墨或金属表现；线宽按最小尺寸反推。
- **负约束**：`no hairline detail, no ornate heraldry, no pseudo-luxury crest, no dense hatching, no long wording, no generic shield-and-check combination`
- **主要风险**：细线断裂、像机构徽章；必须进行 16–24px 模糊与单色测试。

### S09 像素 / 复古数码（系统扩展）

- **适合**：游戏、开发者工具、社区、怀旧记录；Character / Object / Typographic。
- **选择信号**：产品与数字文化、游戏语汇或可编程体验有真实联系。
- **Prompt 增强块**：`pixel-art app icon, deliberately limited pixel grid, one readable sprite or object, chunky clusters, crisp nearest-neighbor edges, limited retro palette, iconic silhouette, no accidental anti-aliasing`
- **构图/光影**：像素网格是结构，不是后期滤镜；减少色阶和抖动。
- **负约束**：`no mixed vector curves, no blurry upscale, no random dithering, no detailed game scene, no fake CRT overlay, no tiny HUD text`
- **主要风险**：缩放模糊、只剩怀旧装饰；需确保产品关系真实且导出链路保持硬边。

### S10 编辑插画 / 粗线手绘（系统扩展）

- **适合**：内容、生活方式、心理健康、社区、创作者产品；Character / Object。
- **选择信号**：品牌需要人味、幽默或不完美感，且已有插画语言可延伸进 UI 与商店图。
- **Prompt 增强块**：`editorial hand-drawn app icon, one expressive central subject, confident uneven contour, simplified screen-print color fills, intentional human gesture, strong silhouette, minimal textured accents`
- **构图/光影**：以线条节奏和形变表达人格；控制笔触数量，保持中心块面。
- **负约束**：`no sketchbook clutter, no pale unfinished construction lines, no watercolor wash reducing contrast, no detailed scene, no illegible handwriting, no imitation of a named illustrator`
- **主要风险**：小尺寸显脏、模仿具体艺术家；描述可观察视觉属性，不点名在世艺术家或复制独特风格。

### S11 单字母 / 字形态度（系统扩展）

- **适合**：品牌名短、字形已是核心资产的工具、媒体、社区；Typographic/Attitude。
- **选择信号**：名称或首字母拥有可注册、可持续的独特字形，且在代表尺寸仍是图形块。
- **Prompt 增强块**：`custom typographic app icon, one proprietary letterform or compact monogram, bold optical corrections, distinctive counter-shape, minimal palette, logo-like silhouette, no supporting copy`
- **构图/光影**：一个字形或极短组合；身份来自字腔、切口、倾角或连接关系。
- **负约束**：`no full app name, no generic font rendering, no random calligraphy, no slogan, no illegible ligature, no trademark imitation`
- **主要风险**：AI 拼字错误、与商标近似；最终字形应人工矢量化并做商标筛查。

## 4. 风格组合规则

- 默认只有一个**主媒介**，例如 `极简扁平`；可以附一个低强度表现 DNA，例如轻微纸纹，但不能把 `Flat + 玻璃 + 软胶 + 波普` 并列堆叠。
- 合理 Hybrid 必须说明主次和因果，例如“几何渐变为主，玻璃仅用于核心数据层的边缘折射”。
- 同一轮比较风格时，保持主体、构图、配色职责和 Identity Lock 不变；风格是唯一主变量。
- 同一轮比较构图时，固定风格；不要同时换媒介、主体和视角。
- 风格预设只追加到 `app-icon-system.md` 的结构化 Prompt，不覆盖 Asset contract、Product association、Identity lock、Small-size contract 和 Output。

## 5. 输出选择卡

```markdown
| Candidate style | Evidence source | Product/brand fit | UI fit | Identity fit | 40–60px risk | Shelf difference | Production risk | Decision |
|---|---|---|---|---|---|---|---|---|
| | 笔记已验证 / 系统扩展 | | | | | | | 主 / 对照 / 淘汰 |

- 主风格：
- 对照风格：
- 淘汰风格与原因：
- 本轮唯一比较变量：
- 待用户确认：
```

若用户已明确指定风格且不与产品、身份或可访问性冲突，直接使用，不强迫重新选择；但仍补全对应负约束和小尺寸契约。若指定风格明显损害任务识别或复制具体 IP/艺术家，说明风险并给相邻替代方案。
