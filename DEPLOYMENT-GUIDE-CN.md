# Vercel 部署说明

## 方法一：GitHub + Vercel

1. 将本项目完整上传到 GitHub 仓库根目录。
2. 登录 Vercel，点击 **Add New → Project**。
3. 导入该 GitHub 仓库。
4. Vercel 会读取 `vercel.json`。
5. 确认：
   - Build Command：`npm run build`
   - Output Directory：`docs/.vitepress/dist`
6. 点击 Deploy。

## 本地预览

```bash
npm install
npm run dev
```

## 替换截图

将真实截图替换到：

- `docs/public/images/zh/`
- `docs/public/images/en/`

保持原文件名不变即可，不需要修改 Markdown。
