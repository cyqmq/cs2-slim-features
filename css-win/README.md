# CounterStrikeSharp 插件框架 Windows 版（CS2 精简服务端功能包）

为 **Windows** 版 CS2 精简服务端安装 **CounterStrikeSharp**（CSS，v1.0.376，win64，带 .NET 运行时）。CSS 是 CS2 服务端最常用的 C# 插件框架，运行在 **Metamod:Source** 之上。

## 依赖

- 必须先安装 **metamod-win**（Metamod:Source Windows 版）。一键安装时用 `CS2_FEATURES=metamod-win,css-win` 会自动先装 metamod 再装 css。

## 安装

### prebuilt 模式（自动拼装）

```powershell
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "metamod-win,css-win"
irm https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.ps1 | iex
```

拼装时自动完成：

1. 安装 metamod-win（Metamod 框架）
2. 解压本包到精简树（`game/csgo/addons/` 结构，含 `counterstrikesharp.vdf` 插件注册文件）
3. 自动在 `game/csgo/gameinfo.gi` 的 SearchPaths 中加入 `Game csgo/addons/metamod`

### 手动安装

```powershell
# 先装 metamod-win，再装 css-win
curl.exe -fL -o css-pack-win.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/css-pack-win.zip
Expand-Archive css-pack-win.zip -DestinationPath <精简树> -Force
```

## 验证

启动服务端后，在控制台输入 `meta list`，应看到：

```
  [01] CounterStrikeSharp (v1.0.376 @ 653d651) by Roflmuffin
```

输入 `css_plugins list` 查看已加载的用户插件（默认 0 个）。将你的 CSS 插件 dll 放到 `game/csgo/addons/counterstrikesharp/plugins/` 后重启即可加载。

## 包内结构

```text
game/csgo/addons/counterstrikesharp/     # CSS 框架（api/ bin/ configs/ dotnet/ gamedata/ lang/ plugins/）
game/csgo/addons/metamod/counterstrikesharp.vdf   # Metamod 插件注册文件
README.md
```

## 注意

- 仅支持 Windows（win64）；Linux 服务端请等待 `css`（Linux 版）功能。
- 本包使用 **with-runtime** 版本，内置 .NET 运行时，无需宿主机预装 .NET。
- 如果启动日志出现 `Could not PreloadLibrary ... Access violation`，是非致命警告，不影响 CSS 运行。

## 重新构建

本目录不提交二进制（114MB），运行 `build_pack.py` 会从 CounterStrikeSharp Release 下载并重打包：

```bash
python css-win/build_pack.py
```