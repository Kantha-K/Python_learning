# expenses = [10,11,7,8,5,11.5,5.5]
# sum = 0

# for i in expenses:
#     sum = sum+i
# print(sum)
# print("you spent", sum)
# print("you spent $", sum)
# print("you spent $", sum,sep="")
# print("you spent $", sum,"on lunch this week",sep="")



num_of_expenses=int(input("enter value:"))

total=0
expenses=[]
for i in range(num_of_expenses):
    expenses.append(float(input("enter expense value:")))
total = sum(expenses)
print("you spent $", total,"on lunch this week",sep="")
