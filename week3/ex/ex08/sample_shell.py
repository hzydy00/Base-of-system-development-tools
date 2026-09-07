"""ex08 教学演示：subprocess 的各种写法（含安全/危险/干扰项）。"""
import subprocess

# --- 安全写法：不应该被正则抓到 ---
subprocess.Popen(["ls", "-l"])                       # 1. 无 shell 参数
subprocess.Popen(["ls"], shell=False)                # 2. 显式 shell=False

# --- 危险写法：shell=True，是正则要抓的目标 ---
subprocess.Popen("ls -l", shell=True)                # 3. 单行 shell=True
subprocess.Popen("dir", shell = True)                # 4. 参数带空格 shell = True
subprocess.Popen(                                    # 5. 多行调用，shell=True 在下一行
    "echo hello && whoami",
    shell=True,
)
subprocess.Popen("rm -rf /tmp/x", shell=True, cwd="/tmp")   # 6. shell=True 后面还有参数

# --- 干扰项：不应被误匹配 ---
subprocess.run("ls", shell=True)                     # 7. 是 run 不是 Popen
result = subprocess.Popen("ls")                      # 8. Popen 但没传 shell
# shell=True 出现在注释里
doc = "subprocess.Popen(cmd, shell=True)  # 字符串里也有"
