yr=int(input("Enter year"))
if yr%100!=0 and yr%400==0 or yr%4==0:
    print("LEAP YEAR -",yr)
else:
    print("NOT A LEAP YEAR -",yr)