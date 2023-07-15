file = open("states.csv")                                  # 'file' object

data = {}                                                  # dict, {}

for line in file:                                          # for each str in list of strings
    line = line.strip('\n')                                # str, "AL,4908621,52420,Alabama"
    abr, value_1, value_2, state = line.split(',')         # AL,4908621,52420,Alabama
    data[state] = abr                                      # adding {'Alabama': 'AL'}

file.close()

count = len(data)                                          # int, 50

print(F"There are {count} pairs in the lookup dict,")
user_type = input("please enter a state name: ")           # str, 'Alabama' (sample value)

if user_type in data:                                      # bool, True
    abr = data[user_type]                                  # str, 'AL' (sample value)
    print(F"Abbreviation for {user_type} is {abr}.")

else:
    print(f'no state found with name "{user_type}".')
