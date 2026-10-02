# Changelog

本文件记录 `farfarfun` 的版本变更，按版本倒序排列，分为 新增 / 修复 / 变更 / 废弃 四类。

## [0.1.20] - 2026-10

### 变更

- `pyproject.toml` 的 `description` 改为据实描述：本仓库是组织 profile 仓库，同时发布同名 PyPI 占位包以保留组织包名。此前为与包名重复的 `farfarfun`，PyPI summary 也随之无意义。
- 补全 ruff 配置：显式声明 `src`、启用 `E/F/I/UP/B/RUF` 规则集；新增 pytest `testpaths` 与 `pythonpath = ["src"]`，确保测试导入工作区代码而非全局已安装版本。

### 新增

- 无。

### 修复

- 无。

### 废弃

- 无。

## [0.1.19] - 2026-09

### 变更

- 源码目录迁移到标准 `src/farfarfun/` 布局，`pyproject.toml` 同步更新打包配置。
- README 重写：补充安装命令与最小可运行示例，明确本仓库同时是组织 profile 页与 PyPI 占位包；移除与规范冲突的"组织未统一许可"表述，明确声明 MIT；移除遗留的 AI 会话式占位内容；末尾追加组织介绍固定区块。
- `.gitignore` 补充 `*.rar`、`.run/`、`logs/`、`.idea/`、`.vscode/`。

### 新增

- 提交 `uv.lock`，保证可复现构建。
- 新增本 CHANGELOG.md。

### 修复

- 无。

### 废弃

- 无。
