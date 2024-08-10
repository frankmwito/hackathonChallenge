# Q1. problem solving
#Input the integers in the list
input_list = list(map(int, input("Enter any intergers of choice seperated by spaces:").split()))

unique_list = list(set(input_list))# remove duplicates the newly added list by converting into a set

sorted_list = sorted(unique_list,reverse = True) # sort the list/set in a reverse order

print("The sorted list of integers without duplicates is:", sorted_list)