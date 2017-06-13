def prime_number_generator(maximum):
    ls = [] #Empty list into which th values will be stored for easier use with the tests
    for num in range(2, maximum + 1): #Looping through the given range
        if num > 1: #Ensuring that the numbers are all positive
            for i in range(2, num): #Looping between 2 and each of the numbers from the outer loop
                if (num % i) == 0: #checking to see if any of the numbers from the second loop divides the value from the outer loop
                    break #break out of the loop to improve run time
            else:
                #print(num) - This was for debugging purposes
                ls.append(num) #Append the numbers sequentially
    return ls #return the resulting list