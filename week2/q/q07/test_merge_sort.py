# 从同目录的 merge_sort.py 导入归并排序函数
from merge_sort import merge_sort

def test_given_input():
    """测试用例1：题目给定的输入数组"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    # 断言：排序后的结果等于预期的升序数组
    assert merge_sort(arr) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_duplicate_elements():
    """测试用例2：包含大量重复元素的数组"""
    # 构造重复元素密集的测试用例，验证算法稳定性和边界处理
    arr = [2, 2, 1, 3, 2, 5, 4, 2]
    assert merge_sort(arr) == [1, 2, 2, 2, 2, 3, 4, 5]
