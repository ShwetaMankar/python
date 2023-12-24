age = int(input("Enter your age : "))
if(age>10 and age<70):

	amount = float(input("Amount you want to invest in policy : "))
	if(amount >= 10000):

		year = int(input("For how many years you want to invest in our policy : "))
		if(year>=3):
			if(age>10 and age<20):
			
				print("")
				print("You will get 3% interest per year")
				print("")
				
				interest_amount = (amount*3*year)/100 #amount at 3% for year
				interest_per_year = interest_amount/year
				print("Your per year interest is Rs.",interest_per_year)
				
				total_interest = interest_amount*year
				print("Rs.",total_interest,"total interest you will recieve ")
				
				tamount = amount+(interest_amount*year)
				print("You will get total amount Rs.%f after %d year"%(tamount,year))
				
			elif(age>20 and age<30):
			
				print("")
				print("You will get 4% interest per year")
				print("")
				
				interest_amount = (amount*4*year)/100 #amount at 4% for year
				interest_per_year = interest_amount/year
				print("Your per year interest is Rs.",interest_per_year)
				
				total_interest = interest_amount*year
				print("Rs.",total_interest,"total interest you will recieve ")
				
				tamount = amount+(interest_amount*year)
				print("You will get total amount Rs.%f after %d year"%(tamount,year))
			
			elif(age>30 and age<40):
			
				print("")
				print("You will get 5% interest per year")
				print("")
				
				interest_amount = (amount*5*year)/100 #amount at 5% for year
				interest_per_year = interest_amount/year
				print("Your per year interest is Rs.",interest_per_year)
				
				total_interest = interest_amount*year
				print("Rs.",total_interest,"total interest you will recieve ")
				
				tamount = amount+(interest_amount*year)
				print("You will get total amount Rs.%f after %d year"%(tamount,year))
			
			elif(age>50 and age<70):
			
				print("")
				print("You will get 7% interest per year")
				print("")
				
				interest_amount = (amount*7*year)/100 #amount at 7% for year
				interest_per_year = interest_amount/year
				print("Your per year interest is Rs.",interest_per_year)
				
				total_interest = interest_amount*year
				print("Rs.",total_interest,"total interest you will recieve ")
				
				tamount = amount+(interest_amount*year)
				print("You will get total amount Rs.%f after %d year"%(tamount,year))
				
		else:
			print("Policy is for more than 3 years investment")
	else:
		print("To in invest in our policy amount must be more than Rs.10000/-")
else:
	print("Age criteria is between 10 to 70")