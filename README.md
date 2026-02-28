# surge-claude-skill

一个 [Claude Code Skill](https://docs.anthropic.com/en/docs/claude-code/skills)，让 Claude 直接查阅 [Surge](https://nssurge.com/) 官方文档来回答配置问题，而非依赖训练数据中可能过时的信息。

## 工作原理

```
用户: /surge DOMAIN-SUFFIX 规则怎么写？
                │
                ▼
    ┌───────────────────────┐
    │  SKILL.md frontmatter │  ~80 tokens，始终在上下文中
    │  (name + description) │  匹配 Surge 相关查询时触发
    └───────────┬───────────┘
                │ 匹配
                ▼
    ┌───────────────────────┐
    │  SKILL.md body        │  ~2,000 tokens，触发时加载
    │  (路由表)              │  话题 → 文件路径
    └───────────┬───────────┘
                │ 路由到 docs/manual/rule/domain-based.md
                ▼
    ┌───────────────────────┐
    │  Read tool            │  ~1,500 tokens，按需加载
    │  (1–3 个文档文件)      │  只读取需要的内容
    └───────────────────────┘
```

典型查询消耗约 3,500 tokens。全量加载约 45,000 tokens — 节省 >90%。

## 文档来源

### 官方文档

| 目录 | 来源 | 获取方式 | 语言 | 文件数 |
|------|------|---------|------|--------|
| `docs/manual/` | [manual.nssurge.com](https://manual.nssurge.com) | Jina Reader → Markdown，清洗后存储 | EN | 58 |
| `docs/kb/en/` | [kb.nssurge.com](https://kb.nssurge.com) | GitBook 原始 Markdown | EN | 31 |
| `docs/kb/zh/` | [kb.nssurge.com](https://kb.nssurge.com) | GitBook 原始 Markdown | ZH | 32 |

**共计 121 个官方文档文件，约 14,600 行。**

### 社区内容

| 目录 | 来源 | 作者 | 最后更新 | 文件数 |
|------|------|------|---------|--------|
| `docs/community/skk-surge-tips.md` | [Sukka's Blog](https://blog.skk.moe/post/i-have-my-unique-surge-setup/) | Sukka (SKK) | 2026-01-02 | 1 |
| `docs/community/zhuangzhuang/` | [壮壮配置详解](https://zhuangzhuang.io/2018/11/14/surge.html) | 壮壮 | 2025-08-20 | 5 |
| `docs/community/policy-icons.md` | [Telegraph](https://telegra.ph/策略图标订阅-合集-03-12-2) | 社区 | — | 1 |

社区内容按话题拆分以便按需加载。壮壮指南分为：general、proxy-and-group、rule、rewrite-and-mitm、script-and-module。

> **注意**：社区教程可能已过时，请始终以 `docs/manual/` 官方文档为准。SKK 博客采用 CC BY-NC-SA 4.0 许可。

### 内容时效性

**官方文档初次爬取日期：2025-02-27。**

文档为特定时间点的快照。Surge 持续开发中，新功能、配置项和 bug 修复可能未反映在此。更新方式：

```bash
# 重新爬取 manual（通过 Jina Reader）并清洗
python3 scripts/crawl_surge_docs.py
python3 scripts/clean_surge_docs.py

# 重新爬取知识库（直接获取 GitBook .md）
python3 scripts/crawl_surge_kb.py
```

> **注意**：脚本默认跳过已有文件。如需强制重新下载，先删除对应目录再运行。

重新爬取后，若 Surge 新增了文档页面，可能需要同步更新 `SKILL.md` 中的路由表。

## 仓库结构

本仓库**本身就是** skill。将整个仓库 clone 或 symlink 到项目的 `.claude/skills/surge/` 即可安装。

```
surge-claude-skill/              ← 本仓库
├── SKILL.md                     ← Skill 定义（路由表 + 使用指令）
├── docs/
│   ├── manual/                  ← 配置参考手册（EN，58 个文件）
│   ├── kb/
│   │   ├── en/                  ← 知识库（EN，31 个文件）
│   │   └── zh/                  ← 知识库（ZH，32 个文件）
│   └── community/               ← 社区教程
│       ├── skk-surge-tips.md    ← SKK 进阶技巧（CC BY-NC-SA 4.0）
│       ├── zhuangzhuang/        ← 壮壮配置详解（按话题分 5 个文件）
│       └── policy-icons.md      ← 策略组图标订阅合集
├── scripts/
│   ├── crawl_surge_docs.py      ← 通过 Jina Reader 爬取 manual
│   ├── crawl_surge_kb.py        ← 爬取知识库
│   └── clean_surge_docs.py      ← 清洗 Jina Reader 产物
├── .gitignore
└── README.md
```

## 安装

将本仓库 clone 到项目的 `.claude/skills/` 目录：

```bash
# 方式一：Git clone（便于拉取更新）
git clone <this-repo-url> your-project/.claude/skills/surge

# 方式二：Symlink（如已 clone 到其它位置）
ln -s /path/to/surge-claude-skill your-project/.claude/skills/surge

# 方式三：直接复制
cp -r /path/to/surge-claude-skill your-project/.claude/skills/surge
```

安装后，在该项目的 Claude Code 会话中即可使用。

### 查询示例

```
/surge DOMAIN-SUFFIX 规则怎么写？
/surge WireGuard 代理怎么配置？
/surge enhanced mode 是什么？
/surge 网关模式性能问题
/surge scripting HTTP request 脚本怎么写？
/surge 购买前常见问题
```

## 话题覆盖

Skill 通过路由表覆盖 13 个话题组：

| 分组 | 话题 |
|------|------|
| 入门概览 | 组件架构、配置文件格式、理解 Surge |
| 规则 | Domain、IP、HTTP、进程、子网、逻辑规则、杂项、规则集、FINAL |
| 策略 | DIRECT、REJECT、代理协议、SSH、WireGuard、外部代理、参数 |
| 策略组 | select、url-test、fallback、load-balance、subnet、嵌套引用 |
| DNS | DNS 覆写、DoH/DoQ、本地 DNS 映射 |
| HTTP 处理 | URL/Header/Body 重写、MITM、Mock |
| 脚本 | 通用 API、HTTP 请求/响应、定时、DNS、事件、规则脚本 |
| 其它功能 | 增强模式、HTTP API、模块、面板、CLI、托管配置等 |
| KB 指南 | 网关模式、故障排除、Ponte、智能策略组、tvOS、代理提供者 |
| KB 技术笔记 | DNS、HTTP 版本、TFO、NAT 类型、IPv6 RA、UDP fast path 等 |
| KB 常见问题 & 授权 | FAQ、TestFlight、购买前问题、iOS/Mac 授权 |
| KB 更新日志 | Surge iOS、Surge Mac 6、旧版 Mac、Snell |
| 社区 | SKK 进阶技巧、壮壮配置详解（5 部分）、策略图标 |

## 许可

`docs/` 中的文档内容来源于 Surge 官方站点，受 [Surge 条款](https://nssurge.com/) 约束。本仓库中的 Skill 定义和爬取脚本仅供个人使用。
