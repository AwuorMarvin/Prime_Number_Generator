def prime_number_generator(maximum):
    ls = []
    for num in range(2, maximum + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                ls.append(num)

    return ls