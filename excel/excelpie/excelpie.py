import xlsxwriter
"""
Author: Anderson
project: calculate numbers and write to excel
"""

def generate_pie():
    workbook = xlsxwriter.Workbook('chart_pie.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    # 生成圆饼图
    chart4 = workbook.add_chart({'type': 'pie'})
    # 定义数据
    data = [
        ['Pass', 'Fail', 'Warn', 'NT'],
        [333, 11, 12, 22],
    ]
    # 写入数据
    worksheet.write_row('A1', data[0], bold)
    worksheet.write_row('A2', data[1])

    chart4.add_series({
        'name': '接口测试报表图',
        'categories': '=Sheet1!$A$1:$D$1',
        'values': '=Sheet1!$A$2:$D$2',
        'points': [
            {'fill': {'color': '#00CD00'}},
            {'fill': {'color': 'red'}},
            {'fill': {'color': 'yellow'}},
            {'fill': {'color': 'gray'}},
        ],
    })
    # Add a chart title and some axis labels.
    chart4.set_title({'name': '接口测试统计'})
    chart4.set_style(3)
    #     chart3.set_y_axis({'name': 'Sample length (mm)'})

    worksheet.insert_chart('E3', chart4, {'x_offset': 10, 'y_offset': 10})
    workbook.close()


generate_pie()