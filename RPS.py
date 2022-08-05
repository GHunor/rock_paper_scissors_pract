#coding: utf-8
import random

class rps_v:
    __translate = {
            0: "rock",
            1: "paper",
            2: "scissors",
            "rock": 0,
            "paper": 1,
            "scissors": 2}
    def __init__(self, val):
        if val in ["rock", "paper", "scissors"]:
            self.val = self.__translate[val]
        elif val in [0, 1, 2]:
            self.val = val
        else:
            print("Valid option please!")
    def by_name(self):
        return self.__translate[self.val]
    def __eq__(self, other):
        return self.val == other.val
    def __lt__(self, other):
        if self.val in [0,2] and other.val in [0,2]:
            return self.val > other.val
        else:
            return self.val < other.val
        
def greetings(GameName):
	print("Welcome to " + GameName +"!")
	playing = input("Do you want to play? ")
	if playing.lower() != "yes":
		print("k thx by!")
		quit()

def game_set():
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

    fstr = "It's{srt: n} out{stp: n}"
    print(fstr.format(srt = win_amount, stp=max_games) + ".")
    print("Type QUIT to end early.")
    return max_games, win_amount
def cycle(max_games, win_amount):
	u_score = 0
	c_score = 0
	games = 0 
	i = 0
	while i < max_games:
		comp_pick = random.randint(0,2)
		if win_amount in [c_score, u_score]:
			break
        
		users_pick = input("What do you pick? ").lower()
		if users_pick == "quit":
			quit()
		if users_pick in [ "rock", "paper", "scissors"]:
			UPick = rps_v(users_pick)
			CPick = rps_v(comp_pick)
			if UPick == CPick:
				print("Stalemate!")
				games = games + 1
				continue
			if UPick < CPick:
				print("You lose! " + CPick.by_name() +" beats " + UPick.by_name())
				c_score = c_score + 1
			else:
				print("You win! " + UPick.by_name() +" beats " + CPick.by_name())
				u_score = u_score + 1     
		else:
			print("Please give a valid option")
			continue
            
		i = i + 1
		games = games + 1
	return u_score, c_score, games
def end_message(c_score, u_score, max_games):
    fstr = "It's{srt: n} out{stp: n}"
    if u_score>c_score:
    	print(fstr.format(srt = u_score, stp=max_games) + ". You're winner!")
    elif u_score<c_score:
    	print(fstr.format(srt = c_score, stp=max_games) + " for me. You lose.")
    else:
    	print("O.o")

    if u_score == 0:
    	print("0 wins?! Wow! How did you manage that?")
    	
def main():
	greetings("Rock Paper Scissors")
	max_games, win_amount = game_set()
	u_score, c_score, games = cycle(max_games, win_amount)
	end_message(c_score, u_score, max_games)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()



'''
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
            		i = i + 1
            		continue
        		if users_pick == "paper":
            		if encoding[comp_pick] == "scissors":
                			print("Scissors beats paper, You lose!")
                			c_score = c_score +1
            		else:
                			print("Paper beats rock, You win!")
                			u_score = u_score + 1
            		games = games + 1
            		i = i + 1
            		continue
        		if users_pick == "scissors":
            		if encoding[comp_pick] == "rock":
                			print("Rock beats scissors, You lose!")
                			c_score = c_score +1
            		else:
                			print("Scissors beats paper, You win!")
                			u_score = u_score + 1
            		games = games + 1
            		i = i + 1
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
'''
