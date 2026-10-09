# ModSharp C# 插件框架 Linux 版（CS2 精简服务端功能包）

为 **Linux** 版 CS2 精简服务端安装 **ModSharp**（git-187）。ModSharp 是一个现代化的 C# 插件框架，已服务超 400 万玩家，支持模块化插件开发。

## 特点

- **独立框架，不依赖 Metamod**（通过 `gameinfo.gi` 的 `Game sharp` 搜索路径加载）
- 安装目录：`game/sharp/`
- 控制台验证命令：`ms`
- **注意：包内不自带 .NET 运行时**，需服务端预装 **.NET 10**（Linux）。

## 环境要求

- .NET 10 Runtime：<https://dotnet.microsoft.com/download/dotnet/10.0>

## 安装

### prebuilt 模式（自动拼装）

```bash
export CS2_MODE=prebuilt CS2_FEATURES=modsharp
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

拼装时自动完成：

1. 解压本包到精简树（`game/sharp/` 结构）
2. 自动在 `game/csgo/gameinfo.gi` 的 `Game_LowViolence` 下方添加 `Game sharp`

### 手动安装

```bash
curl -fsSL -o modsharp-pack.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/modsharp-pack.zip
unzip -o modsharp-pack.zip -d <精简树>
# 然后手动在 game/csgo/gameinfo.gi 的 Game_LowViolence 下方添加：
#   Game sharp
```

## 验证

启动服务端后，在控制台输入 `ms`，能看到 ModSharp 的状态输出即安装成功。

## 开发插件

使用 .NET 10 SDK 创建 ModSharp 插件模块，编译后放入 `game/sharp/modules/` 目录。模板与文档见：

- 官方文档：<https://docs.modsharp.net/>
- 快速开始：<https://docs.modsharp.net/docs/zh-cn/guides/getting-started.html>

## 说明

- 当前 `link-manager`（cs2lm）暂不支持管理 ModSharp 插件。
- 官方仓库：<https://github.com/Kxnrl/modsharp-public>