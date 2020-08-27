numbers = [1, 2, 3, 4]
removed_number = numbers.pop()

print(numbers)
print(removed_number)

a = 10
n = 20

num_list = list(range(a, n))

print(num_list)
print(num_list.pop())
print(num_list)


# Given the following code, what would print to the console?

random_list = [True, 1, 5.5, 3]
popped_value = random_list.pop()
print(random_list)

# Given the following code, what would print to the console?

random_list = ['True', 1, 5.5, 3]
new_value = random_list.pop()
print(new_value)

"""3
Pop Challenge

It is common in mathematics to need to remove outliers from a data set. The .pop() method in conjunction with the .index() method can be a useful combination for accomplishing such a task. Complete the remove_outliers function below. This function takes one parameter called data and is a collection of observed data. This function should return the data list with the smallest value removed and the largest value removed.

Notes:

    Do not modify the original list, make a copy first
    Do not modify the original order of the elements of the list

Example:

    remove_outliers([55, 1, 23, 523, 68, 81, 99]) -> [55, 23, 68, 81, 99]

"""

data_lst = [55, 1, 23, 523, 68, 81, 99]


def remove_outliers(data_lst):
  data_lst1 = data_lst.copy()
  data_lst1.pop(data_lst1.index(max(data_lst1)))
  data_lst1.pop(data_lst1.index(min(data_lst1)))
  return data_lst1
  

print(remove_outliers(data_lst))

