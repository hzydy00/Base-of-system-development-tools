# AI 修复日志

提示：要求 cli.py 在 name 仅含空白字符时 sys.exit(2)，只改 cli.py，用 pytest 验证。
改动：AI 在 cli.py 新增 import sys 和 if not a.name.strip(): sys.exit(2)。
验证：人工审查无无关修改，pytest 1 passed，空白输入退出码2，正常输入仍打印 Hello。
