''' This program will read in 3 data files and correctly organize them so users can 
see what states and counties wore masks the most and which ones didn't '''

class Data:
    def __init__(self):
        self.fips_codes = {}
        self.state_codes = {}
        self.query_states = {} 

        self.read_data()
        self.query()

    # This method is used to read in the data and add it accordingly to the correct dictionary
    def read_data(self):
        with open('mask-use-by-county.csv', 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                self.fips_codes[array[0]] = [array[1], array[2], array[3], array[4], array[5]]
            f.close()

        with open('State_Abbreviations.csv', 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                self.state_codes[array[1]] = [array[0]]
            f.close()

        with open('state-geocodes-v2018.csv', 'r') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                for key in self.state_codes:
                    if array[6] in self.state_codes[key]:
                        self.state_codes[key].append(array[1])
            f.close()

    # Method used to query specific state data that is requested by the user
    def state_query(self, code=''):
        try:
            state_data = self.query_states.get(code)
            best_mask = state_data[5]
            worst_mask = state_data[6]

            print(f"\nNever = {state_data[0]:.2f}%, Rarely = {state_data[1]:.2f}%, Sometimes = {state_data[2]:.2f}%, Frequently = {state_data[3]:.2f}%, Always = {state_data[4]:.2f}%")
            print(f"County {best_mask[0]} has the best mask wearing rate with {best_mask[1]:.2f}%")
            print(f"County {worst_mask[0]} has the worst mask wearing rate with {worst_mask[1]:.2f}%\n")
        except:
            print(f"{code} -> State code was not found")

    # Method is used to calculate whole us data
    def nationwide_query(self):

        loop = 0
        never = 0
        rarely = 0
        sometimes = 0
        frequently = 0
        always = 0

        for value in self.fips_codes.values():
            never += float(value[0])
            rarely += float(value[1])
            sometimes += float(value[2])
            frequently += float(value[3])
            always += float(value[4])
            loop += 1
        print(f"US AVERAGES | Never = {(never/loop) * 100:.2f}%, Rarely = {(rarely/loop) * 100:.2f}%, Sometimes = {(sometimes/loop) * 100:.2f}%, Frequently = {(frequently/loop) * 100:.2f}%, Always = {(always/loop) * 100:.2f}%")

        print("\nState\t | \tNever\t\tRarely\t\tSometimes\tFrequently\tAlways")
        current_best = [None, 0]
        current_worst = [None, 0]
        for state in self.query_states.keys():
            state_data = self.query_states.get(state)

            best_state = ((float(state_data[3]) + float(state_data[4])) / 2)
            if best_state  > current_best[1]:
                current_best[0] = state
                current_best[1] = best_state

            worst_state = ((float(state_data[0]) + float(state_data[1])) / 2)
            if worst_state > float(current_worst[1]):
                current_worst[0] = state
                current_worst[1] = worst_state

            print(f"{state}\t | \t{state_data[0]:.2f}%\t \t{state_data[1]:.2f}%\t \t{state_data[2]:.2f}%\t \t{state_data[3]:.2f}%\t \t{state_data[4]:.2f}%\nBest county mask wearing rate is {state_data[5][0]} with {state_data[5][1]:.2f}% and the Worst county mask wearing rate is {state_data[6][0]} with {state_data[6][1]:.2f}%\n")

        print(f"Best mask wearing state is {current_best[0]} with {current_best[1]:.2f}% and the Worst mask wearing state is {current_worst[0]} with {current_worst[1]:.2f}%\n")

    # Method that calculates state data that has the same county code and calculates it then inserts it into a dictionary 
    # with the corresponding state code 
    def query(self):
        states = []

        for state_id in self.state_codes.keys():
            states.append(state_id)

        for code in states:
            state_code = self.state_codes[code]

            never = 0
            rarely = 0
            sometimes = 0
            frequently = 0
            always = 0
            loop = 0

            best_mask = [0,0]
            worst_mask = [0,0]

            for i in self.fips_codes.keys():

                if i[:2] == state_code[1]:
                    value = self.fips_codes.get(i)

                    bm = ((float(value[3]) + float(value[4]))/2) * 100
                    wm = ((float(value[0]) + float(value[1]))/2) * 100

                    if bm > best_mask[1]:
                        best_mask[0] = i
                        best_mask[1] = bm

                    if wm > worst_mask[1]:
                        worst_mask[0] = i
                        worst_mask[1] = wm

                    never += float(value[0])
                    rarely += float(value[1])
                    sometimes += float(value[2])
                    frequently += float(value[3])
                    always += float(value[4])
                    loop += 1
            try:
                never = (never/loop) * 100
                rarely = (rarely/loop) * 100
                sometimes = (sometimes/loop) * 100
                frequently = (frequently/loop) * 100
                always = (always/loop) * 100

                self.query_states[code] = [never, rarely, sometimes, frequently, always, best_mask, worst_mask]
            except ZeroDivisionError:
                pass

def main():
    d = Data()

    while True:
        print("Commands: 1 - Nationwide data, 2 - State data, 3 - Quit")
        user = int(input("Enter number: "))

        if user == 1:
            d.nationwide_query()
        elif user == 2:
            code = input("Please enter state two-letter code: ").upper()
            d.state_query(code)
        elif user == 3:
            exit(0)
        else:
            print("Invalid Command")

main() 