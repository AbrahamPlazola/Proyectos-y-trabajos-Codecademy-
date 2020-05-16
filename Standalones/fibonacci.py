def fibonacci(n):
    if n is 1:
        return 1
    if n is 0:
        return 0
    
    fibValue = fibonacci(n-1) + fibonacci(n-2)
    if fibValue not in alreadySeen:
        alreadySeen.append(fibValue)
    return fibValue

while True:
    alreadySeen = []
    choice = input("Do you want to generate fibonacci numbers, search them or exit? G/S/E ")
    if choice is "G":
        lowerLimit = int(input("From which number would you like to see? "))
        upperLimit = int(input("Until which number would you like to see? "))

        fibonacci(upperLimit)

        for i in alreadySeen:
            if i > lowerLimit and i < upperLimit:
                print(i)

        w = input("Do you want to save this sequence? Y/N ")
        if w is "Y":
            f = open("fib.txt", "w+")
            for i in alreadySeen[ lowerLimit : upperLimit]:
                f.write(str(i) + ",")
            f.close()
    elif choice is "S":
        f = open("fibUntil40.txt", "r")
        contents = f.read()
        contentsList = contents.split(",")
        f.close()

        search = input("Which number do you want to search? ")
        try:
            print("Number found at index " + contentsList.index(search))
        except ValueError:
            print("Number not found in fibonacci sequence")
    else:
        break

print("bye bye")