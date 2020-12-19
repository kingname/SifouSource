from datetime import *


def get_date_of_x_days_ago(today, delta):
    """计算 x 天之前的日期"""
    return today - timedelta(days=delta)
