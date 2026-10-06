# Metamod:Source 插件框架（CS2 精简服务端功能包）

为 CS2 精简服务端安装 **Metamod:Source**（2.0.0-git1473，linuxsteamrt64），这是 CS2 服务端插件的基础加载框架（CounterStrikeSharp 等插件都依赖它）。

## 安装

### prebuilt 模式（自动拼装）

```bash
export CS2_MODE=prebuilt CS2_FEATURES=metamod
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

拼装时自动完成：

1. 解压本包到精简树（`game/csgo/addons/` 结构）
2. 自动在 `game/csgo/gameinfo.gi` 的 SearchPaths 中加入 `Game csgo/addons/metamod`

### 手动安装

```bash
curl -fsSL -o metamod-pack.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/metamod-pack.zip
unzip -o metamod-pack.zip -d <精简树>
```

然后手动编辑 `game/csgo/gameinfo.gi`，在 `Game_LowViolence csgo_lv` 下一行加入：

```text
Game	csgo/addons/metamod
```

## 验证

启动服务端后，在控制台输入 `meta version` / `meta list`：

```
] meta version
Metamod:Source Version Information
...
```

如果显示 `Unknown command`，说明 gameinfo.gi 补丁未生效，检查 `Game csgo/addons/metamod` 是否存在。

## 包内结构

```text
game/csgo/addons/metamod.vdf
game/csgo/addons/metamod_x64.vdf
game/csgo/addons/metamod/README.txt
game/csgo/addons/metamod/metaplugins.ini
game/csgo/addons/metamod/bin/linuxsteamrt64/libserver.so
game/csgo/addons/metamod/bin/linuxsteamrt64/metamod.2.cs2.so
```

## 注意

- 仅支持 Linux（linuxsteamrt64）；Windows 服务端请使用 Metamod 的 win64 包。
- CS2 游戏更新后 `gameinfo.gi` 可能被重置，需要重新执行一次拼装（或手动补行）。
- 安装 Metamod 后，`game/csgo/addons/metamod/metaplugins.ini` 是插件清单文件。