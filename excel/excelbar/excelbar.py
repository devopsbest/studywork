

import xlsxwriter


"""
Author: Anderson
project: calculate numbers and write to excel
"""

workbook = xlsxwriter.Workbook('chart_bar.xlsx')
worksheet = workbook.add_worksheet()

# 需要写入的数据,假设我们也像支付宝一样的年度账单
expenses = (['交通', 5900],
            ['购物', 8000],
            ['通信', 2300],
            ['旅游', 5500],
            )  # 行跟列的初始位置
row = 0
col = 0

# .write方法  write（行,列,写入的内容,样式）
for item, cost in (expenses):
    worksheet.write(row, col, item)  # 在第一列的地方写入item
    worksheet.write(row, col + 1, cost)  # 在第二列的地方写入cost
    row = row + 1  # 每次循环行数发生改变

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')  # 写入公式


ColumnChart = workbook.add_chart({'type':'column'})  #定义一个柱型图表
ColumnChart.add_series({                             #定义样式
    'name':'2017年度账单',                                #目标值的名
    'categories':'=Sheet1!$A$1:$A$4',              #item的名
    'values':    '=Sheet1!$B$1:$B$4',            #item的值
    'fill':    {'color':'#FF9900'},              #柱子的颜色
})
ColumnChart.set_x_axis({                             #定义x轴
    'name':'类别',           #标题
    'name_font':{'size':10},                       #字体
})
ColumnChart.set_y_axis({                             #定义y轴
    'name':'金额',                       #标题
    'name_font':{'size':14,'bold':True},           #字体样式
    'num_font':{'italic':True},                    #斜体
})
worksheet.insert_chart('A7',ColumnChart)             #将这个表格插入A7的地方
workbook.close()