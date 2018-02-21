"""
Author: Anderson
project: calculate numbers and write to excel
"""

import xlsxwriter

# 创建一个Excel文件
workbook = xlsxwriter.Workbook('chart.xlsx')
# 创建一个工作表sheet对象，使用默认名称："Sheet1"
worksheet = workbook.add_worksheet()
# 创建一个图表对象
chart = workbook.add_chart({'type':'column'})

# 定义数据表头
title = ['业务名称','星期一','星期二','星期三','星期四','星期五','星期六','星期日','平均']
# 定义业务名称列表
buname = ['业务部门一','业务部门二','业务部门三','业务部门四','业务部门五']
# 定义5个部门一周七天的数据列表
data = [
    [145,110,138,149,155,145,148],
    [189,188,195,93,98,100,199],
    [221,200,198,175,170,198,195],
    [175,177,178,178,174,70,179],
    [188,185,187,190,193,188,184]
]

# 定义数据formatter格式对象，设置边框加粗1像素
formatter = workbook.add_format()
formatter.set_border(1)
# 定义标题栏格式对象：边框加粗1像素，背景色为灰色，单元格内容居中、加粗
title_formatter = workbook.add_format()
title_formatter.set_border(1)
title_formatter.set_bg_color('#cccccc')
title_formatter.set_align('center')
title_formatter.set_bold()
# 定义平均值栏数据格式对象：边框加粗1像素，数字按2位小数显示
ave_formatter = workbook.add_format()
ave_formatter.set_border(1)
ave_formatter.set_num_format('0.00')

# 定义图表数据系列函数
def chart_series(cur_row):
    chart.add_series({
        'categories':'=Sheet1!$B$1:$H$1',
        'values':'=Sheet1!$B${}:$H${}'.format(cur_row,cur_row),
        'line':{'color':'black'},
        'name':'=Sheet1!$A${}'.format(cur_row)
    })
    # 注：其中categories表示x轴，values表示y轴，line表示线条样式，name表示图例项

# 下面分别以行和列的方式将标题栏、业务名称、流量数据写入单元格，并引用不同的格式对象
worksheet.write_row('A1',title,title_formatter)
worksheet.write_column('A2',buname,formatter)
# 写入第2到第6行的数据，并将第2~6行数据加入图表系列
for i in range(2,7):
    worksheet.write_row('B{}'.format(i),data[i-2],formatter)
    # 计算平均流量栏数据并写入
    worksheet.write_formula('I{}'.format(i),'=AVERAGE(B{}:H{})'.format(i,i),ave_formatter)
    # 将每一行数据加入图表序列
    chart_series(str(i))

# 设置图表大小
chart.set_size({'width':577,'height':287})
# 设置图表大标题
chart.set_title({'name':u'业务流量周报表'})
# 设置y轴小标题
chart.set_y_axis({'name':'Mb/s'})

# 在A8单元格插入图表
worksheet.insert_chart('A8',chart)

# 关闭Excel文档
workbook.close()