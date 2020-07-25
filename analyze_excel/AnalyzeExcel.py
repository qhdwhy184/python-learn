# coding=utf-8
import os
import xlrd
import xlsxwriter
import datetime


def build_result_file(f1_path, index, src_index_field, new_field):
    print '开始分析处理表1，[表1文件路径]:%s, [表1中匹配字段名称]: %s' % (f1_path.encode("utf-8"), src_index_field.encode("utf-8"))
    wb = xlrd.open_workbook(f1_path)

    sheet = wb.sheets()[0]
    num_cols = sheet.ncols
    num_rows = sheet.nrows
    index_field_no = -1
    new_field_no = num_cols

    for coln in range(num_cols):
        if sheet.cell_value(0, coln) == src_index_field:
            index_field_no = coln
            break

    if index_field_no == -1:
        print '字段 %s 在表1中不存在' % src_index_field.encode("utf-8")
        return

    print '表1共%s行记录, 每行记录有%s列' %(num_rows, num_cols)

    new_wb = xlsxwriter.Workbook('分析结果.xlsx')
    new_sheet = new_wb.add_worksheet(sheet.name)

    for rown in range(0, num_rows):
        print '正在处理第%s行' % rown
        for coln in range(0, num_cols):
            new_sheet.write(rown, coln, sheet.cell_value(rown, coln))
        if rown == 0:
            new_sheet.write(0, new_field_no, new_field)
        else:
            index_field_val = sheet.cell_value(rown, index_field_no);
            if index_field_val in index:
                new_sheet.write(rown, new_field_no, index[index_field_val])
            else:
                new_sheet.write(rown, new_field_no, u'没找到')

    print '开始创建添加字段后的新文件，文件名称:分析结果.xlsx'
    new_wb.close()
    print '完成创建新文件'


def buildIndex(file2_path, index_field, new_field):
    print '开始创建索引, [表2文件路径]:%s, [表2中匹配字段名称]:%s, [从表2中提取的字段名称]:%s' % \
          (file2_path.encode("utf-8"), index_field.encode("utf-8"), new_field.encode("utf-8"))

    wb = xlrd.open_workbook(file2_path)
    sheet = wb.sheets()[0]
    num_cols = sheet.ncols
    num_rows = sheet.nrows

    index_field_no = -1
    new_field_no = -1
    for coln in range(num_cols):
        if sheet.cell_value(0, coln) == index_field:
            index_field_no = coln

        if sheet.cell_value(0, coln) == new_field:
            new_field_no = coln

        if index_field_no != -1 and new_field_no != -1:
            break

    if index_field_no == -1:
        print '字段 %s 在表2中不存在' % index_field.encode("utf-8")
        return

    if new_field_no == -1:
        print '字段 %s 在表2中不存在' % new_field.encode("utf-8")
        return

    index = {}
    for rown in range(1, num_rows):
        index_field_val = sheet.cell_value(rown, index_field_no)
        new_field_val = sheet.cell_value(rown, new_field_no)

        if index_field_val not in index:
            index[index_field_val] = new_field_val

    print '结束创建索引，共索引记录: %s 条' % index.__len__()
    return index


def main():
    start_time = datetime.datetime.now().replace(microsecond=0)
    print "开始时间: %s" % start_time

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, '程序启动参数.txt'))
    args = f.read().splitlines()
    tb1_path = unicode(args[0][(args[0].index(':'))+1:], "utf-8")
    tb2_path = unicode(args[1][(args[1].index(':'))+1:], "utf-8")
    file1_idx = unicode(args[2][(args[2].index(':'))+1:], "utf-8")
    file2_idx = unicode(args[3][(args[3].index(':'))+1:], "utf-8")
    new_field = unicode(args[4][(args[4].index(':'))+1:], "utf-8")

    print "[表1文件路径]:", tb1_path
    print "[表2文件路径]:", tb2_path
    print "[表1中匹配字段名称]:", file1_idx
    print "[表2中匹配字段名称]:", file2_idx
    print "[从表2中提取的字段名称]:", new_field

    index_map = buildIndex(tb2_path, file2_idx, new_field)
    build_result_file(tb1_path, index_map, file1_idx, new_field)
    end_time = datetime.datetime.now().replace(microsecond=0)
    print "结束时间 : %s" % end_time
    print "总用时: %s" % (end_time - start_time)


main()






