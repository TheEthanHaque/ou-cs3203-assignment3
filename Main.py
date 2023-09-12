import sumOfNumbers
import reverse

def main():

    stringOfNumbers = input("Enter a list of Numbers with spaces in between: ")

    numList = [int(num) for num in stringOfNumbers.split()]

    print("These are the result of sum of Numbers: " + str(sumOfNumbers.sumOfNumbers(numList)))
    print("These are the result of product of Numbers: " + str(sumOfNumbers.productOfNumbers(numList)))
    print("reverse of array: ", reverse.reverse_list(numList))

main()
