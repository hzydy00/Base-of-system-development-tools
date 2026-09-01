#!/usr/bin/env bash

# 配置：日志文件路径与待测脚本路径
STDOUT_LOG="fail_stdout.log"
STDERR_LOG="fail_stderr.log"
TARGET_SCRIPT="./faulty_cmd.sh"

# 运行次数计数器
run_count=0

# 无限循环执行命令，直到失败
while true; do
    run_count=$((run_count + 1))
    # 执行待测脚本，分别重定向标准输出和标准错误
    "$TARGET_SCRIPT" > "$STDOUT_LOG" 2> "$STDERR_LOG"
    # 退出码非0则表示失败，终止循环
    if [[ $? -ne 0 ]]; then
        break
    fi
done

# 打印最终结果
echo "================================"
echo "命令在第 $run_count 次运行时失败"
echo "================================"
echo -e "\n失败时的标准输出："
cat "$STDOUT_LOG"
echo "================================"
echo -e "\n失败时的标准错误："
cat "$STDERR_LOG"
echo "================================"
echo -e "\n输出已持久化保存到 $STDOUT_LOG 和 $STDERR_LOG 文件"
