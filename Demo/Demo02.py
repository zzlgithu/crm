
"""
# 字符串格式化1
x = 10
y ='jack'
print('x = %5d , y = %s' % (x,y))

# 字符串格式化2
print(f'x = {x},y = {y}')
"""

# 格式化的练习
name = '传智播客'
stock_price = 19.99
stock_code = '003032'
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f'公司:{name},股票代码:{stock_code},当前股价:{stock_price}')
print('每日增长系数:%.1f，经过%d天的增长后,股价达到:%.3f' % (stock_price_daily_growth_factor,growth_days,(19.99*(1+1.2)**7)))
