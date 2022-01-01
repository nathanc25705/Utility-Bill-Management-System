import unittest
from unittest.mock import patch



from project_code import read_from_csv, most_popular_utility_company,\
    highest_debit, highest_credit, average_time_between_bills,\
        last_day_of_month,provider_error,customer_error,year_error,day_error,\
            month_error,amount_error,debit_or_credit_error,choose_report,\
                chosen_option,order_bills_by_date
                    


class Testbills(unittest.TestCase):
     
    #Checks function for expected output# 
    def test_most_popular_utility_company(self):
        bills = read_from_csv()
        self.assertEqual([['Energia','Vodafone'],2], most_popular_utility_company(bills))
     
    #Checks function for expected output# 
    def test_highest_debit(self):
        bills = read_from_csv()
        self.assertEqual(122.52, highest_debit(bills))
    #Checks function for expected output#   
    def test_highest_credit(self):
        bills = read_from_csv()
        self.assertEqual(11.58, highest_credit(bills))
    
    #Checks function for expected output# 
    def test_average_time_between_bills(self):
        bills = read_from_csv()
        self.assertEqual(47.5, average_time_between_bills(bills))
        
    #Checks function for expected output# 
    def test_last_day_of_month(self):
        month=2
        year=2020
        self.assertEqual(29,last_day_of_month(month,year))
    
    #Checks function for expected output when given input and checks error handling#
    @patch('project_code.get_input', return_value = 'Vodafone')
    def test_provider_error(self, input):
        self.assertEqual(provider_error(), 'Vodafone')
        self.assertRaises(Exception, provider_error, 1)
    
    #Checks function for expected output when given input and checks error handling#
    @patch('project_code.get_input', return_value = 'Abbie Fee')
    def test_customer_error(self, input):
        self.assertEqual(customer_error(), 'Abbie Fee')
        self.assertRaises(Exception, customer_error, 1)
        self.assertRaises(Exception, customer_error, 'Abbie F ee')
      
    #Checks function for expected output when given input and checks error handling#    
    @patch('project_code.get_input', return_value = 2021)
    def test_year_error(self, input):
        self.assertEqual(year_error(), 2021)
        self.assertRaises(Exception, year_error, 1800)
        self.assertRaises(Exception, year_error, 2022)
        self.assertRaises(Exception, year_error, 'b')
    
    #Checks function for expected output when given input and checks error handling#
    #Shows that 29th of february works in leap year#
    @patch('project_code.get_input', return_value = 29)
    def test_day_error(self, input):
        self.assertEqual(day_error(2,2020), 29)
        self.assertRaises(Exception, day_error, 0)
        self.assertRaises(Exception, day_error, 40)
        self.assertRaises(Exception, day_error, 'a')
      
    #Checks function for expected output when given input and checks error handling#    
    @patch('project_code.get_input', return_value = 7)
    def test_month_error(self, input):
        self.assertEqual(month_error(), 7)
        self.assertRaises(Exception, month_error, 0)
        self.assertRaises(Exception, month_error, 13)
        self.assertRaises(Exception, month_error, 'a')
        
    #Checks function for expected output when given input and checks error handling#
    @patch('project_code.get_input', return_value = 42.50)
    def test_amount_error(self, input):
        self.assertEqual(amount_error(), 42.50)
        self.assertRaises(Exception, amount_error, -1)
        self.assertRaises(Exception, amount_error, 52000)
        self.assertRaises(Exception, amount_error, 'a')
        
    #Checks function for expected output when given input and checks error handling#
    @patch('project_code.get_input', return_value = 'debit')
    def test_debit_or_credit_error(self, input):
        self.assertEqual(debit_or_credit_error(), 'debit')
        self.assertRaises(Exception, debit_or_credit_error, 1)
        self.assertRaises(Exception, debit_or_credit_error, 'a')
    
    #Checks functions error handling for incorrect inputs#
    def test_choose_report(self):
        self.assertRaises(Exception, choose_report, 'a')
        self.assertRaises(Exception, choose_report, 20)
    
    #Checks functions error handling for incorrect inputs#
    def test_chosen_option(self):
        self.assertRaises(Exception, chosen_option, 'a')
        self.assertRaises(Exception, choose_report, 0)
    
    #Acending Order test#
    #Checks if the first bill is newer than the following and repeats this#
    #If this is true, check is set equal to True and the unit test checks this#
    @patch('project_code.get_input', return_value = '1')
    def test_order_bills_by_date_asc(self,input):
        bills=read_from_csv()
        dates_in_order=[]
        sorted_bills = order_bills_by_date(bills)
        for i in range(len(bills)):
            dates_in_order.append(sorted_bills[i][7])
        for n in range(len(dates_in_order)-1):
            if dates_in_order[n]>dates_in_order[n+1]:
                check=True
        self.assertEqual(check,True)
        
    #Descending Order test#
    #Checks if the first bill is newer than the following and repeats this#
    #If this is true, check is set equal to True and the unit test checks this#
    @patch('project_code.get_input', return_value = '2')
    def test_order_bills_by_date_dsc(self,input):
        bills=read_from_csv()
        dates_in_order=[]
        sorted_bills = order_bills_by_date(bills)
        for i in range(len(bills)):
            dates_in_order.append(sorted_bills[i][7])
        for n in range(len(dates_in_order)-1):
            if dates_in_order[n]<dates_in_order[n+1]:
                check=True
        self.assertEqual(check,True)

    
#File is executed when ran directly#
if __name__ == '__main__':
    unittest.main()