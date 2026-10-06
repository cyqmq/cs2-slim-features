# cs2-slim-features

CS2 Slim 服务端的**功能组件仓库**（选配组件）。

配合主仓库 [cs2-slim-replica](https://github.com/cyqmq/cs2-slim-replica) 使用，按需为精简服务端添加功能。

## 功能列表

| 功能 | 目录 | 说明 |
|------|------|------|
| 人机 (bots) | `bots/` | 服务端 `bot_add` 人机玩法 + 客户端离线练习配置 |

## 使用方法

### 配置驱动

在 `slim.yaml` 添加：

```yaml
features:
  - bots
```

```bash
python cs2slim.py download --config slim.yaml
python cs2slim.py extract  --config slim.yaml
python cs2slim.py build    --config slim.yaml
```

### 命令行参数

```bash
python cs2slim.py download --platform linux --maps de_dust2 --features bots
```

### 部署配置

构建完成后，把 `bots/config/` 下的 cfg 文件复制到服务端：

```bash
cp bots/config/server_bot.cfg        <精简树>/game/csgo/cfg/server_bot.cfg
cp bots/config/offline_practice.cfg  <精简树>/game/csgo/cfg/offline_practice.cfg
```

然后在 `server.cfg` 末尾加 `exec server_bot`，重启服务端即可。

## 组件格式

每个功能组件包含：

- `filelist.txt` — 追加到核心下载清单的片段（纯配置类功能通常为空）
- `metadata.json` — 元数据（说明、配置路径、更新时间）
- `config/` — 配置文件模板

```json
{
  "name": "bots",
  "description": "人机功能包",
  "filelist": [],
  "config": {
    "server_bot": "config/server_bot.cfg",
    "offline_practice": "config/offline_practice.cfg"
  },
  "updated": "2026-10-06"
}
```

## 更新流程

CS2 更新后，检查配置是否仍适用，更新 `metadata.json` 的 `updated` 字段即可。