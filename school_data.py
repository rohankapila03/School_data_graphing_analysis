# school_data.py
# Rohan Kapila, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np                           #import numpy and say it can be acessed by stating np
import matplotlib.pyplot as plt              #import mathplotlib.pyplot and say it can be accessed as plt
import math as mt                            #import math musule and say it can be accessed as mt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

def find_name(HS_code,dict):
    """A function that finds the name of coreesponding Highschool when user inputs code.
    
    Parameters: 
    HS_code -- user input that is determined to be a highschool code
    dict -- dictionary corresponding schools and codes to eachother
    
    Return: the value of the HS name from inputted code
    
    """
    return dict[HS_code]

def find_code(HS_name,dict):
    """A function that finds the name of coreesponding Highschool code when user inputs name.
    
    Parameters: 
    HS_name -- user input that is determined to be a highschool name in main code
    dict -- dictionary corresponding schools and codes to eachother
    
    Return: 
    return the value of the HS code from inputted name
    
    """
    for i in dict:
        if dict[i] == HS_name:
            return i
    

def find_school_code_index(code,list_codes):
    """Function that finds the index of the school code that is inputeed or to be found.
    
    Parameters:
    code -- The code for a specific school found by using the class function
    list_codes -- list of codes that were hard copied in and used to find the index correlating to the array
    
    Return:
    return the index found in the list of codes which corresponds to the index of the code in the array
    """
    index = list_codes.index(code)
    print(index)
    return index


def mean_enrollment_GR10(data2018_2019,data2019_2020,data2020_2021,index):
    """Function that calculates the average of the average of grade 10 for each year of data imported
    
    Parameters:
    data2018_2019 -- the data imported as an array from the csv files for the years 2018 and 2019
    data2019_2020 -- the data imported as an array from the csv files for the years 2019 and 2020
    data2020_2021 -- the data imported as an array from the csv files for the years 2020 and 2021
    index -- the index of the user code inputted inorder to find the value of the array

    Returns:
    gr10-enroll -- the mean average of grade 10 returned back.
    """
    gr10_enroll = (data2018_2019[index][1]+data2019_2020[index][1]+data2020_2021[index][1])/3
    return gr10_enroll

def mean_enrollment_GR11(data2018_2019,data2019_2020,data2020_2021,index):
    """Function that calculates the average of the average of grade 11 for each year of data imported
    
    Parameters:
    data2018_2019 -- the data imported as an array from the csv files for the years 2018 and 2019
    data2019_2020 -- the data imported as an array from the csv files for the years 2019 and 2020
    data2020_2021 -- the data imported as an array from the csv files for the years 2020 and 2021
    index -- the index of the user code inputted inorder to find the value of the array

    Returns:
    gr11-enroll -- the mean average of grade 11 returned back.
    """
    gr11_enroll = (data2018_2019[index][2]+data2019_2020[index][2]+data2020_2021[index][2])/3
    return gr11_enroll

def mean_enrollment_GR12(data2018_2019,data2019_2020,data2020_2021,index):
    """Function that calculates the average of the average of grade 12 for each year of data imported
    
    Parameters:
    data2018_2019 -- the data imported as an array from the csv files for the years 2018 and 2019
    data2019_2020 -- the data imported as an array from the csv files for the years 2019 and 2020
    data2020_2021 -- the data imported as an array from the csv files for the years 2020 and 2021
    index -- the index of the user code inputted inorder to find the value of the array

    Returns:
    gr12-enroll -- the mean average of grade 12 returned back.
    """
    gr12_enroll = (data2018_2019[index][3]+data2019_2020[index][3]+data2020_2021[index][3])/3
    return gr12_enroll

def graduate(data2018_2019,data2019_2020,data2020_2021,index):
    """Function that calculates the graduated students of grade 12 for each year of data imported
    
    Parameters:
    data2018_2019 -- the data imported as an array from the csv files for the years 2018 and 2019
    data2019_2020 -- the data imported as an array from the csv files for the years 2019 and 2020
    data2020_2021 -- the data imported as an array from the csv files for the years 2020 and 2021
    index -- the index of the user code inputted inorder to find the value of the array

    Returns:
    gr12_grad -- the sum of each years grade 12.
    """
    gr12_grad = (data2018_2019[index][3]+data2019_2020[index][3]+data2020_2021[index][3])
    return int(gr12_grad)



schooldata_2018_2019 = np.genfromtxt('SchoolData_2018-2019.csv',delimiter = ',', skip_header = True) 
schooldata_2019_2020 = np.genfromtxt('SchoolData_2019-2020 (1).csv',delimiter = ',',skip_header = True)             #import csv files for each year and dont include headers
schooldata_2020_2021 = np.genfromtxt('SchoolData_2020-2021.csv',delimiter = ',',skip_header = True)     
school_dict = {1224 :'Centennial High School',                                                                      #create hard copy of dictionaries that correlate school codes to school name, used to find the correlating name or code which can be used to create object.
1679 : 'Robert Thirsk School',
9626 : 'Louise Dean School',
9806 : 'Queen Elizabeth High School',
9813 : 'Forest Lawn High School',
9815 : 'Crescent Heights High School',
9816 : 'Western Canada High School',
9823 : 'Central Memorial High School',
9825 : 'James Fowler High School',
9826 : 'Ernest Manning High School',
9829 : 'William Aberhart High School',
9830 : 'National Sport School',
9836 : 'Henry Wise Wood High School',
9847 : 'Bowness High School',
9850 : 'Lord Beaverbrook High School',
9856 : 'Jack James High School',
9857 : 'Sir Winston Churchill High School',
9858 : 'Dr. E. P. Scarlett High School',
9860 : 'John G Diefenbaker High School',
9865 : 'Lester B. Pearson High School'
}
school_codes = [1224,1679,9626,9806,9813,9815,9816,9823,9825,9826,9829,9830,9836,9847,9850,9856,9857,9858,9860,9865]  #create a list of school codes to find index
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays



# Add your code within the main function. A docstring is not required for this function.
def main():
    
    print("ENDG 233 School Enrollment Statistics\n")                                                                  #introduce the program

    print('Array data for 2020 - 2021:')                                                                               #display the imported arrays and label each year of the array for yeart 2020 and 2021
    print(schooldata_2020_2021)
    
    print('Array data for 2019 - 2020:')                                                                               #display the imported arrays and label each year of the array for year 2019 and 2020
    print(schooldata_2019_2020)
    
    print('Array data for 2018 - 2019:')                                                                               #display the imported arrays and label each year of the array for year 2018 and 2019
    print(schooldata_2018_2019)               
    # Print array data here

    

    # Add request for user input here
    x = True                                                                                                          #create while loop that will return to the top of the loop if the users input is not valid, initially state the variable as the same variable value for while loop
    while x == True:
        user_input = input('Please enter the highschool name or highschool code: ')                                                    #tell user to input a code or a school
        if user_input.isnumeric():                                                                                    #check if user input is numeric, checking if its a code
            if int(user_input) in school_dict.keys():                                                                 #check if code in dictionary keys to see if its a valid code
                highschool_code = int(user_input)                                                                     #if above is valid, create variable of highschool code
                school_object = School(find_name(highschool_code,school_dict),highschool_code)                        #create object using the school class and initialize variables using the parameter code and functin to find HS name
                x != True                                                                                             #break out of whike lopp so the program can continue to run
                break
            else:
                print('You must enter a valid school name or school code')
        elif user_input in school_dict.values():                                                                      #check if the user input is a school, by looking if it is in dictionary values
            highschool_name = user_input                                                                              #if above statement is true then assighn the HS name to a variable
            school_object = School(highschool_name,find_code(highschool_name,school_dict))                            #create an object using the school class with parameters of HS name and the function to find the code
            x != True                                                                                                 #break out of loop if valid input
            break
        else:
            print('You must enter a valid school name or school code')
            x = True                                                                                                  #if user input not valid assighn variable that will make while loop valid again



    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    school_object.print_all_stats()                                                                                   #call the method inside the class using dot notation for a specific object, this line prints out all the stats, the statement to print is located inside the method function                             
    # Add data processing and plotting here
    index_val = find_school_code_index(school_object.code,school_codes)                                               #call the function to find the index of the code in a list which also correspods to the index of the code in the array and return it and store as a variable                                   
    
    mean_enroll_GR10 = mean_enrollment_GR10(schooldata_2018_2019,schooldata_2019_2020,schooldata_2020_2021,index_val) #call the function to calculate the mean enrollment of grade 10, use the parameters of all imported csv files and the index value of the code, store the return of the function as a variable
    print('Mean enrollment for grade 10: ', mt.floor(mean_enroll_GR10))                                               #print the mean enrollment of grade 10

    mean_enroll_GR11 = mean_enrollment_GR11(schooldata_2018_2019,schooldata_2019_2020,schooldata_2020_2021,index_val) #call the function to calculate the mean enrollment of grade 11, use the parameters of all imported csv files and the index value of the code, store the return of the function as a variable
    print('Mean enrollment for grade 11: ', mt.floor(mean_enroll_GR11))                                               #print the mean enrollment of grade 11, use the math module function floor to round number to nearest whole

    mean_enroll_GR12 = mean_enrollment_GR12(schooldata_2018_2019,schooldata_2019_2020,schooldata_2020_2021,index_val) #call the function to calculate the mean enrollment of grade 12, use the parameters of all imported csv files and the index value of the code, store the return of the function as a variable
    print('Mean enrollment for grade 12: ', mt.floor(mean_enroll_GR12))                                               #print the mean enrollment of grade 12, use the math module and floor function inside that module to print the integer rounded down

    graduated = graduate(schooldata_2018_2019,schooldata_2019_2020,schooldata_2020_2021,index_val)                    #call the graduate function which is practcally the same as the mean average of grtade 12 except it is not divided by 3.
    print('Total number of students who graduated in the past three years: ',graduated)                                                                        #print students who graduated in grade 12 from the return value of the function graduate
    #plot 
    plt.figure(1)                                                                                                     #label the first plot as figure(1) so this graph will post on a diffrent page than the bonus and the graph will also access a page
    plt.xticks([10,11,12])                                                                                            #on graph the points 10,11,12 will only print on the xaxis scale
    grades = np.array([10,11,12])                                                                                     #using the numpy module convert a list of the grades into an array so it can be plotted
    student_num_yr_2021 = np.array([schooldata_2020_2021[index_val][1],schooldata_2020_2021[index_val][2],schooldata_2020_2021[index_val][3]]) #using the numpy module create an array from a list of the seperate grades in each year
    plt.plot(grades,student_num_yr_2021,'o',color = 'b', label = '2021 enrollment')                                                            #make a plot using the grades array as a x point and the schooldata for each grade in year 2020 as y point, make it a dot and the color blue and label it 2021 enrollment
    student_num_yr_2020 = np.array([schooldata_2019_2020[index_val][1],schooldata_2019_2020[index_val][2],schooldata_2019_2020[index_val][3]]) #make an array for each grade and the num studesnts in that grade for the year 2019
    plt.plot(grades,student_num_yr_2020,'o',color ='g',label = '2020 enrollment')                                                              #make a plot for the grades as x points and the number of students in the year 2019 for each grade as y points, make it a dot and the color green label it 2020 enrollment
    student_num_yr_2019 = np.array([schooldata_2018_2019[index_val][1],schooldata_2018_2019[index_val][2],schooldata_2018_2019[index_val][3]])  #make an array for num of students in each grade for the year 2018
    plt.plot(grades,student_num_yr_2019,'o',color = 'r',label ='2019 enrollment')                                                              #make a plot using the grade as the x point and the num student in 2018 for each grade in year 2018 as y points, make it a dot and the color red, label 2019 enrollment for legend
    plt.title('Grade enrollment by year')                                                                             #create the title of figure 1
    plt.xlabel('Grade Level')                                                                                         #label the x-axis with a statemenr
    plt.ylabel('Number of Students')                                                                                  #label the y axis with a statement
    plt.legend(shadow = True,loc = "upper left")                                                                      #create a legend and list the location as upper left and give it a shadow
   
#Bonus
    plt.figure(2)                                                                                                     #Create another figure with the number 2, this will ensure the plot pops up on another page
    plt.subplot(3,1,1)                                                                                                #create a plot that will have 3 rows and 1 column which can contain 3 sperate plots, place this plot in the 1st row and only column
    plt.xticks([2019,2020,2021])                                                                                      #the x axis will display the years 2019,2020,2021 as tick points rather than a bunch of numbers this is imported from the pyplot module
    grades_years = np.array([2019,2020,2021])                                                                         #make an array for the years 
    grade_10_enrollment = np.array([schooldata_2018_2019[index_val][1],schooldata_2019_2020[index_val][1],schooldata_2020_2021[index_val][1]]) # access all the grade 10 values at diffrent years, place them as an array, this is done by accessing the numpy module
    plt.plot(grades_years,grade_10_enrollment,'--',color = 'y',label = 'Grade 10')                                    #create a plot using the arrays of years and the grade 10 for diffrent years array created above, make the line dashed and yellow, label it as Grade 10
    plt.title('Enrollment By Grade')                                                                                  #make a title of the plot only for the first one
    plt.ylabel('Number of Students',fontsize = 8)                                                                     #make a label on y - axis and change the font size to 8
    plt.legend(shadow = True, loc = "upper right")                                                                    #create a legend for the graph and locate it on the upper right, give the legend a shadow aswell
    
    plt.subplot(3,1,2)                                                                                                #create a second plot on figure 2, the same as the above plot, however put the subplot in the second row instead
    plt.xticks([2019,2020,2021])                                                                                      #only show the tick in the list on the x-axis scale
    grades_years = np.array([2019,2020,2021])                                                                         #create an array for the years
    grade_11_enrollment = np.array([schooldata_2018_2019[index_val][2],schooldata_2019_2020[index_val][2],schooldata_2020_2021[index_val][2]]) #create an array for the grade 11 students in each dif year by accessing the 3rd column of each array at the given code index
    plt.plot(grades_years,grade_11_enrollment,'--',color = 'm',label = 'Grade 11')                                    #plot the grades years array and the array of grade 11 enrollment above,make sure the line is dashed and magenta, label the graphas a grade 11
    plt.ylabel('Number of Students',fontsize = 8)                                                                     #add a label on the y axis and make the font size smaller
    plt.legend(shadow = True, loc = "upper right")                                                                    #create a legend with a shadow and locate it on the upper right
    
    plt.subplot(3,1,3)                                                                                                #plot the graph on the same figure 2 as above but have the plot in the subsection of the third row
    plt.xticks([2019,2020,2021])                                                                                      #the x axis will onlist show the list of values as ticks rather than the whole scale
    grades_years = np.array([2019,2020,2021])                                                                         #create an array with the years in the list
    grade_12_enrollment = np.array([schooldata_2018_2019[index_val][3],schooldata_2019_2020[index_val][3],schooldata_2020_2021[index_val][3]]) #create a array using the numpy module and the grade 12 students for each year
    plt.plot(grades_years,grade_12_enrollment,'--',color = 'c',label = 'Grade 12')                                    #plot the grade years and the grade 12 enrollment array created above, label the graph as a dashed line with the color cyan, lebel the plot as Grade 12
    plt.ylabel('Number of Students',fontsize = 8)                                                                     #label the y axis and lower the fontsize to 8
    plt.xlabel('Enrollent year')                                                                                      #label the x axis
    plt.legend(shadow = True, loc = "upper right")                                                                    #create a legend in the upper right that has a shadow
    plt.show()                                                                                                        #using the function imported trought the matplotlib module, this function prints the graphs out on a seperate page
    





    # Do not modify the code below
if __name__ == '__main__':                                                                                            #if the file is run in the main rather than being imported it will call the main function which has all the above code
    main()                                                                                                            #call the main function and allow it to run

