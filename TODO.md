# TODO

## Goal
将 `docs/posts/` 83篇扁平文档按 7 大类物理重组为 `docs/{linux,embedded,git,network,tools,programming,windows,cheatsheet}` 子目录，统一 FrontMatter 与 `mkdocs.yml` 导航，归档 WIP 并可 `mkdocs build` 验证。

## Tasks

### 1. 结构设计与清单定版
- [x] 生成 `docs/<新分类>/` 完整文件映射表 `MAPPING.md`（83+6 篇 → 8 目录），供复核
- [x] 确定每篇目标路径、归一化后的 `categories` / `tags`（小写、去重、去除 `WIP` tag、统一 `categories:`）
- [x] 确定 `WIP/6篇` 归档目标（`buildroot 静态ip→embedded/buildroot`、`DWM→cheatsheet`、`gitea→git`、`chrome secure dns→windows`、`gpio keypad→embedded/hardware`、`安装FreeBSD并搭建clash→network`）

### 2. 物理重组（git mv）
- [x] 创建目标目录：`docs/linux`、`docs/embedded`、`docs/git`、`docs/network`、`docs/tools/{apt,ssh,samba}`、`docs/programming/{c-cpp,python,shell}`、`docs/windows`、`docs/cheatsheet`
- [x] 用 `git mv` 批量移动 83 篇 `docs/posts/*.md` 到新位置（保留历史），并移动 6 篇 `WIP/*.md`
- [x] 删除空目录 `docs/posts/`、`WIP/`，更新 `.gitignore` / 校验无孤儿文件

### 3. FrontMatter 统一
- [x] 编写并执行脚本 `scripts/normalize_frontmatter.py`：统一为 `categories:` + `tags:`，小写化（`Shell→shell`），去重，修复 `category/www` → 正确分类，移除 `abbrlink` 残留，`WIP` 移为 `draft: true` 可选
- [x] 抽验 10 篇（每类至少1篇）frontmatter 正确，`categories` 与所在目录一致
- [x] 统一 `template/Front-matter.md` 为新范式

### 4. MkDocs 配置与导航
- [x] 重写 `mkdocs.yml`：`nav` 按 7 大类 `navigation.sections` 组织，含 `index.md` 索引；修正 `plugins.blog.blog_dir` 为 `blog`（不再指向 `.`），保留 `tags_file: blog/tags.md`（已去 deprecated 警告，改用 `tags:` 无参）
- [x] 为每个顶层/子目录创建 `index.md` 分类索引页（含 `dataview` 替代的 tag 列表或手写目录）
- [x] 更新 `docs/index.md` 首页为分类导航入口，`docs/blog/tags.md` 保留并静态化

### 5. 归档与兼容
- [x] 处理 `分类.md` / `home.md`（Obsidian dataview）在 MkDocs 下的替代：转为 `docs/*/index.md` 或移入 `docs/blog/`，避免构建警告 — 已更新 `分类.md` 为 7 类新路径、`home.md` 中 `from "docs/posts"` → `from "docs"`
- [x] 检查内链/图片引用（`assets/BingWallpaper-517.jpg`）是否失效，修复相对路径 — `docs/index.md` 指向 `assets/BingWallpaper-517.jpg` 正常，`blog/tags.md` 链接已修正为 `index.md`
- [x] 删除或重定向旧 `docs/posts` 引用（若有）— 仅 `MAPPING.md`/`TODO.md` 保留历史记录，`docs/` 与 `mkdocs.yml` 无残留

### 6. 验证
- [x] `mkdocs build --strict` / `mkdocs serve` 无 ERROR/WARN（缺失 nav、broken links）— `mkdocs build` / `--strict` 均通过（仅 Material 2.0 banner 非 content warning）
- [x] `grep -r "docs/posts" --include="*.md" --include="*.yml"` 无残留 — `docs/` 与 `mkdocs.yml` 已清零，根目录 `分类.md`/`home.md` 已更新
- [x] `git status` 仅显示预期 mv/modify，无未跟踪文件；抽查 `git log --follow -- <新路径>` 历史可追溯 — 已验证 `git mv` 保留历史

## Notes
- 约束：全部用 `git mv` 保留历史；`mkdocs-material` 版本以 `requirements.txt` 为准；执行前创建 `backup/pre-reorg` 分支
- 决策：1-A 物理移动，2-接受7类（落地为8物理目录，nav合并Windows&速查表为1节），3-统一 FrontMatter，4-A WIP归档，5-A 以 sections 为主导航
- 风险：文件名含空格/中文，需脚本正确处理；`v2ray 脚本安装.md` 含 `abbrlink` 需清理；`OpenWrt 使用记录.md` 含 `WIP` tag 需移除
