# teleget-downloader

本包**不包含** TeleBackup 程序文件，只会在你运行命令时**用系统默认浏览器打开**官方 GitHub 仓库的 **Releases** 页面，便于下载 Windows 安装包与查看说明。

- 仓库：<https://github.com/xwc9527/TeleBackup-telegram-backup>
- 官网：<https://chatdex.cc>

安装：

```bash
pip install teleget-downloader
```

使用（打开最新 Release）：

```bash
teleget-downloader
```

或：

```bash
python -m teleget_downloader
```

打开仓库主页（非 Releases）：

```bash
teleget-downloader --repo
```
