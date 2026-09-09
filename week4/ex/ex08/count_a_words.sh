#!/usr/bin/env bash
# 实例8：统计 /usr/share/dict/words（本仓库用下载的标准词表 words）
# 中包含至少三个 a 且不以 's 结尾的单词个数
set -euo pipefail

DICT="${1:-words}"

# 包含至少三个小写 a 的单词数
total_a3=$(grep -c "a.*a.*a" "$DICT")
# 其中以 's 结尾的单词数（需排除）
ending_s=$(grep -c "a.*a.*a's$" "$DICT")

echo "词表总词数:      $(wc -l < "$DICT")"
echo "含至少3个 a 的词:  $total_a3"
echo "其中以 's 结尾的:  $ending_s"
echo "结果(相减):        $((total_a3 - ending_s))"
