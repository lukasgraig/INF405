from state import StateTuitionCalc
from us import USTuitionCalc

def main():
    i = StateTuitionCalc('us_avg_tuition.csv')
    w = USTuitionCalc('us_avg_tuition.csv')
    

    while True:
            userInput = input("Please enter the state name (i.e. Alabama), 'All' for all US data or 'Exit' to quit: ").title()

            if userInput != 'All' and userInput != 'Exit': 
                i.state_select(userInput)
                i.average_rise()

                while True:
                    choice = int(input('Type 1 for Average state tuition calculation\n     2 for the state average rise\n     3 for the state one year prediction\n     4 for state two year prediction calculation\n     5 to Exit\nSelection: '))

                    if choice == 1:
                        i.average_tuition_cost()
                    elif choice == 2:
                        i.get_average_rise()
                    elif choice == 3:
                        i.one_year_prediction()
                    elif choice == 4:
                        i.two_year_prediction()
                    elif choice == 5:
                        break
                    else:
                        print('Invalid choice')

            elif userInput == 'All' or userInput != 'Exit':
                print('shit stain')
                while True:
                    uschoice = int(input('Type 1 for Average US tuition calculation\n     2 for the US tuition average rise\n     3 for the US one year prediction\n     4 for US two year prediction calculation\n     5 to Exit\nSelection: '))

                    if uschoice == 1:
                        w.average_us_tuition()
                    elif uschoice == 2:
                        w.average_us_rise()
                    elif uschoice == 3:
                        w.one_year_us_prediction()
                    elif uschoice == 4:
                        w.two_year_us_prediction()
                    elif uschoice == 5:
                        break
                    else:
                        print('Invalid choice')

            elif userInput == 'Exit':
                exit(0)

if __name__ == '__main__':
    main()