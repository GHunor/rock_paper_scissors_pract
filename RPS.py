#coding: utf-8
import random



def main():
	print("Welcome to Rock Paper Scissors")

	playing = input("Do you want to play? ")

	if playing.lower() != "yes":
    		print("k thx by!")
    		quit()

	u_score = 0
	c_score = 0
	games = 0


	while True:
    		max_games_s = input("How many games? ")
    		if max_games_s.isdigit():
        		max_games = int(max_games_s)
       		break
    		else:
        		print("Please give a number")
        		continue
    

	win_amount = int(max_games/2)
	if win_amount*2 <= max_games:
    		win_amount = win_amount+1


	encoding = ["rock","paper","scissors"]

	fstr = "It's{srt: n} out{stp: n}"
	print(fstr.format(srt = win_amount, stp=max_games) + ".")
	print("Type QUIT to end early.")

	score = 0
	i = 0;
	# for loop index in python doesn't work with an incremented value
	# it runs trough a sequence of values
	while i<max_games:
    		comp_pick_n = random.randint(0,2)
    		comp_pick = encoding[comp_pick_n]
    		if win_amount in [c_score, u_score]:
        		break
        
    		users_pick = input("What do you pick? ").lower()
    		if users_pick == "quit":
        		quit()
    
    		if users_pick in [ "rock", "paper", "scissors"]:
        		if users_pick == comp_pick:
            		print("Stalemate!")
            		continue
        		if users_pick == "rock":
            		if comp_pick == "paper":
                			print("Paper beats rock, You lose!")
                			c_score = c_score +1
            		else:
                			print("Rock beats scissors, You win!")
                			u_score = u_score + 1
            		games = games + 1
            		i = i+1
            		continue
        		if users_pick == "paper":
            		if encoding[comp_pick] == "scissors":
                			print("Scissors beats paper, You lose!")
                			c_score = c_score +1
            		else:
                			print("Paper beats rock, You win!")
                			u_score = u_score + 1
            		games = games + 1
            		i = i+1
            		continue
        		if users_pick == "scissors":
            		if encoding[comp_pick] == "rock":
                			print("Rock beats scissors, You lose!")
                			c_score = c_score +1
            		else:
                			print("Scissors beats paper, You win!")
                			u_score = u_score + 1
            		games = games + 1
            		i = i+1
            		continue
    		else:
        		print("Please give a valid option")
        		continue
    		i = i+1

	if u_score>c_score:
    		print(fstr.format(srt = u_score, stp=max_games) + ". You're winner!")
	elif u_score<c_score:
    		print(fstr.format(srt = c_score, stp=max_games) + " for me. You lose.")
	else:
    		print("O.o")

	if u_score == 0:
    		print("0 wins?! Wow! How did you manage that?")


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
