
test_dict = {"Hi" : 4, "I" : 4,"am" : 3,"your" : 4,"friend" : 3}

print("The original dictionary is : ",test_dict)

K = int(input("Enter your number in"))

res = 0

for key in test_dict:
    if test_dict[key]==K:
        res = res + 1

print("Frequency of K is : ",res)