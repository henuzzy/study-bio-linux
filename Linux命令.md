# Linux命令

## 1. cat命令作用
    查看文件内容、合并文件、创建文件、以及将内容输出到终端以及其他文件

    查看文件内容：cat filename 会直接在终端显示文件内容。cat /etc/shells 作用：列出了系统中 合法的登录 shell 路径
    合并文件：cat file1 file2 > newfile 将多个文件内容合并到一个新文件中。
    创建文件：cat > filename 可以新建文件并输入内容，按 Ctrl+D 保存退出。

## 2. echo命令作用
    echo 是 Linux/Unix 系统中最常用的命令之一，作用：在终端输出一段文本或变量的值

    1）输出字符：echo "Hello World" -> 输出：Hello World
    2）输出变量：name="Alice" echo name -> 输出：Alice
    3）echo $0：查看当前正在执行的脚本名称
    4）echo $SHELL：查看当前系统默认使用的Shell路径

## 3. shell脚本





