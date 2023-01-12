uppercase = 0
lowercase = 0

input_string = input()

for i in input_string:
    if i.isupper():
        uppercase += 1
    elif i.islower(): 
        lowercase +=1
    elif i.isspace():
        uppercase += 0
        lowercase += 0    

print(lowercase)  
print(uppercase)     
