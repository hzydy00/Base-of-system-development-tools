# wordfreq_optimized.py
words = open("words.txt", encoding="utf-8").read().split()
# 利用set哈希特性去重，时间复杂度O(n)，count结果与原程序完全一致
unique = set(words)
print("count=", len(unique))
