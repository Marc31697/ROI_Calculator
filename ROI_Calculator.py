# Income - Different kinds of income - track total income (Rental, Laundry, Storage, Misc)

# Expenses - Tax, Insurance, Utilities (Electric, Water, Sewer, garbage, gas), HomeOwner Association, Lawn/Snow, Vacancy, Repairs, Capital Expenditures (cont.)
# Property Managment, Mortgage - Some expenses may be handled by renter (Utilities, Lawn/Snow, HoA) - Set 5% of rental income aside for vacancy
# Estimate $100 a month for repairs, CapEx - Property manager 10% of rental income - ****Research Mortgage Payments****

# Cash Flow - (Income - Expenses) = Total Monthly Cash Flow

# Cash on Cash Return on Investment - Down Payment, Closing Costs, Rehab budget, Misc = Total Investment
# ROI = Annual Cash Flow / Total Investment (turn value into a percentage)

class property():

    def __init__(self, income = {}, expenses = {}, investment = {}):
        self.income = income
        self.expenses = expenses
        self.investment = investment

    def enterIncome(self):
        # Ask if they would like to enter their total income in one step
        response = input('\nWould you like to enter your income as a whole or categorized?: ')
        if response.lower() == 'yes':
            response = input('\nEnter Total Income: ')
            self.income['Total Income'] = response
            return self.income

        # Rental
        response = input('\nEnter Rental Income: ')
        self.income['Rental'] = response

        # Laundry
        response = input('\nWill you be receiving Laundry income? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('\nWhat will the income amount be?: ')
            self.income['Laundry'] = response

        # Storage
        response = input('\nWill you be receiving Storage income? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('\nWhat will the income amount be?: ')
            self.income['Storage'] = response

        # Misc
        response = input('\nAre there any other types of income you would like to include here? (Yes/No): ')
        if response.lower() == 'yes':
            while True:
                response = input("\nEnter the name of the income expense or enter to keep this as Misc: ")
                if response.lower() == '':
                    response = input('\nWhat is the income amount?: ')
                    self.income['Misc'] = response
                
                else:
                    response = input('\nWhat will the income source be?: ')
                    self.income[response] = 0
                    responseTwo = input('\nWhat will the income amount be?: ')
                    self.income[response] = responseTwo
                break

    def retrieveIncome(self):
        print('\n')
        for key,value in self.income.items():
            print(f'{key}: {value}')
    
    def enterExpenses(self):
        # Ask if they would like to enter their total expenses in one step
        response = input('\nWould you like to enter your expenses as a whole or categorized?: ')
        if response.lower() == 'yes':
            response = input('\nHow much are the total expenses?: ')
            self.expenses['Total Expenses'] = response
            return self.expenses
        
        # Tax
        response = input("\nEnter Tax Rate: ")
        self.expenses['Tax'] = response

        # Insurance
        response = input('\nEnter Insurance Rate: ')
        self.expenses['Insurance'] = response

        # Utilities
        response = input("\nWill you be paying for utilities? (Yes/No): ")
        if response.lower() == 'yes':
            self.expenses['Utilities'] = {}
            while True:
                response = input("\nEnter the name of the utility expense (Electric/Water/Sewer/Garbage/Gas/Other): ")
                self.expenses['Utilities'][response.title()] = 0

                responseTwo = input("\nEnter the expense amount: ")
                self.expenses['Utilities'][response.title()] = [responseTwo]

                response = input('\nPress 1 to enter another utility or 0 to enter other expenses: ')
                if response == '0':
                    break
        
        # Home Owners Association
        response = input("\nWill you need to pay Home Owner's associaton fees? (Yes/No): ")
        if response.lower() == 'yes':
            response = input('\nHow much will the fee be?: ')
            self.expenses["HoA"] = response

        # Lawn/Snow
        response = input("\nWill you need to pay for lawn/snow care fees? (Yes/No): ")
        if response.lower() == 'yes':
            response = input('\nHow much will the fee be?: ')
            self.expenses["Lawn/Snow"] = response

        # Vacancy
        response = input("\nWould you like to modify the vacancy percentage? (Standard is %5, Yes/No): ")
        if response.lower() == 'yes':
            response = input('\nWhat would you like to set it to?: ')
            self.expenses["Vacancy"] = response
        else:
            self.expenses["Vacancy"] = '5%'

        # Repairs & CapEx
        response = input('\nRepair Costs: ')
        self.expenses['Repairs'] = response

        response = input('\nCapital Expenditures(CapEx): ')
        self.expenses['CapEx'] = response

        # Property Management
        response = input('\nWill you be using a property manager? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('\nEnter Fee: ')
            self.expenses['Property Management'] = response

        # Mortgage
        response = input('\nEnter Mortgage Payments: ')
        self.expenses['Mortgage'] = response
        


    def retrieveExpenses(self):
        print('\n')
        for key,value in self.expenses.items():
            if key == 'Utilities':
                print('Utilities:')
                for i,k in self.expenses[key].items():
                    print(f'  {i}: {"".join(k)}')
            else:
                print(f'\n{key}: {value}')


    def enterInvestment(self):
        # Ask if they would like to enter their total investment in one step
        response = input('\nWould you like to enter your investment as a whole or categorized?: ')
        if response.lower() == 'yes':
            response = input('\nHow much total investment will you be putting in?: ')
            self.investment['Total Investment'] = response
            return self.investment
        
        # Down Payment
        response = input("\nWhat will your down payment be?: ")
        self.investment['Down Payment'] = response

        # Closing Costs
        response = input('\nWhat will your closing costs be?: ')
        self.investment['Closing Costs'] = response
        
        # Rehab Budget
        response = input('\nWhat will your Rehab Budget be?: ')
        self.investment['Rehab Budget'] = response
        
        # Misc Investments
        x = 0
        while True:
            response = input('\nPlease enter any other remaining miscellaneous investments numbers to be included in your total investment (Press 0 at any time to stop): ')
            
            if response == '0':
                self.investment['Misc'] = str(x)
                break
            else:
                x += float(response.replace(',','').strip('$%'))
                
    def retrieveInvestment(self):
        print('\n')
        for key,value in self.investment.items():
            print(f'\n{key}: {value}')
            
    def calculate(self):
        total_Income = 0
        total_Expenses = 0
        total_Investment = 0
        
        # Total income
        for value in self.income.values():
            total_Income += float(value.replace(',','').strip('$%'))
        print(f'Your total monthly income is {total_Income}')
        
        # Total expenses
        for key, value in self.expenses.items():
            if key == 'Utilities':
                for x in self.expenses['Utilities'].values():
                    total_Expenses += float(x.strip('$,'))
            elif '%' in value and 'Insurance' in self.expenses.keys() and key == 'Vacancy':
                total_Expenses += float(value.replace(',','').strip('$%')) / 100 * float(self.income['Rental'].replace(',','').strip('$%'))
            elif '%' in value and 'Rental' in self.income.keys() and key == 'Property Management':
                total_Expenses += float(value.replace(',','').strip('$%')) / 100 * float(self.income['Rental'].replace(',','').strip('$%'))
            else:
                total_Expenses += float(value.replace(',','').strip('$%'))
        print(f'Your total monthly expenses are {total_Expenses}')
        
        # Obtain Annual Cash Flow
        annual_Cash_Flow = (total_Income - total_Expenses) * 12
        print(f'Your annual cash flow is {annual_Cash_Flow}')
        
        # Obtain Total Investment
        for value in self.investment.values():
            print(value.replace(',','').strip('$%'))
            total_Investment += float(value.replace(',','').strip('$%'))
        print(f'Your total investment is {total_Investment}')
        
        # Obtain ROI and return
        return_on_investment = annual_Cash_Flow / total_Investment * 100
        print(f'Here is your total Return on Investment: {return_on_investment}%')
        

    def tester(self):
        self.income = {'Rental' : '$2000.00',
        'Laundry' : '$0',
        'Storage' : '0',
        'Misc' : '0',
        'Testing' : '0'
        }
        
        self.expenses = {'Tax' : '$150.00',
        'Insurance' : '100',
        'Mortgage' : '$860.00',
        'Property Management' : '10%',
        'Vacancy' : '5%',
        'Repairs' : '100',
        'CapEx' : '100'
        }
        
        self.investment = {'Down Payment' : '$40,000',
        'Closing Costs' : '$3000',
        'Rehab Budget' : '$7000'}
        



def run():
    newHouse = property()

    # newHouse.tester()
    # newHouse.calculate()
    newHouse.enterIncome()
    newHouse.retrieveIncome()

    newHouse.enterExpenses()
    newHouse.retrieveExpenses()
    
    newHouse.enterInvestment()
    newHouse.retrieveInvestment()
    
    newHouse.calculate()

run()