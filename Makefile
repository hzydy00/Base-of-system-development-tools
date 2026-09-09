# paper.pdf：构建实验报告（当前为第 4 周报告，XeLaTeX）
# 用法：make paper.pdf
# 产物输出到 paper/build（不改动被跟踪的 week4.pdf），构建失败时
# make 以非 0 退出，pre-commit 钩子据此拒绝提交
.PHONY: paper.pdf clean

TEXDIR := paper/texpaper/week4
BUILD  := $(CURDIR)/paper/build

paper.pdf:
	mkdir -p $(BUILD)
	cd $(TEXDIR) && xelatex -interaction=nonstopmode -halt-on-error -output-directory="$(BUILD)" week4.tex

clean:
	rm -rf $(BUILD)
