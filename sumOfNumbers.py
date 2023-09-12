#Function that computes sum of list 

def sumOfNumbers(listOfNumbers):
    total = 0
    for num in listOfNumbers:
        total += num
    return total

#Function that returns the product of a list

def productOfNumbers(listOfNumbers):
    product = 1
    for num in listOfNumbers:
        product *= num
    return product
