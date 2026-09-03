# Changelog

本文件记录 `farfarfun` 的版本变更，按版本倒序排列，分为 新增 / 修复 / 变更 / 废弃 四类。

## [0.1.19] - 2026-09

### 变更

- 源码目录迁移到标准 `src/farfarfun/` 布局，`pyproject.toml` 同步更新打包配置。
- README 重写：补充安装命令与最小可运行示例，明确本仓库同时是组织 profile 页与 PyPI 占位包；移除与规范冲突的"组织未统一许可"表述，明确声明 MIT；移除遗留的 AI 会话式占位内容；末尾追加组织介绍固定区块。
- `.gitignore` 补充 `*.rar`、`.run/`、`logs/`、`.idea/`、`.vscode/`。

### 新增

- 提交 `uv.lock`，保证可复现构建。
- 新增本 CHANGELOG.md。
