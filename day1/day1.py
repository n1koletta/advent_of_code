#create a list of lists
#find the sum of each list
#find the max of the sums

main_list = []

with open("input_day1.txt", "r") as file:
    temp_list = []
    for line in file:
        if line != '\n':  # if there is no content...
            temp_list.append(line)  # save the valid line.
        else:
            main_list.append(temp_list)
            temp_list = []
    if temp_list: #add the final line
        main_list.append(temp_list)


main_list = [[int(x.replace('\n','')) for x in lst] for lst in main_list]
list_of_sum = [sum(lst) for lst in main_list]

top_three = sorted(list_of_sum,reverse=True)[:3]

print(max(list_of_sum))
print(sum(top_three))