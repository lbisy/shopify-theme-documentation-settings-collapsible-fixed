# 中英文对应页面切换说明

项目已经改为使用 VitePress 内置多语言功能。

现在语言菜单会按当前页面路径切换：

- `/en/getting-started` → `/zh/getting-started`
- `/en/product-pages` → `/zh/product-pages`
- `/en/sections/video-banner` → `/zh/sections/video-banner`

只要中英文 Markdown 文件使用相同的文件名和目录结构，语言切换就会停留在对应页面。

## 添加新页面时

请同时创建：

```text
docs/en/example-page.md
docs/zh/example-page.md
```

两个文件名必须一致。
