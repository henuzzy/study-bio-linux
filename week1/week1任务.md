## 学习目标
- 理解 stdin/stdout/stderr 标准流与"管道"哲学
- 掌握文本处理三剑客 (grep, sed, awk) 核心语法
- 熟练使用 sort、uniq、cut、tr 进行数据清洗与格式转换
- 掌握进程管理和文件安全基本概念
- 编写基础 Bash 脚本

## 理论学习内容

### 标准流与管道哲学
- stdin (标准输入): 文件描述符 0
- stdout (标准输出): 文件描述符 1  
- stderr (标准错误): 文件描述符 2
- 管道 (|): 将一个命令的 stdout 连接到另一个命令的 stdin

### 通配符与正则表达式基础
- 通配符: *, ?, [], {}
- 基础正则: ., *, +, ?, [], (), |

## 工具学习内容

### 文本处理三剑客
1. **grep**: 文本搜索
   ```bash
   grep "pattern" file.txt
   grep -v "pattern" file.txt  # 反向匹配
   grep -E "pattern1|pattern2" file.txt  # 扩展正则
   ```

2. **sed**: 流编辑器
   ```bash
   sed 's/old/new/g' file.txt  # 全局替换
   sed -n '10,20p' file.txt    # 打印特定行
   sed '/pattern/d' file.txt   # 删除匹配行
   ```

3. **awk**: 文本处理编程语言
   ```bash
   awk '{print $1, $3}' file.txt  # 打印第1和第3列
   awk '$3 > 100 {print}' file.txt  # 条件过滤
   awk '{sum+=$2} END {print sum}' file.txt  # 求和
   ```

### 数据清洗工具
```bash
# 将文件按行排序，使相同的行相邻（uniq 只能处理相邻重复行）
# 然后用 `uniq -c` 统计每种行的出现次数（输出行首为计数）
# 常见用法：`sort file.txt | uniq -c | sort -nr`  # 按频率降序排列
sort file.txt | uniq -c

# 从以制表符 (TSV) 分隔的文件中提取第1列和第3列（列编号从1开始）
# `-f` 指定字段编号；若分隔符不是制表符，可以配合 `-d` 指定分隔符
# 示例：`cut -f1,3 file.tsv > selected_columns.tsv`
cut -f1,3 file.tsv

# 将小写字母转换为大写，常用于规范化文本
# 使用输入重定向 `< file.txt` 将文件内容传入 `tr`，输出到 stdout
# 示例：`tr 'a-z' 'A-Z' < file.txt > file.UPPER`  # 将结果重定向到新文件
tr 'a-z' 'A-Z' < file.txt
```

### 进程管理
```bash
# 将命令放入后台并忽略挂断信号 (SIGHUP)。注意：
# - `nohup` 会把 stdout/stderr 重定向到 `nohup.out`（若未显式重定向）。
# - `&` 把命令放到后台执行。
# 推荐用法（把输出写到日志）：`nohup command > command.log 2>&1 &`
```bash
nohup → 忽略挂断信号（SIGHUP），使进程在退出 shell/断开会话后继续运行。
command → 要执行的命令或脚本（占位符）。
> command.log → 将 标准输出 (stdout, fd 1) 重定向到文件 command.log（覆盖写入）。
2>&1 → 将 标准错误 (stderr, fd 2) 重定向到当前的 stdout（也就是同样写入 command.log）。顺序很重要：先把 stdout 重定向，再把 stderr 指向 stdout。
& → 把该命令放到后台执行（shell 立即返回提示符）。
```
# 后台运行
nohup command &

# 列出当前系统上的所有进程并通过 `grep` 过滤进程名/关键字。
# `ps aux`（BSD 风格）显示：USER, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT, START, TIME, COMMAND。
# 注意：`ps aux | grep name` 可能匹配到 grep 本身；可用 `grep [n]ame` 或 `pgrep -fl name` 避免。
# 查看进程
ps aux | grep process_name

# 实时监控系统进程和资源使用（CPU、内存、负载等）。
# 常用交互操作：`q` 退出；`P` 按 CPU 排序；`M` 按内存排序；`1` 显示所有 CPU 核心使用。
# `htop` 为更友好的替代工具（若已安装）。
top

# 发送信号终止一个进程。默认 `kill PID` 发送 SIGTERM（允许进程清理退出）。
# 如果进程不响应，可改用 `kill -9 PID`（SIGKILL，强制终止，不可被捕获）。
# 可用 `pgrep` 或 `ps` 先确认 PID；也可用 `pkill -f pattern` 按名称/模式终止。
kill PID
```

### 文件安全
```bash
# 设置文件权限为 755：拥有者可读/写/执行，组和其他用户可读/执行
# 这常用于可执行脚本，示例：`chmod 755 script.sh`。
# 注意：使用更严格权限（如 700）可限制其他用户访问。
chmod 755 script.sh              # 设置文件权限

# 创建指向目标文件/目录的符号链接（软链接），不会复制文件内容
# 用法：`ln -s target link_name`；若希望覆盖已存在的链接可加 `-f`（`ln -sf target link_name`）
# `ls -l link_name` 会显示为 `link_name -> target`。
ln -s target link_name           # 创建软链接

# 将新路径添加到当前会话的 PATH 环境变量，使 shell 能找到该路径下的可执行文件
# 只对当前 shell 有效（会话结束后失效）；若要永久生效，请把该行添加到 `~/.bashrc` 或 `~/.profile` 中
# 示例检查是否已存在：`echo $PATH | tr ':' '\n' | grep -x "/new/path"`
export PATH=$PATH:/new/path      # 添加环境变量
```

## 练习任务

### 练习 1: Shell 脚本 - 批量重命名
**任务**: 编写脚本，使用 For 循环和变量，批量将 100 个测试文件重命名为规范格式。

**要求**:
- 输入文件: test_1.txt, test_2.txt, ..., test_100.txt
- 输出文件: sample_01.data, sample_02.data, ..., sample_100.data
- 必须包含错误处理和日志输出

**模板**:
```bash
#!/bin/bash
# batch_rename.sh - 批量重命名脚本

# 设置日志文件
LOG_FILE="rename.log"
exec 2> "$LOG_FILE"

echo "开始批量重命名任务..." >&2
date >&2

# 你的代码在这里

echo "批量重命名完成!" >&2
date >&2
```

### 练习 2: 数据提取 - GFF 文件处理
**任务**: 使用 awk 从 GFF 文件提取特定列，只保留 feature 为 CDS 且长度 > 100bp 的行。

**输入格式** (GFF):
```
seqid source feature start end score strand frame attributes
```

**输出格式** (TSV):
```
seqid feature start end length
```

**要求**:
- 计算长度 (end - start + 1)
- 只保留 CDS feature
- 只保留长度 > 100bp 的记录
- 输出为 TSV 格式

## 评估标准
- 代码功能正确性 (40%)
- 错误处理完善性 (20%)
- 代码可读性和注释 (20%)
- 日志输出规范性 (20%)

## 推荐资源
- 《Linux 命令行与 Shell 脚本编程大全》
- man 命令手册页
- GNU Awk 用户指南

