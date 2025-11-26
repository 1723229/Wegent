#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Calculator - 简单的命令行计算器
支持基本四则运算
"""

def add(x, y):
    """加法"""
    return x + y

def subtract(x, y):
    """减法"""
    return x - y

def multiply(x, y):
    """乘法"""
    return x * y

def divide(x, y):
    """除法"""
    if y == 0:
        raise ValueError("除数不能为0")
    return x / y

def calculator():
    """主计算器函数"""
    print("🧮 欢迎使用Python计算器！")
    print("支持的运算：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出 (q)")

    while True:
        choice = input("\n请选择运算 (1/2/3/4/5): ").strip()

        if choice.lower() == 'q' or choice == '5':
            print("👋 感谢使用计算器，再见！")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ 无效的选择，请重新输入！")
            continue

        try:
            # 获取用户输入
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))

            # 执行相应的运算
            if choice == '1':
                result = add(num1, num2)
                print(f"结果: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"结果: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"结果: {num1} × {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"结果: {num1} ÷ {num2} = {result}")

        except ValueError as e:
            print(f"❌ 输入错误: {e}")
        except Exception as e:
            print(f"❌ 发生错误: {e}")

def main():
    """主函数"""
    try:
        calculator()
    except KeyboardInterrupt:
        print("\n\n👋 程序被用户中断，再见！")

if __name__ == "__main__":
    main()