# Linux命令

## 1. cat命令作用
    查看文件内容、合并文件、创建文件、以及将内容输出到终端以及其他文件

    查看文件内容：cat filename 会直接在终端显示文件内容。cat /etc/shells 作用：列出了系统中 合法的登录 shell 路径
    合并文件：cat file1 file2 > newfile 将多个文件内容合并到一个新文件中。
    **创建文件** ：cat > filename 可以新建文件并输入内容，按 Ctrl+D 保存退出。

## 2. echo命令作用
    echo 是 Linux/Unix 系统中最常用的命令之一，作用：在终端输出一段文本或变量的值

    1）输出字符：echo "Hello World" -> 输出：Hello World
    2）输出变量：name="Alice" echo name -> 输出：Alice
    3）echo $0：查看当前正在执行的脚本名称
    4）echo $SHELL：查看当前系统默认使用的Shell路径

## 3. shell脚本
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

    








