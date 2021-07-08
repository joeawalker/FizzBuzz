for num in range(1,101):

    string = ""

    if (num%15==0):
        string += str(num)+": FizzBuzz"
        print(string)

    elif (num%3==0):
        string += str(num)+": Fizz"
        print(string)

    elif (num%5==0):
        string += str(num)+": Buzz"
        print(string)

    else:
        string += str(num)+": "+str(num)
        print(string)

ex = input("")