# 练习
"""
九九乘法表
x = 1
while x <= 9:
    y =1
    while y <= x:
        print(f'{x}*{y}={x*y}   ',end='')
        y+=1
    x+=1
    print()
九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(f'{x}*{y}={x * y}   ', end='')
    print()

# 统计a的个数
count = 0
str01 = 'itheima is a brand of itcast'
for x in str01:
    if x=='a':
        count+=1
print(count)

def fun(tem : float):
    if tem <= 37.5:
        print(f'你的体温{tem}度,体温正常请进')
    else:
        print(f'你的体温{tem}度,需要隔离')

fun(37.5)
"""
money = 5000000
def remain():
    """
    查询余额
    :return: 返回账务剩余数
    """
    return money
def get_money(money01):
    """
    :param money01: 取款金数
    :return:
    """
    remain_money = money-money01
    return f'当前余额:{remain()}'
def post_money(money02):
    """
    :param money02: 存款金额
    :return:
    """
    remain_money = money + money02
    return f'当前金额:{remain()}'
def mian01():
    """
    主函数
    :return:
    """
    name = input('请输入用户名')
