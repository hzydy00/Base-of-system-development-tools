import sys
from my_pkg import mean, stddev, variance


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("用法: my-stats <数字1> <数字2> ...")
        raise SystemExit(1)
    numbers = [float(a) for a in args]
    print(f"均值  : {mean(numbers):.4f}")
    print(f"方差  : {variance(numbers):.4f}")
    print(f"标准差: {stddev(numbers):.4f}")


if __name__ == "__main__":
    main()
