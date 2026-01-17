# Week 2 — Python 与工具实践 🐍🔧

## 概述
本周聚焦 Python 基础与实用工具开发，目标是培养处理生物信息学大文件的能力，掌握编写健壮、可复用命令行工具（CLI）的方法，并熟悉 Git 协作流程。

---

## 学习目标 ✅
- 理解 Python 常用数据结构（List, Dict）及其内存模型。  
- 熟练使用文件句柄 (`with open`)、异常处理 (`try/except`)。  
- 能用生成器/迭代器高效处理超大文件（避免内存溢出）。  
- 能使用 `sys`、`os`、`subprocess` 编写系统交互脚本。  
- 掌握使用 `argparse` 构建标准 CLI，并保证程序的健壮性（使用 `re`、合理的异常处理）。  
- 熟悉 Git 的基本操作与分支协作工作流（Pull Request 流程）。

## 前置知识
- 建议具备基本的 Linux 命令行使用经验与 Python 基础语法。

---

## 理论要点 📚
- Python 数据结构对内存和性能的影响（List vs Dict）。
- 文件 I/O 与上下文管理器 (`with open`) 的最佳实践。
- 异常捕获与错误处理策略（不要滥用裸 `except`）。
- 生成器与迭代器用于大文件流式处理。

---

## 工具与实践 🛠️
- I/O：Generator / Iterator，逐行处理大文件。  
- 系统交互：`sys`, `os`, `subprocess`。  
- CLI：`argparse`（参数校验、帮助信息、子命令等）。  
- 健壮性：`re`（数据校验）、`logging`（替代 `print`）、完善的异常处理。  
- 版本控制：Git（clone/pull/add/commit/push）、分支管理（branch/checkout/merge）、PR 流程。

---

## 练习任务 🧪

### 练习 1 — 算法逻辑：GC 计算
- 目标：实现 `gc_content(seq: str) -> float`，返回序列的 GC 含量（0-100% 或 0-1，可说明）。
- 要求：
  - 禁止使用 Biopython。  
  - 必须包含 `try/except` 来处理含有非 ATCG 字符的异常或忽略非法字符并记录警告。  
  - 拓展思考：如何改为统计所有长度为 k 的 k-mer 频率？给出时间/空间复杂度的简要分析和实现思路。

示例接口建议：
```python
def gc_content(seq: str, ignore_non_atcg: bool = True) -> float:
    """返回 GC 含量（百分比）。当出现非法字符时：
    - 如果 ignore_non_atcg 为 True，则忽略并记录警告；
    - 否则抛出 ValueError。
    """
```

---

### 练习 2 — I/O 流解析：FASTA 处理与过滤工具
- 目标：编写一个 CLI 工具，支持从 FASTA 文件或 `stdin` 读取，输出单行序列并统计长度分布。
- 功能要求：
  - 支持将多行 FASTA 转为单行 (one-record-per-line) 输出。  
  - 支持通过 `--min` / `--max` / `--gcmin` / `--gcmax` 过滤序列（长度与GC范围）。  
  - 输出选项：`--stdout`（打印到屏幕）、`--out <file>`（写入文件）。  
  - 日志与进度信息应写入 `stderr`（使用 `logging`），并在发生错误时优雅退出。  
  - 支持通过管道使用（读取 `sys.stdin`）。

示例：
```bash
# 从文件处理并写结果到 out.tsv
python fasta_tool.py --in sequences.fasta --out results.tsv --min 100 --gcmin 40

# 支持管道
cat sequences.fasta | python fasta_tool.py --stdin --gcmax 60 --stdout
```

---

### 练习 3 — Git 协作与练习流程
1. 代码托管平台（练习用）
   - 站点：https://gitea.biochao.cc/AIGPD/BestPractice4Bioinformatics/
   - **注意**：请勿在公共仓库或共享文档中明文保存真实密码。以下示例为课程演示凭证（若仍然有效，仅用于练习）。
     - 用户名：`student`  
     - 密码：`bgicollege2024`

2. 仓库操作与分支练习：
   - 克隆仓库并切换到新分支：
     ```bash
     git clone <repo_url>
     git checkout -b feature/gc-analyzer
     ```
   - 将练习 2 的脚本模块化为可导入的模块 + CLI，完善 docstring 与单元测试。
   - 按功能提交，例如：
     - `feat: 添加序列长度过滤功能`
     - `docs: 更新函数说明`
   - 推送分支到远程：`git push -u origin feature/gc-analyzer`

3. 模拟 Pull Request（PR）与代码审查：
   - 角色 A（开发者）：在平台创建 PR，描述改动与测试覆盖情况。  
   - 角色 B（审查者）：在 PR 中检查代码风格、异常处理、参数逻辑等，提出至少一处改进建议（示例：建议用 `logging` 替换 `print` 并增加日志级别控制）。  
   - 角色 A：根据评论修改、提交并推送，最后合并到 `main` 分支。

---

## 评估标准 🧾
- 功能正确性与测试覆盖（40%）  
- 错误处理与健壮性（20%）  
- 代码可读性、注释与文档（20%）  
- 日志输出与提交记录规范（20%）

---

## 推荐资源 📚
- Pro Git（在线）：第二、三、五章，特别是分支与工作流部分。  
- GitHub Skills：交互式学习 Pull Request 流程。  
- 《Git 飞行规则》（中文）：解决实际使用中的常见问题。

---

## 附注 & 安全建议 ⚠️
- 避免把明文密码、敏感凭证提交到代码库；使用凭证管理或 CI secret 功能替代。  
- 编写 CLI 时，尽量添加单元测试与示例数据以便评估与复现。

---

_Last updated: 2026-01-17_

