str = input()
output = ""
for n in str:
    if(n=="0"):
        output+="0"
    elif(n=="1"):
        output+="1"
    elif(n=="B"):
        output = output[:-1]
print(output)
