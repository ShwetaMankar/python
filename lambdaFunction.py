add = lambda x=24, y=78 : x+y
print("Addition :",add()) 

sub = lambda a,b : a-b
print("Substraction : ",sub(45,76))

max = lambda l,m : l if(l>m) else m
print("Max number is ",max(45,76))

min = lambda p,q : p if(p<q) else q
print("Min number is ",min(394,58))

mark = lambda m : "Pass" if(m>35) else "Fail" 
print(mark(98))

age = lambda a : "eligible" if(a>18) else "not eligible"
print("For voting you are",age(18))

percent = lambda a,b,c,d,e : a+b+c+d+e
print("Percentage of given marks is ",(percent(98,90,78,88,67)/500)*100)

