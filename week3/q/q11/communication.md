# 第11题 协作材料改写

## Issue

### sdt-greet 对空白 name 参数未按预期拒绝

- **环境**：Windows 11（版本 10.0.26200.9168），Python 3.14.0，greetlab-25100021005 0.1.0
- **复现命令**：`sdt-greet --name " "`
- **期望结果**：name 仅含空白字符时，程序拒绝输入并以退出码 2 结束
- **实际结果**：程序仍输出 `Hello, ！`，并以退出码 0 结束

## 提交信息

Reject blank --name input with exit code 2

问题：当 --name 仅包含空白字符（如 " "）时，程序未拦截空白输入，
仍输出 "Hello, ！" 并以退出码 0 结束。
方案：在 main() 中对 a.name.strip() 判空，为空时调用 sys.exit(2)。

## 评审意见

[Blocking] 当 --name 仅含空白字符时，main() 未拦截空白输入，仍输出问候并以 0 退出，违反空白输入应以退出码 2 结束的契约。建议在 parse_args() 后增加 if not a.name.strip(): sys.exit(2)，并补充空白输入的测试用例。
