#get the loan details

money_owed = float(input("how much money do you owe? "))
apr = float(input("what is annual percentage rate?\n "))
payment = float(input("what will be your monthly payment?\n "))
months = int(input("how many months do you want to see results for"))

#divide apr by 100 to make it percent then divide by 12 to make monthly rate
monthly_rate=apr/100/12

for i in range(months):
    #add in interest
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed-payment<0):
        print("The last payment is",money_owed)
        print("you paid off the loan in",i+1,"months")
        break

    #make payment

    money_owed = money_owed - payment

    #print results
    print("paid",payment,"of which",interest_paid,"was interest",end=" ")
    print("Now i owe" , money_owed)