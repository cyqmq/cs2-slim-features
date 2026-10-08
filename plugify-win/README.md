# Plugify 插件框架 Windows 版（CS2 精简服务端功能包）

为 **Windows** 版 CS2 精简服务端安装 **Plugify** Metamod 加载器（v2.1.4，win64）。Plugify 是一个多语言插件系统，支持 C++、C#、Python、Lua、JS 等语言模块，本包是让 Plugify 运行在 Metamod 之上的**加载器**。

## 依赖

- 必须先安装 **metamod-win**（Metamod:Source Windows 版）。一键安装时用 `CS2_FEATURES=metamod-win,plugify-win` 会自动先装 metamod-win 再装 plugify-win。

## 包内容

安装后包含：

- `game/csgo/addons/plugify/bin/win64/plugify`（Plugify 加载器）
- `game/csgo/addons/plugify/bin/win64/micromamba`（Plugify 包管理器）
- `game/csgo/addons/metamod/plugify.vdf`（Metamod 插件注册文件）

> 本包是**最小加载器**，不包含语言模块。要运行插件，需要先通过 Plugify 包管理器安装对应语言模块（如 C#、Python）与 s2sdk 插件，详见 <https://plugify.net/use-cases/metamod-plugin/installation/>。

## 安装

### prebuilt 模式（自动拼装）

```powershell
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "metamod-win,plugify-win"
# 使用 get-cs2slim.bat 或对应 Windows 拼装流程
```

拼装时自动完成：

1. 安装依赖 `metamod-win`（Metamod 框架，自动补 `gameinfo.gi`）
2. 解压本包到精简树（`game/csgo/addons/plugify/` + `game/csgo/addons/metamod/plugify.vdf`）

### 手动安装

```powershell
# 先装 metamod-win，再装 plugify-win
curl.exe -fsSL -o plugify-pack-win.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/plugify-pack-win.zip
Expand-Archive -Path plugify-pack-win.zip -DestinationPath <精简树> -Force
```

## 验证

启动服务端后，在控制台输入 `meta list`，应看到 Plugify 已加载。

## 后续：安装语言模块

在服务器 `game/csgo` 目录下使用 Plugify 包管理器安装模块（示例）：

```powershell
cd <精简树>\game\csgo
.\addons\plugify\bin\win64\micromamba run plugify package add plugify-csharp
.\addons\plugify\bin\win64\micromamba run plugify package add plugify-s2sdk
```

具体模块名与命令以官方文档为准。

## 说明

- 当前 `link-manager`（cs2lm）暂不支持管理 Plugify 插件。
- 官方仓库：<https://github.com/untrustedmodders/plugify-metamod-loader>