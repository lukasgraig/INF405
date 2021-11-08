from state import StateTuitionCalc
from us import USTuitionCalc

def main():
    i = StateTuitionCalc('us_avg_tuition.csv')
    w = USTuitionCalc('us_avg_tuition.csv')
    i.state_select('Alabama')
    i.average_tuition_cost()
    for x in range(1):
        i.average_rise()
        i.one_year_prediction()
        i.two_year_prediction()

    w.two_year_us_prediction()

    

if __name__ == '__main__':
    main()