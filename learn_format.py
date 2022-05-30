#Problem 5:

#You are given two variables:
#age = 4
#name = "Sammy"

#Use print formatting to print the following string:
#"Hello my dog's name is Bobby and he is 4 years old"

name = "Sammy"
age = 4
print("Hello my dog's name is {} and he is {} years old".format(name,age))
print("Hello my dog's name is {name} and he is {age} years old".format(name="Bobby",age=4))