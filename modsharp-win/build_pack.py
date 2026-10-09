#!/usr/bin/env python3
"""构建 modsharp-pack-win.zip。

从 ModSharp GitHub Release 下载 Windows 包，
重打包为功能组件格式（game/sharp/ 结构 + README.md）。
输出到仓库根目录 modsharp-pack-win.zip（不上传 git，只上传 GitHub Release）。
"""
import os
import shutil
import tempfile
import urllib.request
import zipfile

VERSION = "git-187"
# 上游资产名为 ModSharp-git187-windows.zip（git 后无连字符）
ASSET_VERSION = VERSION.replace("-", "")
BASE_URL = (
    f"https://github.com/Kxnrl/modsharp-public/releases/download/"
    f"{VERSION}/ModSharp-{ASSET_VERSION}-windows.zip"
)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ZIP = os.path.normpath(os.path.join(HERE, "..", "modsharp-pack-win.zip"))


def main():
    tmp = tempfile.mkdtemp(prefix="modsharp-win-build-")
    try:
        src_zip = os.path.join(tmp, "modsharp.zip")
        print("下载 ModSharp Windows 包:", BASE_URL)
        urllib.request.urlretrieve(BASE_URL, src_zip)
        print("解压 ...")
        with zipfile.ZipFile(src_zip) as z:
            z.extractall(tmp)

        # 解压后顶层为 sharp/
        src_sharp = os.path.join(tmp, "sharp")

        if os.path.exists(OUT_ZIP):
            os.remove(OUT_ZIP)
        with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(HERE, "README.md"), "README.md")
            for dp, _, fs in os.walk(src_sharp):
                for fn in fs:
                    full = os.path.join(dp, fn)
                    rel = os.path.relpath(full, src_sharp)
                    z.write(full, os.path.join("game", "sharp", rel))
        print("已生成: %s (%.1f MB)" % (OUT_ZIP, os.path.getsize(OUT_ZIP) / 1024 / 1024))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()