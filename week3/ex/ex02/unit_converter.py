"""单位换算器 v1.0：支持长度、温度、重量三种类型的单位互转。"""

# ---------- 换算基准表（系数 = 该单位 → 基准单位） ----------
LENGTH_UNITS = {          # 基准：米
    "米": 1.0,
    "千米": 1000.0,
    "厘米": 0.01,
    "毫米": 0.001,
    "英里": 1609.344,
    "英尺": 0.3048,
    "英寸": 0.0254,
}

WEIGHT_UNITS = {          # 基准：千克
    "千克": 1.0,
    "克": 0.001,
    "毫克": 0.000001,
    "吨": 1000.0,
    "磅": 0.45359237,
    "盎司": 0.028349523125,
}

TEMPERATURE_UNITS = ["摄氏度", "华氏度", "开尔文"]   # 非线性换算，单独处理


def to_celsius(value, unit):
    """任意温度单位 → 摄氏度（统一中间量）。"""
    if unit == "摄氏度":
        return value
    if unit == "华氏度":
        return (value - 32) * 5 / 9
    if unit == "开尔文":
        return value - 273.15
    raise ValueError(f"未知温度单位: {unit}")


def from_celsius(c, unit):
    """摄氏度 → 任意温度单位。"""
    if unit == "摄氏度":
        return c
    if unit == "华氏度":
        return c * 9 / 5 + 32
    if unit == "开尔文":
        return c + 273.15
    raise ValueError(f"未知温度单位: {unit}")


def convert_length(value, src, dst):
    """长度换算：单位 → 米 → 目标单位。"""
    return value * LENGTH_UNITS[src] / LENGTH_UNITS[dst]


def convert_weight(value, src, dst):
    """重量换算：单位 → 千克 → 目标单位。"""
    return value * WEIGHT_UNITS[src] / WEIGHT_UNITS[dst]


def convert_temperature(value, src, dst):
    """温度换算：单位 → 摄氏度 → 目标单位。"""
    return from_celsius(to_celsius(value, src), dst)


def run_conversion(conv_type):
    if conv_type == "1":
        units, conv = LENGTH_UNITS, convert_length
    elif conv_type == "2":
        units, conv = TEMPERATURE_UNITS, convert_temperature
    else:
        units, conv = WEIGHT_UNITS, convert_weight

    unit_list = "/".join(units)
    try:
        value = float(input("请输入数值: ").strip())
        src = input(f"输入单位 ({unit_list}): ").strip()
        dst = input(f"输出单位 ({unit_list}): ").strip()
        if src not in units or dst not in units:
            print("单位不在支持列表中，请重试。")
            return
        result = conv(value, src, dst)
        print(f"\n>>> {value:g} {src} = {result:g} {dst}\n")
    except ValueError as e:
        print(f"输入有误: {e}\n")


def main():
    print("=" * 30)
    print("      单位换算器 v1.0")
    print("=" * 30)
    while True:
        print("1.长度  2.温度  3.重量  q.退出")
        cmd = input("请选择换算类型 (1/2/3/q): ").strip().lower()
        if cmd == "q":
            print("再见！")
            break
        if cmd in ("1", "2", "3"):
            run_conversion(cmd)
        else:
            print("无效选择，请重试。")


if __name__ == "__main__":
    main()
