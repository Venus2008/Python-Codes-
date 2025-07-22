n='588432347423122345'
   # Output:  234, 23, 12, 2345
out=[]
temp=n[0]

for i in range(1,len(n)): #loop over the string
    if int(n[i])==int(n[i-1])+1: #check the last number is exactly one greater or not 
        temp+=n[i] # if yes then append
    else:
        if len(temp)>=2:  # else check the len of temp to avoide the loop break 
            out.append(temp) # as per the condition of the prograsm limit is set 

        temp=n[i] # save in temp to start the string with last digit every time  

if len(temp)>=2:  # after append one more loop to append 
    out.append(temp)

print(','.join(out)) #print them comma separated 