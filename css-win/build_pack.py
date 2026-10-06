#!/usr/bin/env python3
"""构建 css-pack-win.zip。

从 CounterStrikeSharp GitHub Release 下载 Windows with-runtime 包，
重打包为功能组件格式（game/csgo/addons/ 结构 + README.md）。
输出到仓库根目录 css-pack-win.zip（不上传 git，只上传 GitHub Release）。
"""
import os
import shutil
import tempfile
import urllib.request
import zipfile

VERSION = "1.0.376"
BASE_URL = (
    f"https://github.com/roflmuffin/CounterStrikeSharp/releases/download/"
    f"v{VERSION}/counterstrikesharp-with-runtime-windows-{VERSION}.zip"
)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ZIP = os.path.normpath(os.path.join(HERE, "..", "css-pack-win.zip"))


def main():
    tmp = tempfile.mkdtemp(prefix="css-build-")
    try:
        src_zip = os.path.join(tmp, "css.zip")
        print("下载 CSS 包:", BASE_URL)
        urllib.request.urlretrieve(BASE_URL, src_zip)
        print("解压 ...")
        with zipfile.ZipFile(src_zip) as z:
            z.extractall(tmp)

        if os.path.exists(OUT_ZIP):
            os.remove(OUT_ZIP)
        with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(HERE, "README.md"), "README.md")
            src_addons = os.path.join(tmp, "addons")
            for dp, _, fs in os.walk(src_addons):
                for fn in fs:
                    full = os.path.join(dp, fn)
                    rel = os.path.relpath(full, src_addons)
                    z.write(full, os.path.join("game", "csgo", "addons", rel))
        print("已生成: %s (%.1f MB)" % (OUT_ZIP, os.path.getsize(OUT_ZIP) / 1024 / 1024))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()