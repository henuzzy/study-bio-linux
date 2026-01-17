def gc_content(seq):
    """计算 DNA 序列的 GC 含量（百分比）。

    参数:
        seq (str): DNA 序列字符串（允许小写或大写）

    返回:
        float: 序列的 GC 含量（百分比）。若输入非法则返回 None。
    """
    try:
        # 将输入序列转为大写，保证后续字符匹配不受大小写影响
        seq = seq.upper()

        # 定义合法碱基集合，仅允许 A/T/C/G
        valid_bases = {'A', 'T', 'C', 'G'}

        # 将序列字符集合与合法集合比较，若有不合法字符则抛出异常
        if not set(seq).issubset(valid_bases):
            raise ValueError("序列中包含非 ATCG 的字符！")

        # 统计 G 和 C 的数量（分别计数后相加）
        gc_count = seq.count('G') + seq.count('C')

        # 计算 GC 百分比；如果序列为空则定义为 0，避免除以 0
        gc_percent = (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

        # 返回计算得到的百分比（浮点数）
        return gc_percent
    except Exception as e:
        # 捕获异常并打印错误信息，返回 None 表示计算失败
        print(f"错误：{e}")
        return None


# 以下为简单测试代码，演示函数行为：
# 对于合法序列，返回 GC 含量（百分比）
print(gc_content("ATGCGC"))       # 期望输出: 66.666... （4/6 ≈ 66.67%）

# 对于包含非法字符的序列，函数会捕获异常并返回 None
print(gc_content("ATGXYZ"))       # 期望输出: 错误提示并返回 None




from collections import defaultdict  # 用于统计 k-mer 出现次数，默认值为 0

def kmer_frequencies(seq, k):
    """统计 DNA 序列中所有长度为 k 的 k-mer 的出现频率。

    参数:
        seq (str): DNA 序列（允许小写或大写）
        k (int): k-mer 的长度，必须为正整数且不超过序列长度

    返回:
        dict: k-mer 到频率的映射（值为 0-1 之间的浮点数）
    """
    try:
        # 将序列统一为大写，便于后续匹配
        seq = seq.upper()

        # 定义合法碱基集合，仅允许 A/T/C/G
        valid_bases = {'A', 'T', 'C', 'G'}

        # 若序列包含非法字符，则抛出异常以提醒调用者
        if not set(seq).issubset(valid_bases):
            raise ValueError("序列中包含非 ATCG 的字符！")
        
        # 检查 k 的合法性：k 必须大于 0 且不超过序列长度
        if k <= 0 or k > len(seq):
            raise ValueError("k 的值不合法！")

        # 使用 defaultdict(int) 来统计每个 k-mer 的出现次数，未出现时默认值为 0
        counts = defaultdict(int)

        # 可产生的 k-mer 总数（滑窗数量），用于后续计算频率
        total = len(seq) - k + 1

        # 遍历每个起始位置，截取长度为 k 的子串并计数
        for i in range(total):
            kmer = seq[i:i+k]  # 当前的 k-mer
            counts[kmer] += 1  # 增加该 k-mer 的计数

        # 将计数转换为频率（出现次数 / 总滑窗数）
        freqs = {kmer: count / total for kmer, count in counts.items()}

        # 返回 k-mer 频率字典
        return freqs
    except Exception as e:
        # 出现错误时打印提示并返回空字典作为失败标志
        print(f"错误：{e}")
        return {}
