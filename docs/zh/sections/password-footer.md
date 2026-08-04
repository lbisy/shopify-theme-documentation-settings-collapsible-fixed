# Password Footer（密码页页脚）

**Password footer** 是商店密码模板底部的页脚区域，用于显示商店的社交平台链接，并控制页脚的配色与上下间距。页脚还包含 Shopify 署名和店主登录链接。

![Password footer 设置面板与店铺预览](/images/zh/password-footer.png)

## 打开 Password footer

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 在需要编辑的主题上点击 **自定义**。
3. 打开编辑器顶部的模板选择器，选择 **Password（密码）**。
4. 在左侧 **Template（模板）** 下选择 **Password footer**，不要与 **Password header** 或 **Password** 混淆。
5. 配置各项设置，并同步查看店铺预览。
6. 点击右上角的 **保存**。

Password footer 是密码模板结构的一部分，通常不需要作为普通分区另行添加。品牌标识和密码进入链接在 **Password header** 中配置；上线通知和邮箱订阅表单则在 **Password** 中配置。

## Color scheme（配色方案）

选择页脚使用的全局配色方案。它会影响页脚背景、社交图标、Shopify 署名、店主登录链接，以及主题定义的悬停和焦点状态。

点击 **Edit scheme（编辑方案）** 可以修改所选的全局方案。一个方案可能被多个分区共用，因此修改后可能影响商店的其他区域。请检查文字、链接、图标和键盘焦点标识的对比度。

## Show social media icons（显示社交媒体图标）

开启 **Show social media icons** 后，页脚会显示在 **Theme Settings** 中已配置社交主页所对应的图标。截图中此开关已开启，店铺预览里显示了 Facebook、Instagram 和 YouTube 图标。

只有对应字段中填写了内容的平台才会生成图标。不使用的平台应保持为空。该开关不会验证链接，因此 `1`、`2`、`3` 这类不完整内容也可能生成图标，但无法把访客带到有效的品牌主页。

## Padding（上下间距）

- **Padding top**：控制社交图标上方的留白；没有显示图标时，则控制页脚信息上方的留白。
- **Padding bottom**：控制店主登录链接下方的留白。

截图中两个值均为 `32 px`，可作为均衡的初始设置。请同时检查移动端效果，尤其要留意署名或登录提示换行后的间距。

## Theme Settings：社交主页链接

**Theme Settings** 组中的字段是全局社交主页设置，会被主题中所有支持社交图标的区域共用。每个账号都应填写以 `https://` 开头的完整公开主页网址。在此处修改链接，也可能同时影响主站页眉、页脚或其他社交分区。

| 平台 | 截图中的内容 | 发布说明 |
| --- | --- | --- |
| **Facebook** | `1` | 不完整的占位内容；需替换为完整的 Facebook 主页网址。 |
| **Instagram** | `2` | 不完整的占位内容；需替换为完整的 Instagram 主页网址。 |
| **YouTube** | `3` | 不完整的占位内容；需替换为完整的 YouTube 频道网址。 |
| **TikTok** | `https://tiktok.com/@shopify` | 需替换为商店自己的 TikTok 主页网址。 |
| **X / Twitter** | `https://x.com/shopify` | 需替换为商店自己的 X 主页网址。 |
| **Pinterest** | `https://pinterest.com/shopify` | 需替换为商店自己的 Pinterest 主页网址。 |
| **Snapchat** | `https://www.snapchat.com/add/shopify` | 需替换为商店自己的 Snapchat 主页网址。 |
| **Tumblr** | `https://shopify.tumblr.com` | 需替换为商店自己的 Tumblr 主页网址。 |
| **Vimeo** | `https://vimeo.com/shopify` | 需替换为商店自己的 Vimeo 主页网址。 |

发布前请逐一打开网址，确认其进入预期的品牌公开主页，并移除追踪参数、临时登录链接以及商店已停止维护的账号。

## Shopify 署名与店主登录

页脚预览中包含 **Powered by Shopify** 和 **Are you the store owner? Log in here（您是店主吗？在此登录）**。这些文字通常由主题语言翻译控制，而不是在当前分区面板中填写。登录链接供店主使用，不会向顾客开放店面访问权限。

翻译相关文字时，应清楚保留“店主提示”和“登录操作”的含义。请在无痕窗口中测试链接，切勿把管理员密码或店面密码写入页脚文字、社交字段、截图或公开文档。

## 截图配置示例

| 设置项 | 截图中的示例值 |
| --- | --- |
| Color scheme | 深绿色页脚方案 |
| Show social media icons | 开启 |
| Padding top | `32 px` |
| Padding bottom | `32 px` |
| 预览中可见的图标 | Facebook、Instagram、YouTube |

截图中的社交字段仅为演示数据。发布前必须将所有示例或占位内容替换为商店自己经过验证的主页网址。

## 发布前检查

1. 将 `1`、`2`、`3` 和所有 Shopify 示例主页替换为商店自己的完整网址。
2. 不使用的社交平台字段保持为空。
3. 逐一打开链接，确认能够进入正确的公开主页。
4. 检查页脚背景、文字、图标、链接、悬停状态和焦点标识的对比度。
5. 检查桌面端和移动端的间距与文字换行。
6. 分别使用鼠标、键盘和触控操作测试每个可见图标与店主登录链接。
7. 确认社交图标具有可识别平台名称的无障碍标签，并显示清晰的键盘焦点。
8. 保存主题，并在无痕窗口中完成最终检查。
