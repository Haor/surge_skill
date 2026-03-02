---
Title: Surge 配置校验 API（Beta）
Source: https://services.nssurge.com/v1/config/validate
Crawl Date: 2026-03-02
Description: >
  Official Surge beta API for validating whether a profile is syntactically valid.
  Supports posting raw profile text or JSON payload with `profile` field.
  Returns JSON with `valid` and optional `error` fields.
---

# Surge 配置校验 API（Beta）

## Endpoint

- `POST https://services.nssurge.com/v1/config/validate`

## 用途

用于检查 Surge 配置是否合法。

## 请求方式

可使用以下两种方式提交配置内容：

1. **直接 POST 整个配置文件文本**
2. 当 `Content-Type: application/json` 时，使用 JSON 字段 `profile` 传入配置内容

## 请求示例

### 方式 1：直接提交配置文本

```bash
curl -X POST "https://services.nssurge.com/v1/config/validate" \
  --data-binary @surge.conf
```

### 方式 2：JSON 提交

```bash
curl -X POST "https://services.nssurge.com/v1/config/validate" \
  -H "Content-Type: application/json" \
  -d '{"profile":"[General]\nloglevel = notify\n\n[Rule]\nFINAL,DIRECT"}'
```

## 响应格式

返回 JSON：

- `valid`：布尔值，表示配置是否合法
- `error`：当 `valid` 为 `false` 时返回错误信息（实测为对象，包含 `message` 字段）

### 示例：合法配置

```json
{
  "valid": true
}
```

### 示例：不合法配置

```json
{
  "valid": false,
  "error": {
    "message": "Invalid line ..."
  }
}
```

## 隐私与安全说明（官方）

- 该 API 不配置日志系统
- 上传内容不会被保存

如果仍担心隐私，可在校验前对配置中的敏感字段先做脱敏替换（如服务器地址、用户名、密码等），再提交校验。

## 使用建议

- 语法检查通过（`valid=true`）不代表策略逻辑一定符合预期，仍应结合 `docs/manual/overview/configuration.md` 与相关章节进行人工检查。
- 对大型配置文件，建议在本地预处理后再提交，避免把不必要的敏感段落发往网络接口。
