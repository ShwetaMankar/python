print("Please response for asked details \n\n")

str = input("Are you vaccinated?yes/no : ")

if(str=="yes"):
    doseNo = input("\n\nHave you completed your both doses?yes/no : ")

    if(doseNo=="yes"):
        print("\nGood your are vaccinated..")
        
        temp = float(input("\n\nLet us know your body temprature "))
        if(temp<=99):
            print("\nYou have normal body temprature,you can travel.")
            print("\n........ HAPPY JOURNEY .......")
        else:
            print("Body temperature must be normal to travel due to pandemic. You should consider COVID19 test.")
        
        
    else:
        print("Sorry to say but for your safety both vaccinations must be completed ")
       
else:
    print("sorry....please complete your vaccination to be safe")
    
