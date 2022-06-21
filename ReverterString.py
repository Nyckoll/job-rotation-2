

def reverter(palavra): 
    if len(palavra) == 0: 
        return palavra 
    else: 
        return reverter(palavra[1:]) + palavra[0] 
palavra = input()
print(reverter(palavra))
