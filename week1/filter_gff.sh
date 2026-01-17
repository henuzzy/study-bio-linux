使用 awk 提取 CDS 且长度 > 100 的行，并输出为 TSV


awk '
BEGIN {
    FS = "\t"; OFS = "\t"  # 设置输入和输出的字段分隔符为制表符
}
!/^#/ && $3 == "CDS" {     # 跳过注释行，只处理 feature 为 CDS 的行
    length = $5 - $4 + 1   # 计算 CDS 的长度（结束位置 - 起始位置 + 1）
    if (length > 100) {    # 只保留长度大于 100bp 的 CDS
        print $1, $4, $5, $7, $9  # 输出：染色体、起始、结束、链向、属性
    }
}
' example.gff > cds_filtered.tsv
