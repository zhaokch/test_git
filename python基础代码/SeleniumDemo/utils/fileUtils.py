import csv

class FileUtils():

    def read_file(self):
        path = '../files/test.txt'
        f = open(path, 'r')
        print(f.read(2))
        f.close()

    def read_line(self):
        path = '../files/test.txt'
        f = open(path, 'r')
        print(f.readline())
        print(f.readline())
        f.close()

    def read_lines(self):
        path = '../files/test.txt'
        f = open(path, 'r')
        # 将文件保存在列表中
        txt_list = f.readlines()
        print(type(txt_list))
        print(txt_list)
        print(txt_list[0])

    def write(self):
        path = '../files/test.txt'
        f = open(path, 'a+')
        f.seek(0)
        print(f.read())
        f.write('你好python111')
        print(f.read())
        f.close()
        f = open(path, 'r')
        print(f.read())
        f.close()

    def read_with(self):
        path = '../files/test.txt'
        with open(path, 'r') as f:
            print(f.readlines())

    def read_csv(self):
        path = '../files/test.csv'
        file = open(path, 'r')
        csv_file = csv.reader(file)
        for cs in csv_file:
            print(cs[0])

    import xlrd
    excel_path = '../files/test.xlsx'

    def read_excel():
        file = xlrd.open_workbook(excel_path)
        # 获取第一个sheet
        # sheet = file.sheets()[0]
        # 获取名字为'工作表'的sheet
        # sheet = file.sheet_by_name('工作表')
        # 获取第一个工作表
        sheet = file.sheet_by_index(0)
        print(sheet.nrows)
        print(sheet.ncols)
        print(sheet.row_values(1)[0])

if __name__ == '__main__':
    FileUtils().read_with()