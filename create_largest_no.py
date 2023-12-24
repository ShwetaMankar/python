lst = [1,23,9,8]
lst2 = []
#t=0
#while(t<len(lst)):
for i in lst:
    lst.remove(i)
    #print(lst)
    for j in iter(str(i)):
        #print(j)
        for k in lst[:3]:
            #print(k)
            for l in iter(str(k)):
                if j < l:
                    temp = i
                    i = k
                    k = temp
                    #lst.remove(i)
                    lst2.append(i) #23,1,9,8
                    

#t = t+1
print(lst2)


num = ""
for i in lst2:
    #num = str(i)
    num+=str(i)
print(num)
    

    


            
