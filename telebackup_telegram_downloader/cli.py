"""在浏览器中打开 TeleBackup GitHub 页面（Releases / 仓库主页）。不含应用本体。"""

from __future__ import annotations

import argparse
import webbrowser
from typing import List, Optional

REPO = "https://github.com/xwc9527/TeleBackup-telegram-backup"
RELEASES_LATEST = f"{REPO}/releases/latest"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="在浏览器中打开 TeleBackup 的 GitHub 页面；本包不包含应用本体。",
    )
    parser.add_argument(
        "--repo",
        action="store_true",
        help="打开仓库主页，而不是 Releases（最新版）页面",
    )
    args = parser.parse_args(argv)
    url = REPO if args.repo else RELEASES_LATEST
    print("TeleBackup — 正在打开：")
    print(url)
    print("若未自动跳转，请复制上方地址到浏览器。")
    webbrowser.open(url)
    return 0
