num=int(input("Enter a number : "))
rev=0
temp=num #stored to display later through temp cause it will be 0 at end
while num!=0:
	rem=num%10
	rev=(rev*10)+rem
	num=num//10
print("Reverse number of ",num,"is",rev)