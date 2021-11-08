import csv

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.states = {} 

        self.read_data(self.filename)

    def read_data(self, filename):
        with open(filename , newline='') as csvfile:
            data_file = csv.reader(csvfile)
            next(data_file)    # Removes first line of the file
            for row in data_file:
                self.states[row[0]] = [x[1:] for x in row[1:]] # Adds the items to the dictionary

    def get_all_data(self):
        return self.states 

    def get_state_data(self, state):
        if state in self.states:
            state_data_list = self.states.get(state)
            return state_data_list
