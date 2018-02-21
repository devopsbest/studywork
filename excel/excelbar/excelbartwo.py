
import xlsxwriter
"""
Author: Anderson
project: calculate numbers and write to excel
"""

def charts():
    workbook = xlsxwriter.Workbook('chart_column.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    # 这是个数据table的列
    headings = ['Number', 'Batch 1', 'Batch 2']
    data = [
        [2, 3, 4, 5, 6, 7],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
    ]
    # 写入一行
    worksheet.write_row('A1', headings, bold)
    # 写入一列
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])

    ############################################
    # 创建一个图表，类型是column
    chart1 = workbook.add_chart({'type': 'column'})

    # 配置series,这个和前面worksheet是有关系的。
    #     指定图表的数据范围
    chart1.add_series({
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
    })
    chart1.add_series({
        'name': "=Sheet1!$C$1",
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$C$2:$C$7',
    })


    #添加图表标题和标签
    chart1.set_title({'name': 'Results of sample analysis'})
    chart1.set_x_axis({'name': 'Test number'})
    chart1.set_y_axis({'name': 'Sample length (mm)'})

    # 设置图表风格
    chart1.set_style(11)

    # 在D2单元格插入图表（带偏移）
    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

charts()