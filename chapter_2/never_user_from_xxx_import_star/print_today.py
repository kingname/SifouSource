from util import *
import datetime


now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'现在是北京时间：{now_str}')

three_days_ago = get_date_of_x_days_ago(now, 3)
three_days_ago_str = three_days_ago.strftime('%Y-%m-%d %H:%M:%S')
print(f'3天前的日期是：{three_days_ago_str}')
