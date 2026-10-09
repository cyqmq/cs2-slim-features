#!/usr/bin/env python3
"""构建 link-manager-pack.zip。

从 cs2-link-manager GitHub 仓库（main 分支）下载源码，
连同启动器打包为功能组件格式（cs2lm / cs2lm.bat / tools/cs2lm/）。
输出到仓库根目录 link-manager-pack.zip（不上传 git，只上传 GitHub Release）。
"""
import os
import shutil
import tempfile
import time
import urllib.request
import zipfile

SOURCE_URL = "https://github.com/cyqmq/cs2-link-manager/archive/refs/heads/main.zip"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ZIP = os.path.normpath(os.path.join(HERE, "..", "link-manager-pack.zip"))


def _add_file(z, src, arc, mode=0o644):
    """写文件到 zip 并显式记录 Unix 权限位（zipfile.write 在 Windows 上会丢失执行位）。"""
    with open(src, "rb") as f:
        data = f.read()
    info = zipfile.ZipInfo(arc)
    info.date_time = time.gmtime(os.path.getmtime(src))[:6]
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (mode & 0xFFFF) << 16
    z.writestr(info, data)


def main():
    tmp = tempfile.mkdtemp(prefix="link-manager-build-")
    try:
        src_zip = os.path.join(tmp, "source.zip")
        print("下载 cs2-link-manager 源码:", SOURCE_URL)
        urllib.request.urlretrieve(SOURCE_URL, src_zip)
        print("解压 ...")
        with zipfile.ZipFile(src_zip) as z:
            z.extractall(tmp)
        src_root = os.path.join(tmp, "cs2-link-manager-main")
        if not os.path.isdir(src_root):
            raise SystemExit("未找到源码根目录 cs2-link-manager-main/")

        if os.path.exists(OUT_ZIP):
            os.remove(OUT_ZIP)
        with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
            _add_file(z, os.path.join(HERE, "cs2lm"), "cs2lm", 0o755)
            _add_file(z, os.path.join(HERE, "cs2lm.bat"), "cs2lm.bat", 0o755)
            _add_file(z, os.path.join(HERE, "README.md"), "README.md", 0o644)
            for item in ("src", "pyproject.toml", "README.md", "CHANGELOG.md"):
                fp = os.path.join(src_root, item)
                if not os.path.exists(fp):
                    continue
                if os.path.isdir(fp):
                    for dp, _, fs in os.walk(fp):
                        for fn in fs:
                            full = os.path.join(dp, fn)
                            rel = os.path.relpath(full, src_root)
                            z.write(full, os.path.join("tools", "cs2lm", rel))
                else:
                    z.write(fp, os.path.join("tools", "cs2lm", item))
        print("已生成: %s (%.1f MB)" % (OUT_ZIP, os.path.getsize(OUT_ZIP) / 1024 / 1024))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()