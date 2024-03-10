import random                  
from colorama import Fore               #colorama package to print coloured text
                                        #fore in colorama package prints the text in specified color

print(Fore.GREEN+" ")
def start_game():
    print("Welcome to the Interactive Storytelling Game!")
    print("\033[1m TRAYAMBAKAM is a mysterious inn where one  can find the weapon to attain immortality \033[0m")
                                                                      #\033[1m..\033[0m- is the escape sequence used to bold the statements
    print("you are in a TRAYAMBAKAM now! Pass all the three levels to get the weapons for attaining immortality")
    play()

def play():
    while True:
        print(Fore.BLUE+"")
        choice = input("what will you do? 1.Enter the level one? 2.End your life here?")
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
    print(a.center(100))                            #center method is used to make the text to be aligned in center
    print()
    print("To unlock the YAJAMAHE, answer the riddle")
    print()
    Question = "The epic Ramayana tells the tale of Rama's battle against which demon king?"
    answer = "ravana"
    player_answer = input("Question: {}\nYour answer: ".format(Question))           #{}is used as a placeholder to of a text.
                                                                            # format method formats the specified calues and insert them inside the string's placeholder.
    if player_answer.lower() == answer:
        print("The door unlocks, and you proceed.")
        print()
        l2()
    else: 
        b="You've lost the power."   
        print(b.center(100))  
        print()    

def l2():
    print(Fore.GREEN+"Congratulations! You've got the power of YAJAMAHE")
    print()
    print("It's the time for level-2")
    print()
    c="The Level-SUGANDHIM"
    print(c.center(100))
    print()
    print("Answer me to cross me...")
    Question = "Who wrote the epic RAMAYANA?"
    answer = "valmiki"
    player_answer = input("Question: {}\nYour answer: ".format(Question))
    if player_answer.lower() == answer:
        print("The door unlocks, and you proceed.")
        print()
        l3()
    else: 
        d="You can never answer me! You've lost..."   
        print(d.center(100)) 
        print()

def l3():
    print(Fore.CYAN+"Congratulations! You've got the power of SUGANDHIM")
    print("It's the time for level-3")
    print("You are one step ahead to gain the weapon")
    print()
    e="The Level-Pushtivardhanam"
    print(e.center(100))
    print("HAHAHA you can't answer me!!")
    print()
    Question = "Ravan was devotee of which god?"
    answer = "shiva"
    player_answer = input("Question: {}\nYour answer: ".format(Question))
    if player_answer.lower() == answer:
        print("You've cracked me as well!!")
        z="Congratulations you've successfully attained the weapon for immortality"
        print(z.center(100))
        print()
        nxt()
    else: 
        d="I told you, you can't answer me! HAHAHAHA.. you've lost the weapon"   
        print(d.center(100))
        print()

def nxt():
    print(Fore.GREEN+"Congratulations on attaining the weapon to get the immortality.")
    print()
    print("choose one: Either to use the weapon or to exit the game without getting the immortality.")
    outcome =input(["use", "exit"])
    if outcome == "use":
        use_the_weapon()
    else:
        exit_game()

def use_the_weapon():
    print("you've got to use the weapon and get the immortality")
    print("use the weapon to kill the evil infront or run away..")
    print()
    print("Select one- To run away or to fight the evil. ")
    outcome = input(["run", "fight"])
    if outcome == "run":
        print("You ran away and found a map.")
        print()
        nxt_step()
    else:
        print("You have decided to fight the evil.")
        print()
        if random.random() < 0.5:                                #random() returns a random float number between 0 and 1
            print("You've successfully defeated the evil and found the key.")
            nxt_step()
        else:
            print("The evil monster attacked you. You have lost the weapon!!")

def nxt_step():
    while True:
        choice = input("What's your next move? (1. Follow the map, 2. Explore further): ")
        print()
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
    print()
    y="Congratulations, you've gained the immoratality!HOORAYY!!!"
    print(y.center(100))

def explore_further():
    print(Fore.BLUE+"You explore further and encounter a locked golden gate.")
    print("To unlock the gate, you must solve a riddle:")
    Question = "What can be touched but not seen?"
    answer = "air"
    player_answer = input("Question: {}\nYour answer: ".format(Question))
    if player_answer.lower() == answer:
        print(Fore.YELLOW+"The golden gate is welcoming you whole heartedly.")
        print("You find yourself in the peace and clear way")
        print()
        x="Congratulations, you've gained the immoratality!HOORAYY!!!"
        print(x.center(100))
        print()
    else:
        print("You've lost your weapon and the chance to attain immortality.")                 
        print("Better luck next time")
        print()

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
        print()

        if play_again.lower() == "yes":
            start_game()
        else:
            print("Thank you for playing! Have a nice day....")
            break
        
if __name__ == "__main__":                  # [entry point]. tells that the file is running directly and not imported.
    main()
