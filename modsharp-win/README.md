# ModSharp C# 插件框架 Windows 版（CS2 精简服务端功能包）

为 **Windows** 版 CS2 精简服务端安装 **ModSharp**（git-187）。ModSharp 是一个现代化的 C# 插件框架，已服务超 400 万玩家，支持模块化插件开发。

## 特点

- **独立框架，不依赖 Metamod**（通过 `gameinfo.gi` 的 `Game sharp` 搜索路径加载）
- 安装目录：`game/sharp/`
- 控制台验证命令：`ms`
- **注意：包内不自带 .NET 运行时**，需服务端预装 **.NET 10** 与 **Visual C++ Redistributable**（Windows）。

## 环境要求

- .NET 10 Runtime：<https://dotnet.microsoft.com/download/dotnet/10.0>
- Visual C++ Redistributable：<https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist>

## 安装

### prebuilt 模式（自动拼装）

```powershell
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "modsharp-win"
# 使用 get-cs2slim.bat 或对应 Windows 拼装流程
```

拼装时自动完成：

1. 解压本包到精简树（`game/sharp/` 结构）
2. 自动在 `game/csgo/gameinfo.gi` 的 `Game_LowViolence` 下方添加 `Game sharp`

### 手动安装

```powershell
curl.exe -fsSL -o modsharp-pack-win.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/modsharp-pack-win.zip
Expand-Archive -Path modsharp-pack-win.zip -DestinationPath <精简树> -Force
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