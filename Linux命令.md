# Linux命令

## cat命令作用
1. 查看文件内容、合并文件、创建文件、以及将内容输出到终端以及其他文件
    ```
    查看文件内容: cat filename 会直接在终端显示文件内容。cat /etc/shells 作用：列出了系统中 合法的登录 shell 路径
    合并文件: cat file1 file2 > newfile 将多个文件内容合并到一个新文件中。
    创建文件: cat > filename 可以新建文件并输入内容，按 Ctrl+D 保存退出。
    ```

## echo命令作用
```
    echo 是 Linux/Unix 系统中最常用的命令之一，作用：在终端输出一段文本或变量的值

    1）输出字符：echo "Hello World" -> 输出：Hello World
    2）输出变量：name="Alice" echo name -> 输出：Alice
    3）echo $0：查看当前正在执行的脚本名称
    4）echo $SHELL：查看当前系统默认使用的Shell路径
```

## shell脚本
```
    shell脚本文件的第一行一般是一个"#!/bin/bash"，表示这个脚本文件使用的是bash解释器

    在Linux系统中，想要执行一个脚本文件，必须要有执行权限，可以使用chmod命令来给这个文件添加执行权限。

    chmod命令:  
        权限类型：
        r → 读 (read)

        w → 写 (write)

        x → 执行 (execute)

        chmod a+x file → 给文件所有者增加执行权限

    shell脚本定义变量：
        read name：表示可以读取用户输入的一个值，并赋值给name
        name=$1, sex=$2：表示定义了两个变量，"./game.sh 张三 男",这就是执行game.sh文件并赋值给name, sex变量

    修改完配置文件后需要重新加载一下配置文件，才会使得配置文件生效。"source **"
  ```

## 文本处理三剑客
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
    
## 在终端查看当前所在目录，常用命令：
```bash
    pwd            # 打印当前工作目录（绝对路径）
    echo "$PWD"    # 显示 shell 环境变量中的当前目录
    readlink -f .  # 显示当前目录的规范化绝对路径（解析符号链接）
```




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
sort file.txt | uniq -c          # 排序并计数唯一值
cut -f1,3 file.tsv               # 提取特定列
tr 'a-z' 'A-Z' < file.txt        # 大小写转换
```

### 进程管理
```bash
nohup command &                  # 后台运行
ps aux | grep process_name       # 查看进程
top                              # 实时进程监控
kill PID                         # 终止进程
```

### 文件安全
```bash
chmod 755 script.sh              # 设置文件权限
ln -s target link_name           # 创建软链接
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

