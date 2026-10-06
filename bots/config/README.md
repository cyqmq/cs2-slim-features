# bots 功能包

人机（Bots）选配功能。

## 文件

- `server_bot.cfg` — 服务端人机玩法配置
  - 部署到 `game/csgo/cfg/server_bot.cfg`
  - 在 `server.cfg` 末尾 `exec server_bot`，或启动参数加 `+exec server_bot`
- `offline_practice.cfg` — 客户端离线练习配置
  - 部署到 `game/csgo/cfg/offline_practice.cfg`
  - 本地开图：`-insecure +map de_dust2 +exec offline_practice`

## 说明

- CS2 的 bots 是引擎内置功能，无需额外 depot 文件。
- 地图 VPK 自包含导航网格（nav），因此任意已添加的地图都支持 bots。
- 服务端人机玩法建议配合 `bot_quota_mode fill`（按真人玩家数补齐机器人）。