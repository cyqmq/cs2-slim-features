# Plugify 插件框架 Linux 版（CS2 精简服务端功能包）

为 **Linux** 版 CS2 精简服务端安装 **Plugify** Metamod 加载器（v2.1.4，linuxsteamrt64）。Plugify 是一个多语言插件系统，支持 C++、C#、Python、Lua、JS 等语言模块，本包是让 Plugify 运行在 Metamod 之上的**加载器**。

## 依赖

- 必须先安装 **metamod**（Metamod:Source Linux 版）。一键安装时用 `CS2_FEATURES=metamod,plugify` 会自动先装 metamod 再装 plugify。

## 包内容

安装后包含：

- `game/csgo/addons/plugify/bin/linuxsteamrt64/libplugify.so`（Plugify 加载器）
- `game/csgo/addons/plugify/bin/linuxsteamrt64/micromamba`（Plugify 包管理器）
- `game/csgo/addons/metamod/plugify.vdf`（Metamod 插件注册文件）

> 本包是**最小加载器**，不包含语言模块。要运行插件，需要先通过 Plugify 包管理器安装对应语言模块（如 C#、Python）与 s2sdk 插件，详见 <https://plugify.net/use-cases/metamod-plugin/installation/>。

## 安装

### prebuilt 模式（自动拼装）

```bash
export CS2_MODE=prebuilt CS2_FEATURES=metamod,plugify
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

拼装时自动完成：

1. 安装依赖 `metamod`（Metamod 框架，自动补 `gameinfo.gi`）
2. 解压本包到精简树（`game/csgo/addons/plugify/` + `game/csgo/addons/metamod/plugify.vdf`）

### 手动安装

```bash
# 先装 metamod，再装 plugify
curl -fsSL -o plugify-pack.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/plugify-pack.zip
unzip -o plugify-pack.zip -d <精简树>
```

## 验证

启动服务端后，在控制台输入 `meta list`，应看到 Plugify 已加载。

## 后续：安装语言模块

在服务器 `game/csgo` 目录下使用 Plugify 包管理器安装模块（示例）：

```bash
# 在 game/csgo 目录执行（路径以实际安装为准）
./addons/plugify/bin/linuxsteamrt64/micromamba run plugify package add plugify-csharp
./addons/plugify/bin/linuxsteamrt64/micromamba run plugify package add plugify-s2sdk
```

具体模块名与命令以官方文档为准。

## 说明

- 当前 `link-manager`（cs2lm）暂不支持管理 Plugify 插件。
- 官方仓库：<https://github.com/untrustedmodders/plugify-metamod-loader>