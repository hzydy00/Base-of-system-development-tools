#!/bin/bash
set -x

# 变量定义与引用
username="student"
echo "当前用户: $username"

# 算术运算
base=20
calc_result=$((base * 3 - 8))
echo "运算结果: $calc_result"

# 条件分支判断
if [ $base -ge 15 ]; then
    echo "数值满足条件"
fi
