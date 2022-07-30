#coding: utf-8
import random

print("Welcome to Rock Paper Scissors")


#random.seed()
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("k thx by!")
    quit()

u_score = 0
c_score = 0
games = 0

max_games = int(input("How many games? "))
win_amount = int(max_games/2)
if win_amount*2 == max_games:
    win_amount = win_amount+1

comp_pick = random.randint(0,2)
encoding = {
    0 : "rock",
    1 : "paper",
    2 : "scissors"}

fstr = "It's{srt: n} out{stp: n}."
print(fstr.format(srt = win_amount, stp=max_games))
print("Type QUIT to end early.)

score = 0
guess = the_number-1;
i = 0;
# for loop index in python doesn't work with an incremented value
# it runs trough a sequence of values
while i<max_games):
    if win_amount in [c_score, u_score]:
        break
        
    users_pick = input("What do you pick? ").lower()
    if user_pick == "quit":
        quit()
    
    if users_pick in [ "rock", "paper", "scissors"]:
        if user_pick == encoding[comp_pick]
            print("Stalemate!")
            continue
        if user_pick == "rock":
            if comp_pick == "paper":
                print("Paper beats rock, You lose!")
                c_score = c_score +1
            else
                print("Rock beats scissors, You win!")
                u_score = u_score + 1
            games = games + 1
            i = i+1
            continue
        if user_pick == "paper":
            if encoding[comp_pick] == "scissors":
                print("Scissors beats paper, You lose!")
                c_score = c_score +1
            else
                print("Paper beats rock, You win!")
                u_score = u_score + 1
            games = games + 1
            i = i+1
            continue
        if user_pick == "scissors":
            if encoding[comp_pick] == "rock":
                print("Rock beats scissors, You lose!")
                c_score = c_score +1
            else
                print("Scissors beats paper, You win!")
                u_score = u_score + 1
            games = games + 1
            i = i+1
            continue
    else
        print("Please give a valid option")
        continue
    i = i+1
if u_score>c_score:
    print("You're winner")
elif u_score<c_score:
    print("You lose")
print("You guessed the number in " + str(score) + " tries.")
if score > stop-start:
    print("Wow! How did you manage that?")
