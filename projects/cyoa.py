"""Choose Your Own Adventure Game."""

__author__ = "730408456"

from random import randint

HP = 100

coin: str = '\U00002B50'

points = 0

player: str = "" ""


def greet() -> None:
    global player
    player = input("What is your name? ")
    print(f"Welcome to Dungeon Fighter, {player}!")
    rules = str(input("Would you like to know the rules of the game? YES or NO: "))
    if rules == "YES":
        print("Dungeon Fighter is a turn-based fighting game. You will have the option to go up against two different opponents. ")
        print("The game is simple. Each turn, you will roll a die to determine what attack you perform. Each attack will have a different effect. ")
        print("For example, a FIREBALL attack does 20 damage to the opponent. ")
        print("After you attack, your opponent will. ")
        print("Both you and your opponent have HEALTH POINTS. Deplete your opponent's HP before yours is depleted to win. ")
    ready = str(input("Type OK to continue. "))
    if ready == "OK":
        return

            
def choose(choice: int) -> int:
    print(f"You have three choices, {player}. ")
    print("1: Fight DAVE THE ORC! A strong but stupid opponent, good for beginners! ")
    print("2: Fight RICHARD THE WIZARD! A more crafty and difficult opponent, better for advanced players! ")
    print("3: EXIT GAME ")
    choice = int(input("CHOOSE WISELY: "))
    return choice


def dave(DAVEHP: int, HP: int) -> int:
    print("DAVE THE TROLL! A fearsome opponent, but not too bright. You challenge him to a fight to the death! ")
    x = 0
    points = 0
    while HP > 0 and DAVEHP > 0:
        print("--------------------------------------------------------")
        attack = str(input("Your turn! Type ROLL to roll your die and attack! "))
        if attack == "ROLL":
            x = randint(1, 6)
            if x == 1:
                print("You rolled FIREBALL! Deal 20 damage to your opponent! ")
                DAVEHP -= 20
                print(f"DAVE's HP is now {DAVEHP}! ")
            if x == 2:
                print("You rolled SLASH! Deal 10 damage to your opponent! ")
                DAVEHP -= 10
                print(f"DAVE's HP is now {DAVEHP}! ")
            if x == 3:
                print("You rolled DOUBLE STAB! Deal 15 damage to your opponent! ")
                DAVEHP -= 15
                print(f"DAVE's HP is now {DAVEHP}! ")
            if x == 4:
                print("You rolled BLESSING! Restore 15 points of your HP! ")
                HP += 15
                print(f"Your HP is now {HP}! ")
            if x == 5:
                print("You rolled ENERGY BLAST! Deal 25 damage to your opponent! ")
                DAVEHP -= 25
                print(f"DAVE's HP is now {DAVEHP}! ")
            if x == 6:
                print("You rolled ULTIMATE DESTRUCTION! Deal 40 damage to your opponent! ")
                DAVEHP -= 40
                print(f"DAVE's HP is now {DAVEHP}! ")
            a = randint(1, 3)
            if a == 1:
                print("DAVE rolled HEADBUTT! He deals 10 damage to you! ")
                HP -= 10
                print(f"Your HP is now {HP}! ")
            if a == 2:
                print("DAVE rolled TACKLE! He deals 15 damage to you! ")
                HP -= 15
                print(f"Your HP is now {HP}! ")
            if a == 3:
                print("DAVE rolled STEAL! He deals 10 damage to you, and heals himself for 10 damage! ")
                HP -= 10
                DAVEHP += 10
                print(f"Your HP is now {HP}! DAVE's HP is now {DAVEHP}! ")
    else:
        if HP > DAVEHP:
            print("--------------------------------------------------------")
            print(f"{player} WINS! ")
            print("Your health has been restored to full. ")
            HP = 100
            print("You gained 15 points from defeating DAVE THE TROLL! ")
            points += 1
        if HP < DAVEHP:
            print("--------------------------------------------------------")
            print("You lost to DAVE THE TROLL. Here's 5 points as a consolation prize. Better luck next time! ")
            points += 0
            print("Your health has been restored to full. ")
    return points


def richard(RICHARDHP: int, HP: int, points: int) -> int:
    print("RICHARD THE WIZARD! A crafty warlock, undefeated in the dungeon arena! Fight to the death! ")
    x = 0
    while HP > 0 and RICHARDHP > 0:
        print("--------------------------------------------------------")
        attack = str(input("Your turn! Type ROLL to roll your die and attack! "))
        if attack == "ROLL":
            x = randint(1, 6)
            if x == 1:
                print("You rolled FIREBALL! Deal 20 damage to your opponent! ")
                RICHARDHP -= 20
                print(f"RICHARD's HP is now {RICHARDHP}! ")
            if x == 2:
                print("You rolled SLASH! Deal 10 damage to your opponent! ")
                RICHARDHP -= 10
                print(f"RICHARD's HP is now {RICHARDHP}! ")
            if x == 3:
                print("You rolled DOUBLE STAB! Deal 15 damage to your opponent! ")
                RICHARDHP -= 15
                print(f"RICHARD's HP is now {RICHARDHP}! ")
            if x == 4:
                print("You rolled BLESSING! Restore 15 points of your HP! ")
                HP += 15
                print(f"Your HP is now {HP}! ")
            if x == 5:
                print("You rolled ENERGY BLAST! Deal 25 damage to your opponent! ")
                RICHARDHP -= 25
                print(f"RICHARD's HP is now {RICHARDHP}! ")
            if x == 6:
                print("You rolled ULTIMATE DESTRUCTION! Deal 40 damage to your opponent! ")
                RICHARDHP -= 40
                print(f"RICHARD's HP is now {RICHARDHP}! ")
            a = randint(1, 4)
            if a == 1:
                print("RICHARD rolled VOID BOMB! He deals 20 damage to you! ")
                HP -= 20
                print(f"Your HP is now {HP}! ")
            if a == 2:
                print("RICHARD rolled ZAP! He deals 5 damage to you! ")
                HP -= 5
                print(f"Your HP is now {HP}! ")
            if a == 3:
                print("RICHARD rolled DISENTIGRATE! He deals 30 damage to you! ")
                HP -= 30
                print(f"Your HP is now {HP}! ")
            if a == 4:
                print("RICHARD rolled SIZZLE! It doesn't do any damage... ")
                print(f"Your HP is still {HP}. ")
    else:
        if HP > RICHARDHP:
            print("--------------------------------------------------------")
            print(f"{player} WINS! ")
            print("Your health has been restored to full. ")
            print("You gained 30 points from defeating RICHARD THE WIZARD! ")
            points += 30
        if HP < RICHARDHP:
            print("--------------------------------------------------------")
            print("You lost to RICHARD THE WIZARD. Here's 10 points as a consolation prize. Better luck next time! ")
            print("Your health has been restored to full. ")
            points += 10
    return points


def main() -> None:
    points = 0
    greet()
    b = 0
    while b < 1:
        print("--------------------------------------------------------")
        print(f"You have {points} points. {coin} ")
        z = choose(0)
        if z == 1:
            if dave(100, 100) == 1:
                points += 15
            else:
                points += 5
        if z == 2:
            if points < 10:
                print(f"Sorry {player}, but you do not have enough points to challenge RICHARD THE WIZARD. ")
                print("Acquire 10 points to enter the arena with RICHARD. ")
            else: 
                if richard(125, 100, points) == 1:
                    points += 30
                else:
                    points += 10

        if z == 3:
            b += 1
    else:
        print(f"Goodbye, {player}! You earned {points} points. ")
    

if __name__ == "__main__":
    main()