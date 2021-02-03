import os
import time

def clear():
    os.system('cls')

print("Welcome to my first game!")
name = input("What is your name?: ")

clear()
while True:
    try:
        age = int(input("Hi {}, how old are you?: ".format(name)))
    except ValueError:
        print("Please enter an integer number!")
        continue
    else:
        break
clear()

class character(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hp = 10
        self.record = 0
        self.weapon = None

    def add_weapon(self, weapon):
        self.weapon = weapon
        self.bullet = 0

    def add_bullet(self, bullet):
        self.bullet += bullet

    def attack(self):
        if self.weapon == 'gun':
            if self.bullet >= 1:
                self.bullet -= 1
                print("You killed a zombie!")
                self.record += 1
            else:
                self.hp -= 5
                print("You don't have enough bullets! A zombie damaged you with 5 health points.")
        else:
            self.hp -= 5
            print("You do not have any weapon! A zombie damaged you with 5 health points.")

    def remove_weapon(self):
        self.weapon = None

    def damage(self, damage):
        self.hp -= int(damage)

    def heal(self, heal):
        self.hp += int(heal)

    def check_status(self):
        if self.weapon == 'gun':
            print("You have {} health points and {} bullets left".format(self.hp, self.bullet))
        else:
            print("You have {} health points left".format(self.hp))
        if self.hp <= 0:
            print("You lost all your health points. You lost!")
            exit()
        else:
            pass

    def choices(self, choice):
        self.choice = choice
        if self.choice == 'forest':
            self.choice = 'forest'
        elif self.choice == 'watchtower':
            self.choice = 'watchtower'
        else:
            pass

    def final_record(self):
        print("FINAL RECORD: \nYou have {} health points left and killed {} zombies".format(self.hp, self.record))

def chapter_two(cls):
    if cls.choice == 'forest':
        print('You are now at the forest! \n')
        cls.check_status()
        print("Upon arriving at the forest you saw 2 zombies rushing towards you! \n")
        time.sleep(2)
        attack_or_evade = str(input("Are you going to attack them? or evade them? (attack/evade) \n")).lower()
        clear()
        if attack_or_evade == 'attack':
            cls.attack()
            cls.attack()
            cls.check_status()
            time.sleep(2)
            print("In front of you, you now see two paths. One leads deep into the forest, and the other to the watchtower. \n")
            deep_or_tower = str(input("What path will you choose? (forest/watchtower) \n")).lower()
            clear()
            if deep_or_tower == 'forest':
                print("You went to the deep forest but you were suddenly snatched by someone \n")
                time.sleep(5)
                print('TO BE CONTINUED')
                cls.final_record()
            elif deep_or_tower == 'watchtower':
                print('You are now at the watchtower. Upon gazing at the binoculars, you saw a large ship coming towards the island. \n')
                time.sleep(2)
                print("You were shocked when you saw the banner at the ship ...")
                time.sleep(5)
                print("TO BE CONTINUED")
                cls.final_record()

        elif attack_or_evade == 'evade':
            print('You have safely evaded the zombies but you were snatched by someone at the forest \n')
            time.sleep(5)
            print('TO BE CONTINUED')
            cls.final_record()


    elif cls.choice == 'watchtower':
        print('You are now at the watchtower. Upon gazing at the binoculars, you saw a large ship coming towards the island. \n')
        time.sleep(2)
        print("You were shocked when you saw the banner at the ship ...")
        time.sleep(5)
        print("TO BE CONTINUED")
        cls.final_record()

    else:
        print("You are magically transported to a different dimension!")



rob = character(name, age)

if int(rob.age) >= 18:
    print("You are old enough to play this game, {}.".format(rob.name))
    wants_to_play = str(input("Do you want to play a game?: ")).lower()
    clear()
    if wants_to_play == "yes":
        print("Let's Play! You are starting with {} health points\n".format(rob.hp))
        print("You woke up in a bed. Alone in a room with one door only.\n")
        time.sleep(2)
        print("You peeked at the door window. You saw a zombie rushing to your room")
        time.sleep(5)
        find_or_rush = str(input("What do you do? Find a weapon in the room? or rush outside when the zombie enters? (find/rush): \n")).lower()
        clear()
        if find_or_rush == 'find':
            print("You found a gun with 3 bullets!")
            rob.add_weapon('gun')
            rob.add_bullet(3)
            time.sleep(2)
            ans = input("The zombie entered the room! Are you going to attack it? or rush outside? (attack/rush) \n").lower()
            clear()
            if ans == "attack":
                rob.attack()
                rob.check_status()
                time.sleep(2)
                print("3 sleeping zombies heard the loud shot! They are now rushing towards you. \n")
                time.sleep(2)
                attack_or_rush = str(input("Are you going to attack them? or run away from them? (attack/run) \n")).lower()
                clear()
                if attack_or_rush == 'attack':
                    rob.attack()
                    rob.attack()
                    rob.attack()
                    rob.check_status()
                    print('You ran and got far from the zombie! You arrived at the forest!')
                    rob.choices('forest')
                    chapter_two(rob)
                elif attack_or_rush == 'run':
                    print("You have escaped the zombies and ran at the forest!")
                    rob.choices('forest')
                    chapter_two(rob)
                else:
                    print("You failed to decide what to do and the zombies ate you!")
            elif ans == "rush":
                print("You have escaped the zombie with your parkour skills, but you were damaged in the process losing 2 health points")
                rob.damage(2)
                rob.check_status()
                time.sleep(5)
                print("You saw 3 sleeping zombies outside but you managed to sneak past them. Now there are two roads to choose by. \n")
                forest_or_tower = str(input("One road leads to the forest, and the other to a watchtower. What path will you choose? (forest/watchtower) \n")).lower()
                clear()
                if forest_or_tower == 'forest':
                    rob.choices('forest')
                    chapter_two(rob)
                elif forest_or_tower == 'watchtower':
                    rob.choices('watchtower')
                    chapter_two(rob)
                else:
                    print("You failed to decide what to do and the 3 zombies woke up and ate you")
            else:
                print("You failed to decide what to do and the zombie ate you!")
        elif find_or_rush == 'rush':
            print("You have escaped the zombie with your parkour skills, but you were damaged in the process losing 2 health points")
            rob.damage(2)
            rob.check_status()
            time.sleep(5)
            print("You saw 3 sleeping zombies outside but you managed to sneak past them. Now there are two roads to choose by. \n")
            forest_or_tower = str(input("One road leads to the forest, and the other to a watchtower. What path will you choose? (forest/watchtower) \n")).lower()
            clear()
            if forest_or_tower == 'forest':
                rob.choices('forest')
                chapter_two(rob)
            elif forest_or_tower == 'watchtower':
                rob.choices('watchtower')
                chapter_two(rob)
            else:
                print("You failed to decide what to do and the 3 zombies woke up and ate you")
        else:
            print("You failed to decide what to do and the zombie ate you!")
    else:
        print("Understandable! Have a great day!")
else:
    print("Sorry {}, you are ineligible to play this game.")



