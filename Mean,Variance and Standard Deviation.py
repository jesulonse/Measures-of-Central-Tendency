import math

def mean(list_of_x):
    sum_of_x = sum(list_of_x)
    length_of_x = len(list_of_x)
    return sum_of_x/length_of_x

def variance(list_of_x, mean):
    mean = mean(list_of_x)
    
    new_list = []
    for i in list_of_x:
        new_list.append((i - mean)**2)
    return sum(new_list)/len(new_list)
def standard_deviation():
    return math.sqrt(variance)
        
val_of_x = [21,21,21,21,24,24,24,24,24,24,26,26,26,26,26,26,26,29,29,29,29,29,29,29,29,29,29,29,40,40]

variance = variance(val_of_x, mean)
print(f"Mean is {mean(val_of_x)}")
print(f"Variance is {variance}")
print(f"Standard Deviation is {standard_deviation()}")
