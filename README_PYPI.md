# telebackup-telegram-downloader

> **关于本 PyPI 包**  
> 本包为**轻量引导工具**：`pip install telebackup-telegram-downloader` 后运行 `telebackup-telegram-downloader` 或 `telebackup`，会用系统浏览器打开官方 **GitHub Releases** 页面。**不包含** TeleBackup 桌面程序本体；安装包请从 [Releases](https://github.com/xwc9527/TeleBackup-telegram-backup/releases) 或官网 [chatdex.cc](https://chatdex.cc/zh/download) 获取。  
>  
> 以下为 **TeleBackup** 产品说明（与仓库 / 官网介绍一致）。

## 如何使用本 PyPI 包

```bash
pip install telebackup-telegram-downloader
telebackup-telegram-downloader
# 或：telebackup
# 或：python -m telebackup_telegram_downloader
```

添加 `--repo` 可打开仓库主页（而非 Releases 最新页）。

---

## TeleBackup Telegram Downloader

**TeleBackup** —— Telegram **备份与归档**、**媒体批量下载**与**频道 / 群组内容同步**的桌面辅助工具。

TeleBackup 是一款面向 Telegram 用户的桌面应用，采用 **Flet** 构建界面，通过 **Telethon** 与 Telegram 交互。适用于在**合规、自用**前提下，将你有权访问的对话内容进行**本地归档**、按规则**批量保存媒体**，以及将源频道 / 群组内容**结构化同步**到目标对话（镜像 / 整理场景），减轻手工导出与整理的负担。

若你在官方客户端中遇到部分媒体**不便保存**、需要**长期本地留存**频道资料，或需要在**自己管理的对话之间**做内容迁移与整理，可在遵守服务条款与当地法律的前提下使用本工具辅助完成。**功能效果受 Telegram 与对话设置影响**，请以实际运行结果为准。

---

## 主要解决的用户痛点

- 部分媒体在官方客户端中保存不便、需要本地化归档  
- 大量频道 / 群组历史消息与附件需要**批量、可续传**地整理到本地  
- 转发或简单复制时容易出现结构不完整、相册顺序混乱等问题  
- 本地文件与消息量大时，需要**搜索、筛选与导出**能力  

---

## 核心功能一览

- **下载与归档**：支持常见媒体与文件类型；内置断点续传、并发与进度展示，适合大体积文件的稳定拉取（具体是否可用取决于账号权限与对方设置）。  
- **结构化镜像同步**：可将源对话的消息、媒体、话题与评论等按结构同步到目标位置；支持规则侧调整（链接、按钮、文案等），便于二次整理与发布（请在**有权访问**的对话范围内使用）。  
- **本地数据库**：消息写入本地 **SQLite**，支持关键词与条件检索，便于离线浏览与查找。  
- **导出与目录组织**：可导出 HTML / CSV 等；按频道、日期、类型等组织本地目录，并支持命名规则。  
- **多账号**：在界面内管理多账号；可配合 **Telegram Desktop** 的 `tdata` 导入会话（按官方与工具说明操作）。  
- **增量与去重**：侧重仅处理新增或变更，并减少重复拉取与写入。  

### 其他特性

- 支持论坛话题与评论区抓取（在协议与权限允许范围内）  
- 标签与收藏夹；磁盘占用提示  
- 系统代理与 SOCKS5 / HTTP 代理  
- **相册 / 媒体组**尽量按组处理以保持顺序与完整性（受平台与消息类型影响）  
- 可选 **Hash Breaker**：对文件做去重特征处理（一般**不改变**肉眼可见内容），用于部分场景下的哈希重复判定；请按需、合规使用  

---

## 适合哪些用户

- 需要**本地备份**自己参与的聊天与订阅内容的个人用户  
- 需要**镜像或整理**自有频道 / 群组内容的运营者  
- 需要**批量导出与检索**历史资料做归档的研究或自用场景  

TeleBackup 适合作为 **Telegram 归档、媒体整理、频道同步**等需求的辅助工具；请始终在个人合法用途范围内使用。

---

## 重要提醒

本工具仅限 **个人合法** 的备份、归档与同步。请遵守 **Telegram 服务条款** 与适用的法律法规；**不得**用于未经许可抓取、传播他人内容或规避监管的用途。`data/` 目录含会话与配置，请妥善保管与备份，勿随意分享。

**支持平台**：目前主要适配 **Windows 10 / 11（64 位）**。  
**当前产品版本**：**v1.2.5**（桌面程序，持续更新；**本 PyPI 引导包**的版本号以项目页 / `pip show` 为准）。

---

## 链接

- GitHub：<https://github.com/xwc9527/TeleBackup-telegram-backup>  
- 官网：<https://chatdex.cc>  
- 博客：<https://chatdex.cc/zh/blog>  
- 下载：<https://chatdex.cc/zh/download>  
