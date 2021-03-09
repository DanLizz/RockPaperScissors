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
win = '''____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| 
                                                                       '''
lose = '''     ___       __     ____    __    ____  __  .__   __. 
    /   \     |  |    \   \  /  \  /   / |  | |  \ |  | 
   /  ^  \    |  |     \   \/    \/   /  |  | |   \|  | 
  /  /_\  \   |  |      \            /   |  | |  . `  | 
 /  _____  \  |  |       \    /\    /    |  | |  |\   | 
/__/     \__\ |__|        \__/  \__/     |__| |__| \__| 
                                                        '''                                                                  
draw = ''' _______  .______          ___   ____    __    ____ 
|       \ |   _  \        /   \  \   \  /  \  /   / 
|  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  
|  |  |  ||      /      /  /_\  \  \            /   
|  '--'  ||  |\  \----./  _____  \  \    /\    /    
|_______/ | _| `._____/__/     \__\  \__/  \__/     
                                                    '''
import random

user = input("Rock, Paper or Scissor? Type in your choice \n").lower()
ai = ["rock","paper","scissors"]
computer = random.choice(ai)

if user == "rock":
  print(rock)
elif user == "paper":
  print(paper)
elif user == "scissors":
  print(scissors)
else:
  print("Invalid input")

if computer == "rock":
  print(rock)
  if user == "paper":
    print(win)
  elif user == "scissors":
    print(lose)
  elif user == "rock":
    print(draw)
elif computer == "paper":
  print(paper)
  if user == "paper":
    print(draw)
  elif user == "scissors":
    print(win)
  elif user == "rock":
    print(lose)
elif computer == "scissors":
  print(scissors)
  if user == "paper":
    print(lose)
  elif user == "scissors":
    print(draw)
  elif user == "rock":
    print(win)
else:
  print("Invalid input")

