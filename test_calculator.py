#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试计算器功能
"""

# 导入计算器中的函数
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator import add, subtract, multiply, divide

def test_calculator():
    """测试计算器的各项功能"""
    print("🧪 开始测试计算器功能...")

    # 测试加法
    assert add(5, 3) == 8, "加法测试失败"
    assert add(-2, 5) == 3, "加法测试失败"
    print("✅ 加法测试通过")

    # 测试减法
    assert subtract(10, 4) == 6, "减法测试失败"
    assert subtract(3, 7) == -4, "减法测试失败"
    print("✅ 减法测试通过")

    # 测试乘法
    assert multiply(6, 7) == 42, "乘法测试失败"
    assert multiply(-3, 4) == -12, "乘法测试失败"
    print("✅ 乘法测试通过")

    # 测试除法
    assert divide(15, 3) == 5, "除法测试失败"
    assert divide(7, 2) == 3.5, "除法测试失败"
    print("✅ 除法测试通过")

    # 测试除零错误
    try:
        divide(5, 0)
        assert False, "除零错误测试失败"
    except ValueError as e:
        assert str(e) == "除数不能为0", "除零错误消息不正确"
        print("✅ 除零错误测试通过")

    print("\n🎉 所有测试通过！计算器功能正常")

if __name__ == "__main__":
    test_calculator()