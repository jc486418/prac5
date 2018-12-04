STATE_NAMES = {"QLD":"Queensland", "NSW": "New South Wales", "NT" :"Northern Territory", "WA" : "Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania"}
# print(STATE_NAMES)
for i,x in STATE_NAMES.items():
    print("{} is {}".format(i,x))

state = str.upper(input("Enter short state: "))
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = str.upper(input("Enter short state: "))