import xlrd
import xlsxwriter
import sys

def huihui():
        # if len(sys.argv) >=2:
        #         name = sys.argv[1]
        # else:
        #         name = 'World'
        # print 'Hello', name, sys.argv[0]
        #
        #
    new_wb = xlsxwriter.Workbook('test_20181001.xlsx')
    new_sheet = new_wb.add_worksheet(u"123")
    new_sheet.write(0, 0, u"123")
    new_wb.close()

huihui()