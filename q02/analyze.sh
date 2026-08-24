#!/bin/bash

# 检查是否只传了1个参数
if [ $# -ne 1 ]; then
    echo "用法: $0 <csv文件路径>" >&2
    exit 1
fi

# 把第一个参数存成变量，方便后面用
csv_file="$1"

# 检查文件是否不存在
if [ ! -f "$csv_file" ]; then
    echo "错误: 文件 '$csv_file' 不存在" >&2
    exit 1
fi

echo "5xx请求Top2路径:"
awk -F, 'NR>1 && $4 ~ /^5/ {print $3}' "$csv_file" \
    | sort \
    | uniq -c \
    | sort -k1,1nr -k2,2 \
    | head -n 2 \
    | awk '{print $2}'

echo -e "\n平均延迟(ms):"
awk -F, 'NR>1 {sum+=$5; count++} END {printf "%.2f\n", sum/count}' "$csv_file"
