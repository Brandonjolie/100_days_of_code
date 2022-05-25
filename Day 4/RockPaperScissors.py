import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
selection = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)
choices = {0: rock, 1: paper, 2: scissors}
print(f"{choices[selection]}")
print(f"Computer chose:\n {choices[computer]}")
if selection == 1 and computer == 0:
    print("You win!")
elif selection == 2 and computer == 1:
    print("You win!")
elif selection == 0 and computer == 2:
    print("You win!")
elif selection == computer:
    print("Draw")
else:
    print("You lose!")
