###Importing any functions to be used###
import datetime
from datetime import date



###opening up the main list used throughout###
bills = []



######################### Main Menu Function #################################

def chosen_option():
    """Main Menu Display and returns the option chosen, it does this with 
    complexity O(1) as it is only based on a single input"""
    print('\n{:^16s}'.format('Menu') 
          +'\n'+'='*16+"\n1. View Bills\n2. Add new bill\n3. View Reports\n4. Read T&C's\n5. Quit")
    return get_input("\nPlease choose option: ")




################### Reading and Writing to the file functions#################

def read_from_csv():
    """Reads any existing bills from the csv, it does this with complexity
    O(n) as its runtime is dependant on the number of bills"""
    bills.clear() #ensures file is clean and ready to go for new run of code#
    
    for line in open("bills.csv"):
        if line.strip() == "": #Gets rid of any blank lines#
            continue   
        
        bill = line.strip().split(',') #Separates lines into elements of a list#
        #Now this section removes any blank spaces between elements of the list#
        #and ensures each element is of correct type#
        bill[0] = bill[0].strip()
        bill[1] = bill[1].strip()
        bill[2] = int(bill[2].strip())
        bill[3] = int(bill[3].strip())
        bill[4] = int(bill[4].strip())
        bill[5] = float(bill[5].strip())
        bill[6] = bill[6].strip()
        bills.append(bill) #Adds new line from the csv to the bills matrix#
    return bills



def write_new_bill(bills):
    """Writes new bills to the file project.txt, with complexity O(n) 
    as its runtime is dependant on the number of bills"""
    file_bills = open("bills.csv", "w")
    for line in bills:
        #converts each bill into a comma seperated list and adds it to the csv#
        line[2]= str(line[2])
        line[3]= str(line[3])
        line[4]= str(line[4])
        line[5]= str(line[5])
        while len(line) >= 8:
            line.pop()
        file_bills.write(','.join(line) + '\n')
    file_bills.close()
    
    
    
################## Data gathering/generating functions #######################    

def gather_new_data(bills):
    """Gathers new bill data from user inputs to be added to bills,
    it does this with complexity O(1) as it is dependant on inputs"""
    #Calls upon error handling functions for each input#
    provider = provider_error()
    customer = customer_error()
    year = int(year_error())
    month = int(month_error())
    day = int(day_error(month,year))
    amount = round(float(amount_error()),2)
    debit_or_credit = debit_or_credit_error()
    #Adding the new bill to the bills matrix#
    bill = []
    bill.append(provider)
    bill.append(customer)
    bill.append(year)
    bill.append(month)
    bill.append(day)
    bill.append(amount)
    bill.append(debit_or_credit.lower())
    bills.append(bill) 
    print('\nSuccess!\nThe new bill has been entered\nThank you!')
    
    


##Assuming the most popular provider is the one with the most bills##
def most_popular_utility_company(bills):
    """Finds the most popular utility provider and their number of bills
    with complexity O(n),as its runtime is dependant on number of bills"""
    #Scans through bills and gets all providers#
    providers = []
    for line in bills:
        provider = line[0]
        providers.append(provider)
    #Scans through to find the number of bills to each provider#
    provider_number_bills = []
    for provider in providers:
        provider_number_bills.append(providers.count(provider))
    #Forms a list of lists with providers matched to their number of bills#
    matched = list(zip(providers, provider_number_bills))
    matched = list(dict.fromkeys(matched))
    #Finds the max number of bills in the success list#
    max = 0
    for n in range (0 , (len(matched))):
        if (matched[n][1] > max):
           max = matched[n][1]
    popular_providers = []
    #Adds providers to list in order of popularity#
    for n in range (0 , (len(matched))):
        if (matched[n][1] >= max):
           popular_providers.append(matched[n][0])
    #Returns the most popular provider(s) and their number of bills#
    return [popular_providers,max] 


def last_day_of_month(month,year):
    """Returns the last day of each respecitve month
    to be used in error handling of day, this function has 
    complexity O(1) as it is dependant on constants"""
    last_day_30th=[9,4,6,11]
    last_day_31st=[1,3,5,7,8,10,12]
    if month in last_day_30th:
        last_day_in_month=30
    elif month in last_day_31st:
        last_day_in_month=31
    elif month == 2 and year%4 == 0: #Check for leap year in range of years defined#
        last_day_in_month=29
    else:
        last_day_in_month=28
        
    return last_day_in_month


def highest_debit(bills):
    """Finds the highest debit amount in one bill with complexity O(n),
    as its runtime is dependant on number of bills"""
    debits = []
    for line in bills:
        if line[6] == 'debit':  #Adds any debit value to list of debits#
            debits.append(float(line[5])) 
    return max(debits) #returns the highest debit value#



def highest_credit(bills):
    """Finds the highest credit amount in one bill with complexity O(n),
    as its runtime is dependant on number of bills"""
    credits = []
    for line in bills:
        if line[6] == 'credit':  #Adds any credit value to list of debits#
            credits.append(float(line[5]))        
    return max(credits) #returns the highest credit value#


def dates(list_of_dates):
    """Fills a list (given as input) with a list of datetime values generated
    from the bills matrix, it does this with complexity O(n),as its runtime
    is dependant on number of bills"""
    #creates the dates list#
    for line in bills:
        date = datetime.datetime(line[2], line[3], line[4])
        list_of_dates.append(date) #Adds the new datetime value to the list#
        
    
def average_time_between_bills(bills):
    """"Calculates the average time between bills, with complexity O(n),
    as its runtime is dependant on the number of different dates 
    and as such on the number of bills"""  
    #Uses dates function above#
    list_of_dates = []
    dates(list_of_dates)
    #Sorts the date list#
    list_of_dates= sorted(list_of_dates)
    #Calculates time between bills#
    diff_in_dates = []
    for n in range(1,len(list_of_dates)):
        difference = (list_of_dates[n]-list_of_dates[n-1])
        diff_in_dates.append(difference.days)
    #Error handling#
    if len(diff_in_dates)== 0:
        raise ZeroDivisionError('Cannot divide by Zero')
    #Calculates average time between bills and rounds to 2dp#
    average_between_bills=sum(diff_in_dates)/len(diff_in_dates)
    average_between_bills=round(average_between_bills,2)
    return average_between_bills

def order_bills_by_date(bills):
    """Sorts the bills matrix by date into either ascending or descending order
    it does this with complexity O(n),as its runtime is dependant on 
    number of bills"""
    #Froms new bills matrix with new date column which will be used for sorting#
    sorted_bills = []
    for line in bills:
        sorted_bills.append(line)
    for line in sorted_bills: #Adds new datetime value onto each line#
        line.append(date(line[2], line[3], line[4]))
    #Asks how user wants bills sorted and sorts accordingly
    asc_dsc = None
    while asc_dsc == None:
        asc_dsc=get_input("\nWould you like the bills to be in ascending or descending order"
                  +"\n1.Ascending"
                  +"\n2.Descending"
                  +"\n\nPlease Choose Option: ")
        if asc_dsc == "1": #The below sorts bills in ascending order#
            sorted_bills = sorted(sorted_bills,key=lambda x: x[-1],reverse=True)
        elif asc_dsc == "2": #The below sorts bills in descending order#
            sorted_bills = sorted(sorted_bills,key=lambda x: x[-1],reverse=False)
        else:   #The above also removes the datetime column from bills#
            print("Invalid choice, please try again")
            asc_dsc=None
    return sorted_bills


    
################### Report Generating Functions ##############################

def bills_viewer(bills):
    """First Report Generating Function (Bill viewing function),
    this functions has complexity O(n),as its runtime is dependant on
    number of bills"""
    #Producing the main title and eaach column title
    print('\n'+'{:^110}'.format('Bills')
         +'\n'+'='*110)
    print('\nUtility Company\t\tCustomer\t\tDate (YYYY/MM/DD)\t  Amount\t\tType'
         +'\n'+'-'*110)
    #Entering the bills in line by line
    for line in bills:
        print("{:<20}\t{:<10}\t\t{}\t\t{:^10}\t\t{:<10}".format(
               str(line[0]),line[1],date(line[2],line[3],line[4]),line[5],line[6]))
    
        
    

def Yearly_Report(bills):
    """Produces a report with columns: Year, Total Credited and Total Debited,
    it does this with complexity O(n^2) as the the runtime is dependant on
    the number of bills and on the number of different years in those bills"""
    #Producing the Main heading and the column headings#
    print('\n'+'{:^40}'.format('Yearly Report')
          +'\n'+'='*40)
    print('Year\tTotal Credited\t  Total Debited'
          +'\n'+'-'*40)
    #Runs through years and if a year is lower than current min,#
    #It is assigned to be the new min and the opposite for max  #
    min_year = 3000
    max_year = 1000
    for line in bills: 
        if min_year > line[2]:
            min_year = line[2]
        if max_year < line[2]:
            max_year = line[2]
    years = list(range(min_year, max_year+1))
    #Runs through each year and adds up the debit and credit values for each year#
    for year in years:
        debits_for_year = 0.0
        credits_for_year = 0.0
        for line in bills:
            if line[2] == year:
                if line[6] == "debit":
                    debits_for_year += line[5]
                elif line[6]=="credit":
                    credits_for_year += line[5]
        if debits_for_year != 0 or credits_for_year != 0:
            print("{:<7}{:^16}\t{:^16}".format(year, round(credits_for_year,2),\
                                               round(debits_for_year,2)))
   

def Most_Popular_Company_Report(bills): 
    """Produces a report showing the most popular provider,
    it does this with complexity O(n) as this is the complexity of the function
    'most_popular_utiltiy_company(bills)' which this function calls upon"""
    #Using a previous function#
    data = most_popular_utility_company(bills)
    #Displaying the Title and Headings#
    print('\n'+'{:^40}'.format('Most Popular Company Report')
           +'\n'+'='*40)
    print('Utility Company\t   Number of Bills'
           +'\n'+'-'*40)
    #prints one of the options in a report#
    #handles if there are no bills, one popular provider#
    #or multiple equally popular providers#
    if (len(data[0]) == 0):
       print("Error, no bills found") 
    else:
        for i in range(len(data[0])):
            print('{:<20} {:^12}'.format(data[0][i],data[1]))
   


def Bills_in_Order_of_Date(bills):
    """Produces a report that shows bills arranged by date,
    it does this with complexity O(n) as this is the complexity of the function
    'order_bills_by_date(bills)' which this function calls upon"""
    #Gets the sorted bills matrix from the function 'order_bills_by_date'#
    sorted_bills=order_bills_by_date(bills)
    #Displays Title and column headings#
    print('\n'+'{:^90}'.format('Bills in Order of Date')
           +'\n'+'='*90
           +'\nProvider\t\tCustomer\t  Date (YYYY/MM/DD)  \tAmount  \tType'
           +'\n'+'-'*90)
    #Prints out the sorted bills#
    for line in sorted_bills:
        print("{:20s}\t{:20s}{}\t\t{}\t\t{:20s}".format(
                                      str(line[0]), 
                                      line[1],
                                      date(line[2],line[3],line[4]),
                                      line[5],
                                      line[6]))




def Highest_Debit_and_Credit_Report(bills):  
    """"Producing a report to show highest debit and credit values
    it does this with complexity O(n) as this is the complexity of the functions
     which this function calls upon"""
    print('\n'+'{:^31}'.format('Highest Debit and Credit Report')
           +'\n'+'='*31)
    print('{}\t\t{}'.format('Debit/Credit','Value')
           +'\n'+'-'*31)
    highest_debit_value = highest_debit(bills)
    highest_credit_value = highest_credit(bills)
    #Print Report#
    print('Debit\t\t\t{}\nCredit\t\t\t{}'.format(highest_debit_value,highest_credit_value))




def Company_Success_Report(bills):
    """Produces a report showing how successful each company is,
  by displaying the total number of bills, it does this with complexity O(n) 
  as its runtime is dependant on the number of bills"""
    #Print the Title and column headings##
    print('\n'+'{:^45}'.format('Company Success Report')
           +'\n'+'='*45
           +'\n{}\t\t{}'.format('Utility Company','Number of Bills')
           +'\n'+'-'*45)
    #Scans through bills and gets all providers#
    providers = []
    for line in bills:
       provider = line[0]
       providers.append(provider)
    #Scans through to find the number of bills to each provider#
    provider_number_bills = []
    for provider in providers:
       provider_number_bills.append(providers.count(provider))
    #Forms a list with providers matched to their number of bills#
    #Use dict to get providers matched with their bills and then convert it#
    #back to a list, therefore using dict just to format the data in the list#
    matched = list(zip(providers, provider_number_bills))
    matched = list(dict.fromkeys(matched))
    matched.reverse()
    #Prints number of bills for each provider#
    for n in range (0 , (len(matched))):
        print("{:<20} {:^18}".format(matched[n][0], matched[n][1]))
  



def Average_Spend_per_Period_of_Time_Report(bills):
    """	Produces a report of average spend for a period (month/year) 
     as chosen by the user, it does this with complexity O(n) as its runtime
     is dependant on the the number of bills"""
    #Scan through bills, add debits and subtract credits from the the spend variable#
    spend = 0.0
    for bill in bills:
        if bill[6] == 'debit':
            spend += bill[5]
        else:
            spend -= bill[5]
    #Use the datetime list produced by the dates function#
    list_of_dates = []
    dates(list_of_dates)
    #Work out the length of time between the highest and lowest date
    time = max(list_of_dates)-min(list_of_dates)
    #This is in days#
    time = time.days
    #Convert days into years and months
    years = time/ 365
    months = years*12
    #Error handling for zero division error
    if years== 0 or months == 0:
        raise ZeroDivisionError('Cannot have 0 months or years')
    #Getting averages#
    average_spend_year = spend/years
    average_spend_month = spend/months
    #Get input on period#
    month_or_year = None
    while month_or_year == None:
        try:
            month_or_year = int(get_input('\nWould you like to see the average spend per year'
                             +' or per month?\n\n1. Year\n2. Month'+'\n3. Both\n\nPlease choose option: '))
            if month_or_year == 1:
                print('\n'+'{:^34}'.format('Average Spend per Period of Time')
                  +'\n'+'='*34
                  +'\n  {}\t{}'.format('Period','Average Spend')
                  +'\n'+'-'*34
                  +'\n  {}\t\t{}'.format('Year',round(average_spend_year,2)))
            elif month_or_year == 2:
                print('\n'+'{:^34}'.format('Average Spend per Period of Time')
                      +'\n'+'='*34
                      +'\n  {}\t{}'.format('Period','Average Spend')
                      +'\n'+'-'*34
                      +'\n  {}\t\t{}'.format('Month',round(average_spend_month,2)))
            elif month_or_year == 3:
                print('\n'+'{:^34}'.format('Average Spend per Period of Time')
                          +'\n'+'='*34
                          +'\n  {}\t{}'.format('Period','Average Spend')
                          +'\n'+'-'*34
                          +'\n  {}\t\t{}'.format('Year',round(average_spend_year,2))
                          +'\n  {}\t\t{}'.format('Month',round(average_spend_month,2)))
            else:
                print('Invalid Option, Please Try Again ')
        except ValueError:   
            print('Invalid Option, Please Try Again')
            month_or_year=None

       
   


 
def Average_Time_Between_Bills(bills):
    """"Produces a report of the average time between bills, it does this with
    complexity O(n) as this is the complexity of the function
    "average_time_between_bills(bills)" which this function calls """ 
    #Use previous function#
    average_time = average_time_between_bills(bills)
    #Printing the report#
    print('\n'+'{:^35}'.format('Average Time Between Bills Report')
          +'\n'+'='*35
          +'\n'+'-'*35
          +'\n  {}\t{}'.format('Average Time (Days) :',round(average_time,2)))

    
    

def Read_T_C():
    """Produces the terms and conditions report, it does this with complexity
    O(n) as its runtime is dependant on the number of lines in the t&c's"""  
    print('\n'+'{:^68}'.format('Terms and Conditions')
           +'\n'+'='*68
           +'\n'+'-'*68)
    #Reads lines from terms.txt
    for line in open ('terms_and_conditions.txt'):
        print(line.strip('\n')) 
 
    

    


def choose_report():
    """Function for getting choice for report menu, the complexity here is
    O(1) as it is dependant only on inputs"""
    print('\n{:^42s}'.format('Report Menu') 
          +'\n'+'='*42+'\n1. Yearly Report\n2. Most Popular Company Report'
          +'\n3. Bills in Order of Date\n4. Highest Debit and Credit Report\n5.'
          +' Company Success Report\n6. Average Spent per Period of Time Report\n7.'
          +' Average Time Between Bills\n8. Return to Main Menu')
    return get_input("\nPlease choose a report: ")


def view_reports(bills):
    """Function for viewing report menu, the complexity here is O(n^2) as this
    is the complexity of the function with the highest complexity which this
    function calls upon"""
    chosen_report=choose_report()
    while chosen_report!="8":
        if chosen_report == "1":
            Yearly_Report(bills)
        elif chosen_report == "2":
            Most_Popular_Company_Report(bills)
        elif chosen_report == "3":
            Bills_in_Order_of_Date(bills)
        elif chosen_report == "4":
            Highest_Debit_and_Credit_Report(bills)
        elif chosen_report == "5":
            Company_Success_Report(bills)
        elif chosen_report == "6":
            Average_Spend_per_Period_of_Time_Report(bills)
        elif chosen_report == "7":
            Average_Time_Between_Bills(bills)
        elif chosen_report=="8":
            print("Thank you for using Utility Bills Management System"+
                  ", have a nice day")
        else:
            print("Invalid choice, please try again")
        chosen_report=choose_report()











####################### Error Handling Functions #############################

"""The complexity of all functions in this error handling section will be O(1)
as they are all just dependant on inputs from the user """

def get_input(text):
    """This function will be used for input fuctions which are being tested
    ie any function which uses the input function, will instead use this function
    so the functions can be properly unit tested"""
    return input(text)

def provider_error():
    """Error handling for entry of provider"""
    #Using the try statement in the opposite of how it is meant to be used#
    #For a correct entry a value error is raised so the except block is executed#
    #This allows me to use try and excpet statement to check if the
    #type of the entry is correct instead of just using an if statement#
    provider = None
    while provider== None:
        try:
            provider= str.capitalize(get_input("\nPlease enter the Utility Company: "))
            if provider == "":
                provider = None
            int(provider)
            print("\nInvalid Utility Company, please try again ")
            provider = None
        except ValueError:
            continue
        except TypeError:
            print("\nInvalid Utility Company, please try again ")
    return provider


def customer_error():
    """Error handling for customer"""
    #Same idea as last function#
    customer = None
    while customer== None:
        try:
            customer=(get_input("\nPlease enter the customers full name: "))
            int(customer)
            print("\nInvalid name, please try again ")
            customer = None
        except ValueError:
            customer=customer.split()  #Splits name into first and surname#
            if len(customer) ==2:  #Makes first letter of each a capital#
                customer[0]=str.capitalize(customer[0])
                customer[1]=str.capitalize(customer[1])
                customer=customer[0]+" "+ customer[1]
            else: #If more than first and surname entered#
                print("\nInvalid entry, please enter the customers first name and surname")
                customer = None
    return customer
        
    
def year_error():
    """Error handling for entry of year"""
    year = None
    while year == None:
        try:
            year= int(get_input('\nPlease enter the year: '))
            if year>2021 or year<1946: #Ensures year is within a possible range#
                print('Invalid Year, please try again')
                year = None
            
        except ValueError: #Picks up value error#
            print('\nInvalid Year, please try again.')
            year = None
    return year


def day_error(month,year):
    """"Error handling for entry of day"""
    #Works out last day of entered month using previous function#
    last_day_in_month=last_day_of_month(month,year)
    day = None
    while day == None:
        try:
            day= int(get_input('\nPlease enter the day (number): '))
            if day<1 or day>last_day_in_month: #Ensures year is within a possible range#
                print('Invalid day, please try again')
                day = None
                
        except ValueError: #Picks up value error#
            print('\nInvalid day, please try again.')
            day = None 
    return day



def month_error():
    """Error handling for entry of month"""
    month = None
    while month == None:
        try:
            month= int(get_input('\nPlease enter the month (1-12): '))
            if month<1 or month>12: #Ensures year is within a possible range#
                print('\nInvalid month, please try again')
                month = None
                
        except ValueError: #Picks up value error#
            print('\nInvalid month, please try again.')
            month = None
    return month



def amount_error():
    """"Error handling for entry of amount"""
    amount = None
    while amount == None:
        try:
            amount= float(get_input('\nPlease enter the bill amount (2 d.p.): '))
            if amount<=0 or amount>= 50000: #Ensures bill is within sensible range#
                print('\nInvalid amount, please try again')
                amount = None
                
        except ValueError: #Picks up value error#
            print('\nInvalid amount, please try again.')
            amount = None

    return amount


def debit_or_credit_error():
    """"Error handling for entry of debit/credit"""
    debit_or_credit = None
    while debit_or_credit is None:
        
        debit_or_credit = get_input('\nIs the bill debit or credit: ')
        #Ensures the entry is either "debit" or "credit"#  
        if debit_or_credit!="debit" and debit_or_credit != "credit":
            print("\nInvalid Entry. Please try again")
            debit_or_credit=None
    return debit_or_credit
    



################## Main Function which runs all others########################

def main_function():
    """"Main function which runs and controls all other functions,
    the complexity here would be O(n^2) as this is the highest complexity of
    the functions which this function calls"""
    #Reads bills from the csv#
    bills = read_from_csv()
    #Prints a Greeting#
    print("-"*50+'\n{:^50s}\n'.format('Welcome to the Utility Billing Management System')
          +"-"*50)
    choice= chosen_option()
    #process the choice
    while choice != '5':
        if choice == "1":
           bills_viewer(bills)
        elif choice == "2":
            gather_new_data(bills)
        elif choice == "3":
            view_reports(bills)
        elif choice == "4":
            Read_T_C()
        else:
            print('Invalid Option, please try again')
        #display menu and ask for user choice
        choice = chosen_option()
        
    write_new_bill(bills) 
    #Goodbye Message#
    print("\nThank you for using the Utility Bill Management System.\n"
          +"Have a nice day!")

#File is executed when ran directly#
if __name__ == '__main__':
    main_function()
