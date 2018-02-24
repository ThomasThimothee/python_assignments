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

#   Question 1: Has the crime decreased or increased over the last 20 years?
def question_1():
    wb = xlrd.open_workbook(filename_1)
    sheet = wb.sheet_by_index(0)
    values = []
    years = []
    for row in range(4,24):
        count = 0
        for column in range(2, 19, 2):
            count += sheet.cell_value(row, column)
        values.append(count)
        year = str(int(sheet.cell_value(row, 0))) #some of the cells are float some are str, if keep all int then the x axis is weird

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

#   Question 2: Has the type of crime changed?
def question_2():
    wb = xlrd.open_workbook(filename_1)
    sheet = wb.sheet_by_index(0)
    crimes_category_1994 = []
    crimes_category_2004 = []
    crimes_category_2013 = []
    wb = xlrd.open_workbook(filename_1)
    sheet = wb.sheet_by_index(0)
    categories = []
    final_categories = []

    for column in range(2, 19, 2):
        categories.append(sheet.cell_value(3, column))  

    #remove line jump from titles because it looks even worse on the chart
    for title in categories:
        title = title.replace("\n","")
        final_categories.append(title)
   

    for column in range(2, 19, 2):
            crimes_category_1994.append(sheet.cell_value(4, column))
    for column in range(2, 19, 2):
            crimes_category_2004.append(sheet.cell_value(14, column))
    for column in range(2, 19, 2):
            crimes_category_2013.append(sheet.cell_value(23, column))

    plt.subplot(221)
    plt.pie(crimes_category_1994, autopct='%1.1f%%')
    plt.title("Crime per category 1994", fontsize = 24)

    plt.subplot(222)
    plt.pie(crimes_category_2004, autopct='%1.1f%%')
    plt.title("Crime per category 2004", fontsize = 24)

    plt.subplot(223)
    plt.pie(crimes_category_2013, autopct='%1.1f%%')
    plt.title("Crime per category 2013", fontsize = 24)

    plt.legend(labels = final_categories, bbox_to_anchor=(1.5, 0), loc='lower left', borderaxespad=0.)
    plt.show()
    
        
#   Question 3: Has the crime moved to from one area to another?
def question_3():
    wb = xlrd.open_workbook(filename_2)
    sheet = wb.sheet_by_index(0)
    

#   Question 4: Is there a connection between type of crimes and locations?
def question_4():
    pass


#   Question 5: Which year was the most crime and what crime occured most times?
def question_5():
    wb = xlrd.open_workbook(filename_1)
    sheet = wb.sheet_by_index(0)
    values = []
    years = []
    crimes_category_1994 = []
    categories = []

    for row in range(4,24):
        count = 0
        for column in range(2, 19, 2):
            count += sheet.cell_value(row, column)
        values.append(count)
        year = str(int(sheet.cell_value(row, 0))) 
        years.append(year)

    max_value = max(values)
    max_index = values.index(max_value)


    for index, item in enumerate(years):
        if  (item == 20013):
            years[index] = 2001
        if  (item == 20124):
            years[index] = 2012

    for column in range(2, 19, 2):
        crimes_category_1994.append(sheet.cell_value(4, column))   

    for column in range(2, 19, 2):
        categories.append(sheet.cell_value(3, column))      
    
    plt.subplot(211)
    plt.bar(years, values)
    plt.axis([min(years), max(years), 0, max(values)])
    plt.ylabel("Total number of crime", fontsize = 7)
    plt.title("Crimes per year", fontsize = 12)

    plt.subplot(212)
    plt.bar(categories,crimes_category_1994)
    plt.ylabel("Number of crime", fontsize = 7)
    plt.title("Crimes per category in 1994", fontsize = 12)
    
    plt.show()



    
if __name__ == "__main__" :
#    doc_1(sys.argv[1])
#    doc_2(sys.argv[2])
#    question_1()
#    question_2()
#    question_3()
#    question_4()
    question_5()