import random
from colorama import Fore

def start_game():
    print("Welcome to the Interactive Storytelling Game!")
    print("you are in a TRAYAMBAKAM now! Pass all the three levels to get the weapons for attaining immortality")
    play()

def play():
    while True:
        choice = input("what will you do? 1.Enter the level one? 2.End you life here?")
        if choice == '1':
          l1()
          break   
        elif choice == '2':
            nd()  
        else:
            print("Invalid choice. Please enter 1 or 2.")

def l1():
    print(Fore.RED+"You've chosen to enter the level 1")
    a="The Level-YAJAMAHE"
    print(a.center(100))
    print("To unlock the YAJAMAHE, answer the riddle")
    puzzle = "The epic Ramayana tells the tale of Rama's battle against which demon king?"
    answer = "ravana"
    player_answer = input("Puzzle: {}\nYour answer: ".format(puzzle))
    if player_answer.lower() == answer:
        print("The door unlocks, and you proceed.")
        l2()
    else: 
        b="You've lost the power."   
        print(b.center(100))      

def l2():
    print(Fore.GREEN+"Congratulations! You've got the power of YAJAMAHE")
    print("It's the time for level-2")
    c="The Level-SUGANDHIM"
    print(c.center(100))
    print("Answer me to cross me...")
    puzzle = "Who wrote the epic RAMAYANA?"
    answer = "valmiki"
    player_answer = input("Puzzle: {}\nYour answer: ".format(puzzle))
    if player_answer.lower() == answer:
        print("The door unlocks, and you proceed.")
        l3()
    else: 
        d="You can never answer me! You've lost..."   
        print(d.center(100)) 

def l3():
    print(Fore.CYAN+"Congratulations! You've got the power of SUGANDHIM")
    print("It's the time for level-3")
    print("You are one step ahead to gain the weapon")
    e="The Level-Pushtivardhanam"
    print(e.center(100))
    print("HAHAHA you can't answer me!!")
    puzzle = "Ravan was devotee of which god?"
    answer = "shiva"
    player_answer = input("Puzzle: {}\nYour answer: ".format(puzzle))
    if player_answer.lower() == answer:
        print("You've cracked me as well!!")
        z="Congratulations you've successfully attained the weapon for immortality"
        print(z.center(100))
        nxt()
    else: 
        d="I told you, you can't answer me! HAHAHAHA.. you've lost the weapon"   
        print(d.center(100))

def nxt():
    print(Fore.GREEN+"Congratulations on attaining the weapon to get the immortality.")
    outcome = random.choice(["use", "exit"])
    if outcome == "use":
        use_the_weapon()
    else:
        exit_game()

def use_the_weapon():
    print("you've got to use the weapon and get the immortality")
    print("use the weapon to kill the evil infront")
    outcome = random.choice(["run", "fight"])
    if outcome == "run":
        print("You ran away and found a map.")
        nxt_step()
    else:
        print("You have decided to fight the evil.")
        if random.random() < 0.6:  
            print("You've successfully defeated the animal and found the key.")
            nxt_step()
        else:
            print("The evil monster attacked you. You have lost the weapon!!")

def nxt_step():
    while True:
        choice = input("What's your next move? (1. Follow the map, 2. Explore further): ")
        if choice == '1':
            follow_map()
            break
        elif choice == '2':
            explore_further()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")       

def follow_map():
    print(Fore.YELLOW+"You follow the map and discover a secret exit from the TRAYAMBAKAM.")
    y="Congratulations, you've gained the immoratality!HOORAYY!!!"
    print(y.center(100))

def explore_further():
    print(Fore.BLUE+"You explore further and encounter a locked golden gate.")
    print("To unlock the gate, you must solve a riddle:")
    riddle = "What can be touched but not seen?"
    answer = "air"
    player_answer = input("Riddle: {}\nYour answer: ".format(riddle))
    if player_answer.lower() == answer:
        print(Fore.YELLOW+"The golden gate is welcoming you whole heartedly.")
        print("You find yourself in the peace and clear way")
        x="Congratulations, you've gained the immoratality!HOORAYY!!!"
        print(x.center(100))
    else:
        print("You've lost your weapon and the chance to attain immortality.")                 
        print("Better luck next time")

def exit_game():
    print("You find a treasure chest!")
    outcome = random.choice(["map", "trap"])
    if outcome == "map":
        print("You open it and find a map.")
        nxt_step()
    else:
        print("As you open the chest, it triggers a trap. You narrowly avoid it and find a key inside.")
        nxt_step()      

def nd():
    f='You have chosen to end here.Restart...'
    print(f.center(100))

 
def main():
    start_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            start_game()
        else:
            print("Thank you for playing! Have a nice day....")
            break
if __name__ == "__main__":
    main()
