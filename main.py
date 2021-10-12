numbers = [3,2,3,7,10,20]
my_list = [3, 7, "apple", "3", 7] 
second_list = [3, 10, 4, 7, 21, 3]
example = [ 2, 1, 3, 4 , 7, 8] 
example_2 = [ 123, 12345, 34543]
first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
second = [1, 20, 5, 10, 9, 11, 13, 4 ]

#1 
def problem_one(lis):
  total = 0
  for number in lis:
    total = total + number
  return total


#2
def problem_two(lis):
  total = 1
  for number in lis:
    total = total * number
  return total

#3
def problem_three(lis):
  temp = lis[0]
  for number in lis:
    if temp < number:
      temp = number
  return temp

#4
def problem_four(lis):
  temp = lis[0]
  for number in lis:
    if temp > number:
      temp = number
  return temp

#7














#8












#11













#14








#22







print(problem_one(numbers))
print(problem_two(numbers))
print(problem_three(numbers))
print(problem_four(numbers))