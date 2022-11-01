"""
注释：
    1.注释的作用：通过用自己熟悉的语言，在程序中对某些代码进行标注说明，这就是注释的作用，能够大大增强程序的可读性。
    2.注释的分类及语言
        2.1注释分为两类：单行注释和多行注释。
            2.1单行注释：只能注释一行内容，语法：# 注释内容
            2.2多行注释：可以注释多行内容，一般用在注释一段代码的情况，语法:”“” 一段代码 “”“
"""

# 单行注释:输出hello world
print('hello world')
"""多行注释第一种写法:
输出hello Python"""
'''
多行注释：第二种写法
'''
print('hello Python')

"""
变量
    1.变量的作用：
        1.1 变量的主要作用，就是用来存储信息，然后在计算机程序中使用这些信息。
        1.2 通过给变量赋值，也将数据与一些能够描述的名字连接起来，简单说，就是给数据一个能让人理解的名字。
        1.3 变量的值，最终是存储在内存中。
        1.4 在Python中，对象有类型，变量无类型。
        
    2.定义变量  变量名 = 值  
        2.1 变量名自定义，要满足标识符命名规则。
        2.2 标识符
            2.2.1 标识符命名规则是Python中定义各种名字的时候的统一规范：
                - 有数字、字母、下划线组成
                - 不能数字开头
                - 不能使用内置关键字
                - 严格区分大小写
        2.3命名习惯
            - 见名知义。
            - 大驼峰；即每个单词首字母都大写，例如：MyName.
            - 小驼峰：第二个(含)以后的单词首字母大写，例如：myName。
            - 下划线：例如：my_name.
        2.4 使用变量        
"""

# 定义变量
my_name = 'TOM'
num_1 = 1
num_2 = 2
# 输出变量my_name
print(my_name)
# 使用变量
num_3 = num_1 + num_2
print(num_3)

"""
认识bug
    所谓bug，就是程序中的错误。如果程序有错误，需要程序员排查问题，纠正错误。
"""
# print(My_name) #错误：变量名My_name未定义

"""
Debug工具PyCharm IDE中集成的用来调试程序的工具，在这里程序员可以查看程序的执行细节和流程或者调解bug。

1. Debug工具使用步骤：
    1.1. 打断点
    1.2. Debug调试
2. 打断点
    - 断点位置：目标要调试的代码的第一行代码即可，即一个断点即可。
    - 打断点的方法：单击目标代码的行号右侧空白位置。
"""

"""
数据类型：
    1. 按经验将不同的变量存储不同的的类型的数据
    2. 验证这些数据到底是什么类型 -- 监测数据类型 -- type(数据)
"""

# int -- 整型
num_2 = 1
print(type(num_2))

# float -- 浮点型，就是小数
num_1 = 1.1
print(type(num_1))

# str -- 字符串，特点：数据都要带引号
a = 'hello world'
print(type(a))

# bool -- 布尔型，通常判断使用，布尔型有两个取值Tru，False
b = True
print(type(b))

# list -- 列表
c = [10, 20, 30]
print(type(c))

# tuple -- 元组
d = (10, 20, 30)
print(type(d))

# set -- 集合
e = {10, 20, 30}
print(type(e))

# dict -- 字典 -- 键值对
f = {'name': 'TOM', 'age': 18}
print(type(f))
