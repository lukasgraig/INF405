from typing import final
from data import Data

class USTuitionCalc(Data):
    def __init__(self, filename):
        super().__init__(filename)
        self.final_avg = 0
        self.all_states = {}
        self.get_all_data()

    def get_all_data(self):
        self.all_states = super().get_all_data()

    def average_us_tuition(self):
        avg_state_tuition = {}
        for state in self.all_states:
            state_avg = 0
            loop = 0
            for data in self.all_states.get(state):
                state_avg += data
                loop += 1
            final_avg = state_avg / loop
            avg_state_tuition[state] = final_avg

        loop = 0
        avg = 0
        for x in avg_state_tuition.values():
            avg += x
            loop += 1

        final_avg = avg/loop
        print(f'The average tuition rate in the US is ${final_avg:.2f}')

    def average_us_rise(self):
        final_dif_list = [] 

        for state in self.all_states:
            total = 0
            previous = 0
            hold_data = []

            for data in self.all_states.get(state): # For loop to get the differences from year to year then adds to a list
                total = data - previous
                previous = data
                hold_data.append(total)
            
            dif_total = 0
            for count, x in enumerate(hold_data[1:]):
                dif_total += x

            avg_rise = dif_total / count
            final_dif_list.append(avg_rise)
        
        final = 0
        for count, x in enumerate(final_dif_list):
            final += x

        self.final_avg = final/count
        print(f'The average tutition price rise in the US is ${self.final_avg:.2f}')

    def one_year_us_prediction(self):
        
        last_year_tr = 0 # Last year tuition rate 
        tr_list = [] # Holds the difference for the last year for all states
        loop = 0
        for state in self.all_states:
            state_tr = self.all_states.get(state)
            last_year_tr += state_tr[11]
            tuition_rise = state_tr[11] - state_tr[10]
            tr_list.append(tuition_rise)
            loop += 1

        oy_avg = 0     
        for count, x in enumerate(tr_list):
            oy_avg += x   

        avg = oy_avg/ count
        last_year_tr = last_year_tr / loop 
        oy_final = last_year_tr + avg
        print(f'The prediction tuition rate one year out in the US is ${oy_final:.2f}')

    def two_year_us_prediction(self):
        last_year_tr = 0 # Last year tuition rate 
        tr_list = [] # Holds the difference for the last year for all states
        loop = 0
        for state in self.all_states:
            state_tr = self.all_states.get(state)
            last_year_tr += state_tr[11]
            tuition_rise = state_tr[11] - state_tr[10]
            tr_list.append(tuition_rise)
            loop += 1

        oy_avg = 0     
        for count, x in enumerate(tr_list):
            oy_avg += x   

        avg = oy_avg/ count
        last_year_tr = last_year_tr / loop 
        oy_final = last_year_tr + avg

        prev_year = 0 # Holds the value of 2015-16 for all schools combined
        sec_year = 0  # Holds the value of 2014-15 for all schools combined
        for state in self.all_states:
            x = self.all_states.get(state)
            prev_year += x[11]
            sec_year += x[10]

        tuition_rise = oy_final - (prev_year / 50)

        average = (oy_final + (prev_year / 50) + (sec_year / 50)) / 3

     
        final_pred = tuition_rise + average
        print(f'The prediction tuition rate two years out in the US is ${final_pred:.2f}')

