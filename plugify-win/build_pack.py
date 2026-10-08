#!/usr/bin/env python3
"""构建 plugify-pack-win.zip。

从 plugify-metamod-loader GitHub Release 下载 Windows 构建（tar.bz2），
重打包为功能组件格式（game/csgo/addons/ 结构 + README.md）。
输出到仓库根目录 plugify-pack-win.zip（不上传 git，只上传 GitHub Release）。
"""
import os
import shutil
import tarfile
import tempfile
import urllib.request
import zipfile

VERSION = "2.1.4"
SHA = "2d1e135"
BASE_URL = (
    f"https://github.com/untrustedmodders/plugify-metamod-loader/releases/download/"
    f"v{VERSION}/plugify-metamod-loader-build-win64-{SHA}.tar.bz2"
)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ZIP = os.path.normpath(os.path.join(HERE, "..", "plugify-pack-win.zip"))


def main():
    tmp = tempfile.mkdtemp(prefix="plugify-win-build-")
    try:
        src = os.path.join(tmp, "plugify.tar.bz2")
        print("下载 Plugify Windows 包:", BASE_URL)
        urllib.request.urlretrieve(BASE_URL, src)
        print("解压 ...")
        with tarfile.open(src, "r:bz2") as t:
            t.extractall(tmp)

        # 解压后顶层为 csgo/
        src_csgo = os.path.join(tmp, "csgo")

        if os.path.exists(OUT_ZIP):
            os.remove(OUT_ZIP)
        with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(HERE, "README.md"), "README.md")
            for dp, _, fs in os.walk(src_csgo):
                for fn in fs:
                    full = os.path.join(dp, fn)
                    rel = os.path.relpath(full, src_csgo)
                    z.write(full, os.path.join("game", rel))
        print("已生成: %s (%.1f MB)" % (OUT_ZIP, os.path.getsize(OUT_ZIP) / 1024 / 1024))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()