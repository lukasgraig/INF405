''' This program will read in 3 data files and correctly organize them so users can 
see what states and counties wore masks the most and which ones didn't '''

class Data:
    def __init__(self):
        self.fips_codes = {}
        self.state_codes = {}

        self.read_data()

    # This method is used to read in the data and add it accordingly to the correct dictionary
    def read_data(self):
        with open('mask-use-by-county.csv') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                self.fips_codes[array[0]] = [array[1], array[2], array[3], array[4], array[5]]
            f.close()

        with open('State_Abbreviations.csv') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                self.state_codes[array[1]] = [array[0]]
            f.close()

        with open('state-geocodes-v2018.csv') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                array = line.split(',')
                for key in self.state_codes:
                    if array[6] in self.state_codes[key]:
                        self.state_codes[key].append(array[1])
            f.close()

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
        
        print(f"Never = {(never/loop) * 100:.2f}%, Rarely = {(rarely/loop) * 100:.2f}%, Sometimes = {(sometimes/loop) * 100:.2f}%, Frequently = {(frequently/loop) * 100:.2f}%, Always = {(always/loop) * 100:.2f}%")

    def state_query(self, code=''):
        
        loop = 0
        never = 0
        rarely = 0
        sometimes = 0
        frequently = 0
        always = 0

        best_mask = [0,0]
        worst_mask = [0,0]

        try:
            if self.state_codes.fromkeys(code):
                state_code = self.state_codes[code]
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

            print(f"Never = {(never/loop) * 100:.2f}%, Rarely = {(rarely/loop) * 100:.2f}%, Sometimes = {(sometimes/loop) * 100:.2f}%, Frequently = {(frequently/loop) * 100:.2f}%, Always = {(always/loop) * 100:.2f}%")
            print(f"County {best_mask[0]} has the best mask wearing rate with {best_mask[1]:.2f}%")
            print(f"County {worst_mask[0]} has the worst mask wearing rate with {worst_mask[1]:.2f}%")
        except:
            print(f"{code} -> State code was not found")

def main():
    d = Data()
    run = True
    
    while run:
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