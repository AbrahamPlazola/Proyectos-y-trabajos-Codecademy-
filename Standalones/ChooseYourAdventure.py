print("Once upon a time...")

class TreeNode:
    def __init__(self, storypiece):
        self.storypiece = storypiece
        self.choices = []
    
    def addChild(self, node):
        self.choices.append(node)
    
    def traverse(self):
        flag = 0
        storyNode = self
        print(storyNode.storypiece)
        while storyNode.choices != []:
            choice = int(input("Enter 1 or 2 to continue the story: "))
            if choice not in [1, 2]:
                print("Enter a correct number")
            else:
                choice -= 1
                if flag == 0:
                    chosenChild = self.choices[choice]
                    flag = 1
                else:
                    chosenChild = storyNode.choices[choice]   
                storyNode = chosenChild           
                print(storyNode.storypiece)  

            
# Start #
start = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""  
storyRoot = TreeNode(start)
# Path A #
choiceA = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
pathA = TreeNode(choiceA)
storyRoot.addChild(pathA)

choiceA1 = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
pathA1 = TreeNode(choiceA1)
pathA.addChild(pathA1)

choiceA2 = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""
pathA2 = TreeNode(choiceA2)
pathA.addChild(pathA2)

# Path B #
choiceB = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
pathB = TreeNode(choiceB)
storyRoot.addChild(pathB)

choiceB1 = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
pathB1 = TreeNode(choiceB1)
pathB.addChild(pathB1)

choiceB2 = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
pathB2 = TreeNode(choiceB2)
pathB.addChild(pathB2)

userChoice = input("What is your name? ")
storyRoot.traverse()