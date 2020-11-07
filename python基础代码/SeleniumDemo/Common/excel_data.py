'''
操作excel类
'''
import xlrd
'''
读取excel操作，所有数据存放在字典中
filename为文件名
index为excel sheet工作薄索引
'''

def read_excel(filename, index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data


    return dic

if __name__ == '__main__':
    data = read_excel('../files/testdata.xlsx', 0)
    print(data)
    print(data[0])