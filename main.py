# mylist = [1, 2, 3, 4]
# counter_of_even = 0
# counter_of_odds = 0
# for i in mylist:
#     if int(i) % 2 == 0:
#         counter_of_odds += int(i)
#     elif int(i) % 2 != 0 :
#         counter_of_even += int(i)
# print(f'sum of odds = {counter_of_odds}, counter of even = {counter_of_even}')

def sum_of_list(mylist):
    counter_of_even = 0
    counter_of_odds = 0
    for i in mylist:
        if int(i) % 2 == 0:
            counter_of_odds += int(i)
        elif int(i) % 2 != 0:
            counter_of_even += int(i)
    return f'sum of odds = {counter_of_odds}, counter of even = {counter_of_even}'
print(sum_of_list([1, 1, 1, 1]))




