# Income - Different kinds of income - track total income (Rental, Laundry, Storage, Misc)

# Expenses - T̶a̶x̶,̶ I̶n̶s̶u̶r̶a̶n̶c̶e̶,̶ U̶t̶i̶l̶i̶t̶i̶e̶s̶ (̶E̶l̶e̶c̶t̶r̶i̶c̶,̶ W̶a̶t̶e̶r̶,̶ S̶e̶w̶e̶r̶,̶ g̶a̶r̶b̶a̶g̶e̶,̶ g̶a̶s̶)̶,̶ HomeOwner Association, Lawn/Snow, Vacancy, Repairs, Capital Expenditures (cont.)
# Property Managment, Mortgage - Some expenses may be handled by renter (Utilities, Lawn/Snow, HoA) - Set 5% of rental insurance aside for vacancy
# Estimate $100 a month for repairs, CapEx - Property manager 10% of rental income - ****Research Mortgage Payments****

# Cash Flow - (Income - Expenses) = Total Monthly Cash Flow

# Cash on Cash Return on Investment - Down Payment, Closing Costs, Rehab budget, Misc = Total Investment
# ROI = Annual Cash Flow / Total Investment (turn value into a percentage)

class property():

    def __init__(self, income = {}, expenses = {}):
        self.income = income
        self.expenses = expenses

    def enterIncome(self):
        # Rental
        response = input('How much rental income will you be receiving?: ')
        self.income['Rental'] = response

        # Laundry
        response = input('Will you be receiving Laundry income? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('What will the income amount be?: ')
            self.income['Laundry'] = response

        # Storage
        response = input('Will you be receiving Storage income? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('What will the income amount be?: ')
            self.income['Storage'] = response

        # Misc
        response = input('Are there any other types of income you would like to include here? (Yes/No): ')
        if response.lower() == 'yes':
            while True:
                response = input("\nEnter the name of the income expense or enter to keep this as Misc: ")
                if response.lower() == '':
                    response = input('What is the income amount?: ')
                    self.income['Misc'] = response
                
                else:
                    response = input('What will the income source be?: ')
                    self.income[response] = 0
                    responseTwo = input('What will the income amount be?: ')
                    self.income[response] = responseTwo
                break

    def retrieveIncome(self):
        for key,value in self.income.items():
            print(f'{key}: {value}')
    
    def enterExpenses(self):
        # Tax
        response = input("\nWhat will your tax rate be?: ")
        self.expenses['Tax'] = response

        # Insurance
        response = input('\nWhat will your insurance rate be?: ')
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
        response = input('\nHow much would you like to put aside for repairs?: ')
        self.expenses['Repairs'] = response

        response = input('\nHow much would you like to put aside for Capital Expenditures?: ')
        self.expenses['CapEx'] = response

        # Property Management
        response = input('\nWill you be using a property manager? (Yes/No): ')
        if response.lower() == 'yes':
            response = input('\nHow much will the fee be?: ')
            self.expenses['Property Management'] = response

        # Mortgage
        response = input('\nHow much will the mortgage be?: ')
        self.expenses['Mortgage'] = response
        


    def retrieveExpenses(self):
        for key,value in self.expenses.items():
            if key == 'Utilities':
                print('Utilities:')
                for i,k in self.expenses[key].items():
                    print(f'  {i}: {"".join(k)}')
            else:
                print(f'{key}: {value}')

    def calculate(self):
        pass
        total_Income = 0
        total_Expenses = 0
        # Total income
        for value in self.income.values():
            total_Income += float(value.strip('$,'))
        print(total_Income)

    def tester(self):
        self.income = {'Rental' : '$50.00',
        'Laundry' : '$25.0',
        'Storage' : '14.25',
        'Misc' : '$15.00'
        }



def run():
    newHouse = property()

    newHouse.tester()
    newHouse.calculate()
    # newHouse.enterIncome()
    # newHouse.retrieveIncome()

    # newHouse.enterExpenses()
    # newHouse.retrieveIncome()
    

run()