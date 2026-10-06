# CounterStrikeSharp 插件框架 Linux 版（CS2 精简服务端功能包）

为 **Linux** 版 CS2 精简服务端安装 **CounterStrikeSharp**（CSS，v1.0.376，linuxsteamrt64，带 .NET 运行时）。CSS 是 CS2 服务端最常用的 C# 插件框架，运行在 **Metamod:Source** 之上。

## 依赖

- 必须先安装 **metamod**（Metamod:Source Linux 版）。一键安装时用 `CS2_FEATURES=metamod,css` 会自动先装 metamod 再装 css。

## 安装

### prebuilt 模式（自动拼装）

```bash
export CS2_MODE=prebuilt CS2_FEATURES=metamod,css
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

拼装时自动完成：

1. 安装依赖 `metamod`（Metamod 框架，自动补 `gameinfo.gi`）
2. 解压本包到精简树（`game/csgo/addons/` 结构，含 `counterstrikesharp.vdf` 插件注册文件）

### 手动安装

```bash
# 先装 metamod，再装 css
curl -fsSL -o css-pack.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/css-pack.zip
unzip -o css-pack.zip -d <精简树>
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

- 仅支持 Linux（linuxsteamrt64）；Windows 服务端请使用 `css-win` 功能。
- 本包使用 **with-runtime** 版本，内置 .NET 运行时，无需宿主机预装 .NET。
- 如果启动日志出现 `Could not PreloadLibrary ... Access violation`，是非致命警告，不影响 CSS 运行。

## 重新构建

本目录不提交二进制（解压约 100+MB），运行 `build_pack.py` 会从 CounterStrikeSharp Release 下载并重打包：

```bash
python css/build_pack.py
```