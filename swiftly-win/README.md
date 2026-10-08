# SwiftlyS2 插件框架 Windows 版（CS2 精简服务端功能包）

为 **Windows** 版 CS2 精简服务端安装 **SwiftlyS2**（v1.4.13，win64，**带 .NET 运行时**）。SwiftlyS2 是一个基于 C++、支持 C# 插件的 CS2 脚本框架。

## 特点

- **独立框架，不依赖 Metamod**（与 CounterStrikeSharp 不同）
- 自带 .NET 运行时（with-runtimes 包）
- 插件目录：`game/csgo/addons/swiftlys2/plugins/`
- 控制台验证命令：`sw`

## 安装

### prebuilt 模式（自动拼装）

```powershell
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "swiftly-win"
# 使用 get-cs2slim.bat 或对应 Windows 拼装流程
```

拼装时自动完成：

1. 解压本包到精简树（`game/csgo/addons/swiftlys2/` 结构）
2. 自动在 `game/csgo/gameinfo.gi` 的 `Game_LowViolence` 下方添加 `Game csgo/addons/swiftlys2`

### 手动安装

```powershell
curl.exe -fsSL -o swiftly-pack-win.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/swiftly-pack-win.zip
Expand-Archive -Path swiftly-pack-win.zip -DestinationPath <精简树> -Force
# 然后手动在 game/csgo/gameinfo.gi 的 Game_LowViolence 下方添加：
#   Game csgo/addons/swiftlys2
```

## 验证

启动服务端后，在控制台输入 `sw`，能看到 SwiftlyS2 的版本/状态输出即安装成功。

## 开发插件

插件模板（需 .NET 10 SDK）：

```bash
dotnet new install SwiftlyS2.CS2.PluginTemplate
dotnet new swplugin -n MyPlugin --PluginName "My Plugin" --PluginVersion "1.0.0" --PluginAuthor "Author" --PluginDescription "My first SwiftlyS2 plugin"
dotnet publish
```

将 `build/publish/<PluginId>/` 复制到 `game/csgo/addons/swiftlys2/plugins/<PluginId>/`，重启服务端即可加载。

## 说明

- 当前 `link-manager`（cs2lm）暂不支持管理 SwiftlyS2 插件，仅支持 Metamod/CounterStrikeSharp。
- 官方文档：<https://swiftlys2.net/docs/installation>