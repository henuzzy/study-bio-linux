import sys  # 访问系统相关参数和函数
import argparse  # 解析命令行参数
import logging  # 日志记录模块

# 设置日志输出到 stderr，默认级别为 INFO，格式为 [级别] 信息
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='[%(levelname)s] %(message)s')


def parse_fasta(handle):
    """读取 FASTA 文件，将多行序列合并为单行。

    参数:
        handle: 一个可迭代的文本文件句柄（例如打开的文件或 sys.stdin）

    返回:
        生成器，产出 (header, sequence) 对，sequence 为不含换行的完整序列字符串
    """
    header = None  # 当前记录的 header（以 '>' 开头）
    seq_lines = []  # 暂存序列行，稍后合并为单行

    for line in handle:
        line = line.strip()  # 去除行首尾空白和换行符
        if not line:
            # 跳过空行（容错处理）
            continue
        if line.startswith(">"):
            # 遇到新的 header
            if header:
                # 如果已有未输出的记录，则先输出前一条记录
                yield (header, ''.join(seq_lines))
            header = line  # 更新当前 header
            seq_lines = []  # 重置序列行缓存
        else:
            # 非 header 行则为序列内容，加入缓存
            seq_lines.append(line)

    # 文件结束后，如果存在未输出的记录则输出
    if header:
        yield (header, ''.join(seq_lines))


def gc_content(seq):
    """计算序列的 GC 含量（百分比）。

    如果序列包含非法字符（非 ATCG），则记录警告并返回 None。
    """
    try:
        seq = seq.upper()  # 统一为大写，便于判断和统计

        # 验证序列是否仅包含合法碱基
        if not set(seq).issubset({'A', 'T', 'C', 'G'}):
            # 遇到非法字符，抛出异常，后续被捕获并处理
            raise ValueError("非法字符")

        # 统计 G 和 C 的数量
        gc = seq.count('G') + seq.count('C')

        # 计算百分比；空序列时返回 0 避免除以 0
        return (gc / len(seq)) * 100 if len(seq) > 0 else 0
    except Exception as e:
        # 记录警告并返回 None，调用者可以选择忽略或记录该序列
        logging.warning(f"跳过序列（GC计算失败）: {e}")
        return None


def main():
    # 创建命令行参数解析器并添加参数
    parser = argparse.ArgumentParser(description="FASTA 过滤器，支持长度和 GC 含量筛选")

    # 长度与 GC 筛选阈值
    parser.add_argument('--min', type=int, default=0, help='最小序列长度')
    parser.add_argument('--max', type=int, default=1e9, help='最大序列长度')
    parser.add_argument('--gcmin', type=float, default=0, help='最小 GC 含量')
    parser.add_argument('--gcmax', type=float, default=100, help='最大 GC 含量')

    # 输出控制：--stdout 表示打印到终端；--out 指定输出文件
    parser.add_argument('--stdout', action='store_true', help='输出到屏幕')
    parser.add_argument('--out', type=str, help='输出到文件')

    # 输入文件，若不提供则从 stdin 读取（支持管道）
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='输入 FASTA 文件，默认读取 stdin')
    args = parser.parse_args()

    # 决定输出句柄：优先使用 --stdout，若未指定但提供 --out 则写入文件，否则写入 stdout
    output_handle = sys.stdout if args.stdout or not args.out else open(args.out, 'w')

    # 统计总序列数和通过过滤的数量
    count_total = 0
    count_pass = 0

    # 逐条读取并处理 FASTA 记录
    for header, seq in parse_fasta(args.infile):
        count_total += 1  # 计数总记录数
        length = len(seq)  # 计算序列长度

        # 计算 GC，若函数返回 None（表示非法序列），则跳过该序列
        gc = gc_content(seq)
        if gc is None:
            continue

        # 根据长度和 GC 范围筛选，符合则写入输出
        if args.min <= length <= args.max and args.gcmin <= gc <= args.gcmax:
            output_handle.write(f"{header}\n{seq}\n")
            count_pass += 1

    # 若打开了文件句柄（非 stdout），则关闭它
    if output_handle is not sys.stdout:
        output_handle.close()

    # 输出处理统计信息到 stderr（通过 logging）
    logging.info(f"总序列数: {count_total}")
    logging.info(f"通过过滤: {count_pass}")


if __name__ == "__main__":
    # 作为脚本直接运行时，执行主函数
    main()
