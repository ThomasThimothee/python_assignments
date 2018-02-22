import sys
import webget
import xlrd
import matplotlib.pyplot as plt


filename_1 = "data1.xls"
filename_2 = "data2.xls"

def doc_1(argument):
#    webget.download(argument)
#    filename_1 = '
    pass

    
def doc_2(argument):
#    webget.download(argument)
#    filename_2 =
    pass

def question_1():
    wb = xlrd.open_workbook(filename_1)
    sheet = wb.sheet_by_index(0)
    values = []
    years = []
    for row in range(4,24):
        count = 0
        for column in range(2,18,2):
            count += sheet.cell_value(row, column)
        values.append(count)
        year = str(int(sheet.cell_value(row, 0))) #some of the cells are float some are str, if keep all int then the x axis is weird
#        if type(year) == float:
#            year = int(year)

        years.append(year)

    for index, item in enumerate(years):
        if  (item == 20013):
            years[index] = 2001
        if  (item == 20124):
            years[index] = 2012

    plt.plot(years, values)
    plt.axis([min(years), max(years), 0, max(values)])
    plt.title("Evolution of total number of crime", fontsize = 24)
    plt.xlabel("years", fontsize = 14)
    plt.ylabel("Total number of crime", fontsize = 14)
    plt.show()


def question_2():
#    wb = xlrd.open_workbook(filename_1)
#    sheet = wb.sheet_by_index(0)
#    for row in range(4,24,9):
#        for column in range()    
    pass

def question_3():
    pass

def question_4():
    pass

def question_5():
    pass



    
if __name__ == "__main__" :
#    doc_1(sys.argv[1])
#    doc_2(sys.argv[2])
    question_1()
#    question_2()
#    question_3()
#    question_4()
#    question_5()