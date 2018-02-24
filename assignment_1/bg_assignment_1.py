import sys
import webget
import xlrd
import matplotlib.pyplot as plt
import pprint


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
    plt.title("Question 1: Evolution of total number of crime", fontsize = 24)
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
    
    plt.suptitle('Question 2')
    plt.show()
    
        
#   Question 3: Has the crime moved to from one area to another?
# We cannot really asnwer this question since we have data for 2013 only
# I collected total number of crime per state, I guess that if we had the data over 20 years we could
# answer the question with a 3D histogram and see if one state recorded more crimes while others recorded less
def question_3():
    wb = xlrd.open_workbook(filename_2)
    sheet = wb.sheet_by_index(0)
    state = "ALABAMA"
    count = 0
    results = {}
    #when merge cells (first column, state name) , only first row has value, following ones have empty values
    # sheet.cell_value(4, 0) = Alabama // sheet.cell_value(5, 0) and followings = ""
    for row in range(4,9295):  
        if sheet.cell_value(row, 0) != "":
            results.update({state : count})
            state = sheet.cell_value(row, 0) 
            count = 0     
            for column in range(3,14):
                if sheet.cell_value(row,column) != "":
                    count += int(sheet.cell_value(row,column))
        else :
            for column in range(3,14):
                if sheet.cell_value(row,column) != "":
                    count += int(sheet.cell_value(row,column))

    plt.bar(results.keys(), results.values())  
    plt.xlabel('xlabel', fontsize=5)
    plt.xticks(rotation=90)   
    plt.title("Question 3") 
    plt.show()

#   Question 4: Is there a connection between type of crimes and locations?
# --> look at top 3 crime categories per state, we can see that it is somewhat the same ones
def question_4():
    results = {}
    state = "ALABAMA"
    crimes_categories = {}
    top ={}

    wb = xlrd.open_workbook(filename_2)
    sheet = wb.sheet_by_index(0)
    for row in range(4,9295):  
        if sheet.cell_value(row, 0) != "":
            top = top_cat(crimes_categories)
            results.update({state : top})
            crimes_categories = {}
            state = sheet.cell_value(row, 0)      
            for column in range(3,14):
                count = crimes_categories.get(sheet.cell_value(3, column),  0)
                if sheet.cell_value(row,column) != "":
                    count += int(sheet.cell_value(row,column))
                crimes_categories[sheet.cell_value(3, column)] = count
        else :
            for column in range(3,14):
                count = crimes_categories.get(sheet.cell_value(3, column),  0)
                if sheet.cell_value(row,column) != "":
                    count += int(sheet.cell_value(row,column))
                crimes_categories[sheet.cell_value(3, column)] = count  
    print("__________________")
    print("question 4")
    print("__________________")
    pprint.pprint(results)             

def top_cat(dic):
    my_dic = dic
    top ={}
    for _ in range(3):
        max_cat = ""
        max_value = 0
        for cat, value in my_dic.items():
            if value > max_value:
                max_value = value
                max_cat = cat  
        top[max_cat] = max_value
        my_dic.pop(max_cat, None)   # del my_dic[max_cat] was throwing an error... don't know why  
    return(top)


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

    # wanted to use these values to find the year with biggest crime number and do second subplot
    # dynamically, however it means finding the row where the column 1 equal this value, didn't have the time 
    #to implement it yet. So hardcode the row 4 in second subplot so far
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
    
    plt.suptitle('Question 5')
    plt.show()



    
if __name__ == "__main__" :
#    doc_1(sys.argv[1])
#    doc_2(sys.argv[2])
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()