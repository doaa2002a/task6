# question 1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
largest_number = max(lst)
print(largest_number)

smallest_number = min(lst)
lst.remove(smallest_number)
# print(lst) # output = [30, 75, 9, 97, 50, 70, 59]

lst.sort() #print(lst) # output = [9, 30, 50, 59, 70, 75, 97]

lst.sort(reverse=True) #print(lst) # output = [97, 75, 70, 59, 50, 30, 9]


last_4_numbers = lst[:-5:-1]
print(last_4_numbers)


# question 2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count = 0
for sublist in main_lst:
    if "python" in sublist:
        count += 1
print(count)

# question 3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(' '.join(my_lst).title())

# question 4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]

my_lst_copy = my_lst[:]
print(my_lst_copy)


# question 5
my_lst2 = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst2 [2] = my_lst2 [4]
print(my_lst2)


# question 6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))

# question 7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
add = 9,
tuple1 = tuple1 + (add)
print(tuple1)
print(type (tuple1))


# question 8
tuple2 = (4, 'python', 'GSG', [8, 3, 1])
tuple3 = ('Java', 'C++', 7.8)
new_tuple = (tuple2) + (tuple3)
print(new_tuple)


print("full mark inshallah ^_^")