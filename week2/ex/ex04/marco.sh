#!/bin/bash

# 保存当前工作目录到变量
marco() {
    export MARCO_DIR="$PWD"
    echo "已保存当前目录: $MARCO_DIR"
}

# 切换回 marco 保存的目录
polo() {
    if [ -z "$MARCO_DIR" ]; then
        echo "错误：尚未执行 marco 保存目录，请先运行 marco 命令"
        return 1
    fi
    cd "$MARCO_DIR" && echo "已切换到目录: $MARCO_DIR"
}
