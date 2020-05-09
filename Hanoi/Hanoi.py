from stacks import Stack

leftStack = Stack("Left")
middleStack = Stack("Middle")
rightStack = Stack("Right")
stacksLst = [leftStack, middleStack, rightStack]

numDisks = int(input("\n How many disks you wanna play with? \n"))
while numDisks < 3:
    numDisks = int(input("\n Enter a number greater than or equal to 3\n"))

for i in range(numDisks, 0, -1):
    leftStack.push(i)

optimalMoves = (2**numDisks) - 1
print("\n The fastest game would be {optimal} moves\n".format(optimal = optimalMoves))

def get_input():
    choices = ["L", "M", "R"]
    while True:
        for i in range(len(stacksLst)):
            name = stacksLst[i].get_name()
            letter = choices[i]
            print("Enter {letter} for {stack}".format(letter = letter, stack = name))
        
        user_input = input("")
        if user_input in choices:
            for i in range(len(stacksLst)):
                if user_input == choices[i]:
                    return stacksLst[i]

numUserMoves = 0

while rightStack.get_size() != numDisks:
    print("\n\n\n...Current Stacks...")
    for i in stacksLst:
        i.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        fromStack = get_input()
        print("\nWhich stack do you want to move to?\n")
        toStack = get_input()

        if fromStack.is_empty():
            print("\n\nInvalid Move. Try again.")
        elif toStack.is_empty() or fromStack.peek() < toStack.peek():
            disk = fromStack.pop()
            toStack.push(disk)
            numUserMoves += 1
            break
        else:
            print("\n\nInvalid Move. Try again.")

print("You completed the game in {moves} moves".format(moves = numUserMoves))
