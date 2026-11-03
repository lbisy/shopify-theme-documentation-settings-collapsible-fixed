# Logo

Logo 设置用于管理商店的品牌 Logo 和浏览器图标。

## 打开 Logo 设置

1. 登录 Shopify 后台。
2. 进入 **在线商店 > 主题**。
3. 找到当前使用的主题，点击 **自定义**。
4. 点击左侧的 **主题设置**。
5. 选择 **Logo**。

![打开 Logo 设置](/images/zh/settings/logo.png)

## Logo

在 **Logo** 设置中，你可以上传商店的品牌 Logo。

点击 **选择图片** 上传新的 Logo，或者从 Shopify 文件库中选择已经上传的图片。

![上传 Logo](/images/zh/settings/logo.png)

### 建议

为了获得更好的显示效果，建议：

- 使用 PNG、JPG、WebP 或 SVG 格式的图片。
- 如果 Logo 需要显示在不同颜色的背景上，建议使用透明背景的 PNG 图片。
- 上传清晰度较高的图片，避免 Logo 在高分辨率设备上显示模糊。
- Logo 图片周围尽量不要保留过多空白区域。

::: tip 提示
上传 Logo 后，请同时检查桌面端和移动端的显示效果。
:::

## Logo width

**Logo width** 用于调整 Logo 在网站中的显示宽度。

拖动设置中的滑块即可调整 Logo 大小。

![调整 Logo 宽度](/images/zh/settings/logo.png)

数值越大，Logo 显示尺寸越大；数值越小，Logo 显示尺寸越小。

::: warning 注意
Logo width 只会调整 Logo 的显示尺寸，不会修改原始图片的实际尺寸。
:::

建议根据 Header 的高度和导航菜单数量调整 Logo 宽度。

如果导航菜单较多，可以适当减小 Logo 宽度，为菜单保留更多显示空间。

## Favicon

Favicon 是显示在浏览器标签页、浏览器收藏夹以及部分移动设备快捷方式中的网站图标。

点击 **选择图片** 上传 Favicon。

![上传 Favicon](/images/zh/settings/logo.png)

建议使用：

- 正方形图片
- 简洁的品牌图标
- 清晰、容易识别的设计
- PNG 格式图片

由于 Favicon 的实际显示尺寸较小，不建议使用包含大量文字或复杂细节的图片。

::: tip 推荐
如果你的品牌 Logo 包含“图标 + 文字”，建议只使用图标部分作为 Favicon。
:::

## 保存设置

完成 Logo 设置后，点击主题编辑器右上角的 **保存**。

![保存 Logo 设置](/images/zh/settings/logo.png)

保存后，建议检查以下内容：

- Logo 是否清晰显示。
- Logo 大小是否合适。
- Logo 与导航菜单之间是否有足够空间。
- 移动端 Logo 是否正常显示。
- Favicon 是否成功更新。

::: info 提示
浏览器可能会缓存旧的 Favicon。如果修改 Favicon 后没有立即显示，可以尝试刷新浏览器缓存或使用无痕窗口查看。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `config/settings_schema.json` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 主题设置 → Logo

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Logo<br>`logo` | image_picker：选择或上传图片 | 未声明 | — |
| Logo width<br>`logo_width` | range：拖动滑块调整数值 | 100 | 50–300 px; 步长 10 |
| Favicon<br>`favicon` | image_picker：选择或上传图片 | 未声明 | info: Recommended size: 32 × 32 px. |

<!-- latest-schema:end -->
