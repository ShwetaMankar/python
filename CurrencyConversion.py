print("Foreign Currency convertion into INR\n")

usd = float(input("Enter USD to convert into INR : "))
yen = float(input("Enter Yen to convert into INR : "))
pound = float(input("Enter Pound to convert into INR : "))
yuan = float(input("Enter Yuan to convert into INR : "))
rand = float(input("Enter Rand to convert into INR : "))

usd_inr = usd*76.59
yen_inr = yen*0.59
pound_inr = pound*96.02
yuan_inr = yuan*11.59
rand_inr = rand*4.80

print("\nUSD to INR : ",usd_inr)
print("Yen to INR : ",yen_inr)
print("Pound to INR : ",pound_inr)
print("Yuan to INR : ",yuan_inr)
print("Rand to INR : ",rand_inr)

print("\nINR convertion into Foreign Currency\n")
inr = float(input("\nEnter INR for foreign currency conversion : "))

""""inrUsd = float(input("Enter INR to convert into USD : "))
inrYen = float(input("Enter INR to convert into Yen : "))
inrPound = float(input("Enter INR to convert into Pound : "))
inrYuan = float(input("Enter INR to convert into Yuan : "))
inrRand = float(input("Enter INR to convert into Rand : "))

inr_usd = inrUsd/76.59
inr_yen = inrYen/0.59
inr_pound = inrPound/96.02
inr_yuan = inrYuan/11.59
inr_rand = inrRand/4.80"""

inr_usd = inr/76.59
inr_yen = inr/0.59
inr_pound = inr/96.02
inr_yuan = inr/11.59
inr_rand = inr/4.80


print("\nINR to USD : ",inr_usd)
print("INR to Yen : ",inr_yen)
print("INR to Pound : ",inr_pound)
print("INR to Yuan : ",inr_yuan)
print("INR to Rand : ",inr_rand)