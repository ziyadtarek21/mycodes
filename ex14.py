first_date=(input("enter first date in commas "))
second_date=(input("enter second date in commas "))
first_date=first_date.split(",")
second_date=second_date.split(",")
mylist=first_date
mylisttwo=second_date
result1=(int(mylist[2])-int(mylisttwo[2]))
result2=(int(mylist[0])-int(mylisttwo[0]))
years=(result2*365)
result3=(int(mylist[1])-int(mylisttwo[1]))
months=(result3*30)
final_result=(abs(months)+abs(years)+abs(result1))
print(str(final_result)+ " days")
