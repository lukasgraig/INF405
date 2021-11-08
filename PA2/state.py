from data import Data

class StateTuitionCalc(Data):
    def __init__(self, filename):
        super().__init__(filename)
        self.state_data = []
        self.state = None
        self.avg_rise = 0

    def state_select(self, state):
        '''This function handles the state the user selects and cleans the data'''
        self.state_data = super().get_state_data(state)
        self.state = state


    def average_tuition_cost(self):
        '''A method to calculate the average tuition costs for the years given'''
        loop_count = 0
        total = 0
        for i in self.state_data:
            loop_count += 1
            total += i

        avg = total / loop_count
        print(f"The average cost to attend a school in {self.state} is ${avg:.2f}")

    def average_rise(self):
        '''A method to calculate the average rise in tuition for the years given'''
        dif_list = []
        total = 0
        previous = 0
        for x in self.state_data: # For loop to get the differences from year to year then adds to a list
            total = x - previous
            previous = x
            dif_list.append(total)

        dif_total = 0
        for count, x in enumerate(dif_list[1:]):
            dif_total += x

        self.avg_rise = dif_total / count
        print(f'The average rise in tuition for each year in {self.state} is ${self.avg_rise:.2f}')


    def one_year_prediction(self):
        '''A calculation to predict what the upcoming tuition rate will be in one year'''
        tuition_rise = self.state_data[11] - self.state_data[10]
        one_year_rise = self.avg_rise + tuition_rise

        oyp_final = self.state_data[11] + one_year_rise
        self.state_data.append(oyp_final)
        print(f'The one year prediction in {self.state} is ${oyp_final:.2f}')


    def two_year_prediction(self):
        '''A calculation to predict what the upcoming tuition rate will be in two years'''
        tuition_rise = self.state_data[12] - self.state_data[11]
        average = (self.state_data[12] + self.state_data[11] + self.state_data[10]) / 3

        typ_final = 0
        for count, cost in enumerate(self.state_data):
            typ_final += cost

        typ_final = typ_final / count
        final_pred = (typ_final + average) / 2 + tuition_rise

        print(f'The two year prediction in {self.state} is ${final_pred:.2f}')
