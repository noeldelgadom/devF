
def challenge1(lista,element):
    if element in lista:
        return "I found the element in index %d" % lista.index(element) 
    else:
            return "Sorry, i couldn't find your element"
            
def challenge2(lista):
    total = 1
    for i in lista:
        total *= i
    return total
            
        
lista = [1,2,3,4,5,6,7]
element = 3
print(challenge1(lista,element))
print(challenge2(lista))
