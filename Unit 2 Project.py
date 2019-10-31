# I removed the time.sleep so that it was easier to go through the code if you want to see every option and not have to
# wait an extra few minutes for the new code to pop up.

# The code in the final boss room has to add up to be a total of 176 if you can't figure it out

import math  # importing
import random
import time

destiny_class = 0
edz = 0  # global variables
titan = 0
nessus = 0
io = 0
element = 0
cave_split = 0
take_back_docks = 0
red_tower = 0
find_cayde = 0
cabal_or_explore = 0
fight_irausk = 0
edz_complete = False
titan_complete = False
nessus_complete = False
io_complete = False
ghaul = 0
code = 0
final_fight = 0
super_ghaul = False
sniper_ghaul = False
thunderlord_ghaul = False
hide_ghaul = False
end_of_fight = 0
middle_of_fight = 0
start_of_fight = 0
super_ghaul2 = 0

print("Light")  # basic inputs for names and game intro
# time.sleep(3)
name = input("\nPlease enter your name.")
print("\nThe Traveler, the source of your power, was captured by the Cabal. You must escape the city and find a way to "
      "get your Light back. Without the light,\nyou cannot revive yourself."
      "")
# time.sleep(5)

choose_class = True  # while loop and a menu for choosing a class. it has a description for each class. Most of the code
# is like this
while choose_class: #this means while choose_class == True but in a shorter form.
    print("\nChoose a class\n1. Titan\n2. Hunter\n3. Warlock\n4. Random")
    destiny_class = input("What class are you?")
    if destiny_class == '1':
        print("\nTitans protect the city through strength, sacrifice, and mercilessness. They specialize in punching. "
              "They only know punch.")
        # time.sleep(3)
        print("\nDo you wish to choose the Titan?\n1. Yes\n""2. Go Back")
        titan_yesorno = input("")  # lets you go back if you don't like what you chose. There are a lot of inputs that
        # are similar below.


        if titan_yesorno == '1':
            choose_class = False

    elif destiny_class == '2':
        print("\nHunters are the most agile class. They use stealth and long range to kill.")
        # time.sleep(3)
        print("\nDo you wish to choose the Hunter?\n1. Yes\n""2. Go Back")
        hunter_yesorno = input("")

        if hunter_yesorno == '1':
            choose_class = False
    elif destiny_class == '3':
        print("\nWarlocks specialize in combining magic powers granted by The Traveler with modern weapons.")
        # time.sleep(3)
        print("\nDo you wish to choose the Warlock?\n1. Yes\n""2. Go Back")
        warlock_yesorno = input("")

        if warlock_yesorno == '1':
            choose_class = False

    elif destiny_class == '4':  # random class is chosen. it picks a random number between 1 and 3 since there are
        # 3 classes
        destiny_class = str(random.randint(1, 3))
        if destiny_class == '1':
            print("\nTitans protect the city through strength, sacrifice, and mercilessness. They specialize in "
                  "punching.They only know punch.")
            # time.sleep(3)
            print("\nDo you wish to choose the Titan?\n1. Yes\n""2. Go Back")
            titan_yesorno = input("")

            if titan_yesorno == '1':
                choose_class = False

        elif destiny_class == '2':
            print("\nHunters are the most agile class. They use stealth and long range to kill.")
            # time.sleep(3)
            print("\nDo you wish to choose the Hunter?\n1. Yes\n""2. Go Back")
            hunter_yesorno = input("")

            if hunter_yesorno == '1':
                choose_class = False
        elif destiny_class == '3':
            print("\nWarlocks specialize in combining magic powers granted by The Traveler with modern weapons.")
            # time.sleep(3) I removed these so that is wouldn't take so long to get through it
            print("\nDo you wish to choose the Warlock?\n1. Yes\n""2. Go Back")
            warlock_yesorno = input("")

            if warlock_yesorno == '1':
                choose_class = False
    else:
        print("\nWrong input. Please try again.")  # defensive code. it repeats a lot below after every while loop.
        # time.sleep(2)

gender = True

while gender:  # similar to class, just with gender
    print("\nWhat is your gender?\n1. Male\n2. Female")
    character_gender = input("")
    if character_gender == '1':
        print("\nDo you wish to be male?\n1. Yes\n""2. Go Back")
        male_yesorno = input("")

        if male_yesorno == '1':
            gender = False

    elif character_gender == '2':
        print("\nDo you wish to be female?\n1. Yes\n""2. Go Back")
        female_yesorno = input("")

        if female_yesorno == '1':
            gender = False

    else:
        print("\nWrong input. Please try again.")

fire_exit = True
print("\nYou wake up to an explosion. Surrounded by fire, you look for a way out. You find an exit and your ghost "
      "on the ground beside you.")  # first scene
while fire_exit:
    print("\n\nWhat would you like to do?\n1.Go to the exit\n2.Talk to your ghost")
    exit_or_ghost = input("")  # print menu and an input asking what you want to do
    if exit_or_ghost == '1':
        print("\nYou pick up your ghost and walk to the exit. You see the city in ruins. You have to leave before any "
              "Cabal find you.")
        fire_exit = False
        destroyed_city = True  # set this while loop false and a new one to true to switch scenes.
    elif exit_or_ghost == '2':
        print("\nThe ghost says the Cabal lord Ghaul has taken the traveller. You need to find your light to have a "
              "chance at beating him.")  # after this prints it will go back to ask what the player wants to do.
    else:
        print("\nWrong input. Please try again.")
        # time.sleep(2)

destroyed_city = True
print("\nThe exit leads outside where you see the traveller crumbling to the ground. You're reminded about what "
      "the "
      "ghost said. You sneak past the Cabal and into the mountains. You see a hawk circle around you then fly off "
      "into the distance.")  # description
while destroyed_city:
    print("\nWhat would you like to do?\n1. Follow it\n2. Take a break")
    destroyed_city = input("")  # input
    if destroyed_city == '1':
        destroyed_city = False
    elif destroyed_city == '2':
        print("\nYou sit down and take a break. This calmness is quickly interrupted by Cabal War Beasts chasing you."
              "You have to run.")
        destroyed_city = '1'
    else:
        print("\nWrong input. Please try again.")
print("\nYou follow the bird through the mountains and find a group of humans. The leader introduces herself "
      "as Hawthorne. She is a friend of Zavala, the Vanguard leader. You see her as an ally. They tell you about a "
      "Shard of the Traveller. Something that might bring your light back.")

get_light = True
while get_light:
    print("\nWhat would you like to do?\n1. Follow them to the Shard\n2. Explore the area")
    get_light = input("")  # input what to do
    if get_light == '1':
        print("You make your way to the Shard. You reach out to touch it. A surge of power enters your body, making you"
              " feel refreshed. Cabal appear from the trees and start running at you. You can now fight back with your "
              "power.\nWhat element would you like to use?\n1. Arc\n2. Void\n3. Solar")
        element = input("")
        if element == '1' and destiny_class == '1':  # choose was element you want to be
            print("You cast Fists of Havoc. The ground crackles as your Fists of Havoc activates. You shoulder charge "
                  "into every Cabal in your "  # depending on what you pick, you get a certain line to match
                  "way.")
            get_light = False
        elif element == '1' and destiny_class == '2':  # example: element 1 is arc and destinyclass 2 is hunter
            print("You cast Arc Staff. You conjure a staff of arc light. You slice through each Cabal as you watch "
                  "them crackle. ")  # so you get an arc hunter super as your line.
            get_light = False
        elif element == '1' and destiny_class == '3':
            print("You cast Stormtrance. You start to levitate as lightning blazes out of your fingertips. You "
                  "electrocute all Cabal in your "
                  "path")
            get_light = False
        elif element == '2' and destiny_class == '1':
            print("You cast Sentinel Shield. Your Sentinel Shield appears on your arm. You throw it at the Cabal, "
                  "watching it bounce off each "
                  "enemy until they are all dead. ")
            get_light = False
        elif element == '2' and destiny_class == '2':
            print("You cast Shadowshot. You shoot a Void Anchor at your enemies, slowing them and killing them in "
                  "the process.")
            get_light = False
        elif element == '2' and destiny_class == '3':
            print("You cast Nova Bomb. You hurl an explosive bolt of Void Light at the Cabal, obliterating everything "
                  "around you.")
            get_light = False
        elif element == '3' and destiny_class == '1':
            print("You cast Hammer of Sol. You hurl fire-forges hammers at the Cabal as they helplessly run to find "
                  "cover.")
            get_light = False
        elif element == '3' and destiny_class == '2':
            print("You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets at the "
                  "Cabal.")
            get_light = False
        elif element == '3' and destiny_class == '3':
            print("You cast Daybreak. You weave Solar Light into blades and smite the Cabal from the skies.")
            get_light = False
        else:
            print("\nWrong input. Please try again.")

    elif get_light == '2':
        print("You look around to explore the area. Hawthorne says they are surrounded. Going too far will get you "
              "killed. She says you need to get your light back.")
        get_light = '1'
    else:
        print("\nWrong input. Please try again.")
print("\nYou return to Hawthorne with your powers. She says she can bring you to other survivors. It is in a place "
      "called the farm")
to_farm = True
print("You reunite with Zavala at the farm. Your time there is short as he commands you to take back one of their "
      "planets.")
while to_farm:
    print("\nWhere would you like to go?\n1. EDZ\n2. Titan\n3. Nessus\n4. IO \n5. Random\nYou will end up having "
          "to do all of them")
    planet = input("")  # general hub of the main storyline. there is a list of planets in a while loop in menu form
    if planet == '1':
        edz = True  # sets the planet and its first scene to true to start it
        cave_split = True
    elif planet == '2':
        titan = True
        take_back_docks = True
    elif planet == '3':
        nessus = True
        find_cayde = True
    elif planet == '4':
        io = True
    elif planet == '5':  # if you want to start randomly
        planet = str(random.randint(1, 4))
        if planet == '1':
            edz = True
            cave_split = True
        elif planet == '2':
            titan = True
            take_back_docks = True
        elif planet == '3':
            nessus = True
            find_cayde = True
        elif planet == '4':
            io = True
            cabal_or_explore = True
    else:
        print("\nWrong input. Please try again.")

    while edz:
        print("You meet up with Devrim Kay by the abandoned church. He tells you to go to the Salt Mines and kill the "
              "Major Servitor hiding in there. He is causing disturbances in the mines and needs to be taken out. "
              "You agree and enter. As you walk, you find a fork in the cave.")
        while cave_split:
            print("\nWhich path would you like to pick?"
                  "\n1. Straight, spooky path\n2. Long, windy, path")
            long_or_straight = input("")
            if long_or_straight == '1':
                print(
                    "\nYou start walking down the path. You are greeted by a Fallen captain. They begin running at you."
                    "\n"
                    "\nWhat would you like to do?\n1. Fight (You probably shouldn't)\n2. Run (You probably should) ")
                cave_fightrun = input("")
                if cave_fightrun == '1':  # similar while loops with different texts
                    print("You try and shoot the captain, but he is too powerful. Without your full potential unlocked,"
                          " you are K.O'd in one hit. You Died.\nYou respawn back at the fork in the cave.")
                elif cave_fightrun == '2':
                    print("You run away from the captain and back to the fork in the cave.")
                else:
                    print("\nWrong input. Please try again.")
            elif long_or_straight == '2':
                print(
                    "As you walk down the windy path, you see laser tripwires scattered all around the walls.\n\nWhat "
                    "would you like to do?\n1. Run through the lasers as fast as you can\n2. Throw a rock through "
                    "the lasers")
                rock_or_run = input("")
                if rock_or_run == '1':
                    print("Your immense speed allows you to zip past the mines. They detonate behind you and the "
                          "shockwave throws you into a wall. You reach low health but are still living. You take a "
                          "short break.")
                    cave_split = False
                elif rock_or_run == '2':  # like the choose element area, you destroy the rocks with your chosen element
                    # and class. Similar things keep happening below
                    print("The rock hits the ground echoing at the end of the tunnel. The sound if closely followed by "
                          "a large explosion. Rocks crumble to the ground and your path is blocked.")
                    if element == '1' and destiny_class == '1':
                        print(
                            "You cast Fists of Havoc. Your explosive arc damage destroys the rocks in the way.")
                        cave_split = False
                    elif element == '1' and destiny_class == '2':
                        print(
                            "You cast Arc Staff. You slice the rocks until there are none left.")
                        cave_split = False
                    elif element == '1' and destiny_class == '3':
                        print(
                            "You cast Stormtrance. You zap the rocks until they are tiny sediments and your way is "
                            "clear.")
                        cave_split = False
                    elif element == '2' and destiny_class == '1':
                        print(
                            "You cast Sentinel Shield. You slice them apart and clear the way. ")
                        cave_split = False
                    elif element == '2' and destiny_class == '2':
                        print(
                            "You cast Shadowshot. The rocks slowly crumble in its wake and the way is clear.")
                        cave_split = False
                    elif element == '2' and destiny_class == '3':
                        print(
                            "You cast Nova Bomb. You hurl an explosive bolt of Void Light, obliterating the rocks.")
                        cave_split = False
                    elif element == '3' and destiny_class == '1':
                        print(
                            "You cast Hammer of Sol. You hurl fire-forges hammers at the rocks, clearing the way.")
                        cave_split = False
                    elif element == '3' and destiny_class == '2':
                        print(
                            "You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets at "
                            "the rocks until they are no more.")
                        cave_split = False
                    elif element == '3' and destiny_class == '3':
                        print(
                            "You cast Daybreak. You weave Solar Light into blades and slice the rocks until the path"
                            " is clear.")
                        cave_split = False

                else:
                    print("\nWrong input. Please try again.")
            else:
                print("\nWrong input. Please try again.")
        combustion_boss = True
        print("\nYou make your way through the mines and find an elevator. Access to it is blocked by the servitor "
              "Devrim was talking about.")
        while combustion_boss:
            print("\nWhat would you like to do?\n1. Throw a grenade\n2. Use your auto rifle\n3. Use your sniper\n4. "
                  "Random weapon")
            combustion_boss_weapon = input("")
            if combustion_boss_weapon == '1':
                print("You throw a grenade at the servitor. It bounces off of it and deals no damage. The servitor"
                      " shoots purple laser balls at you and gets you in the leg.\n\nWhat would you like to do?\n1."
                      " run\n2. 360 NoScope the servitor")
                combustion_boss_runorsnipe = input("")
                if combustion_boss_runorsnipe == '1':
                    print("You try to run but the servitor hits you again. You die and respawn back to before you see "
                          "the servitor.") # you die here so it will send you back to the while loop after printing this
                elif combustion_boss_runorsnipe == '2':
                    print("You jump out from behind a rock with your sniper out. You try and 360 NoScope the servitor "
                          "but your aim is terrible. You get hit by more lasers and die. You respawn back to before you"
                          " see the servitor.")
                else:
                    print("\nWrong input. Please try again.")
            elif combustion_boss_weapon == '2':
                if destiny_class == '1':  # this is what kills the boss, so it is what sets the while loop to false
                    print("You spray the servitor with your auto rifle, making it flinch. You also have your rally "
                          "barricade allowing you to auto reload and finish off the servitor easily.")
                    combustion_boss = False
                    combustion_boss_weapon = False
                elif destiny_class == '2':
                    print("You spray the servitor with your auto rifle, making it flinch. The servitor gets in close, "
                          "but you dodge out of the way and can keep your distance so you can finish it off from afar.")
                    combustion_boss = False
                    combustion_boss_weapon = False
                elif destiny_class == '3':
                    print("You spray the servitor with your auto rifle, making it flinch. You have your healing rift"
                          "to keep you alive for the time you need to reload. You finish it off with ease and full "
                          "health.")
                    combustion_boss = False
                    combustion_boss_weapon = False
                else:
                    print("\nWrong input. Please try again.")
            elif combustion_boss_weapon == '3':
                print("You try to pull out your sniper to kill the servitor. You forget your aim is garbage and you "
                      "miss horribly. You die and respawn before you reach the servitor.")
            elif combustion_boss_weapon == '4':  # another use of random
                combustion_boss_weapon = str(random.randint(1, 3))
                if combustion_boss_weapon == '1':
                    print("You throw a grenade at the servitor. It bounces off of it and deals no damage. The servitor"
                          " shoots purple laser balls at you and gets you in the leg.\nWhat would you like to do?\n1."
                          " run\n2. 360 NoScope the servitor")
                    combustion_boss_runorsnipe = input("")
                    if combustion_boss_runorsnipe == '1':
                        print(
                            "You try to run but the servitor hits you again. You die and respawn back to before you see"
                            " the servitor.")
                    elif combustion_boss_runorsnipe == '2':
                        print(
                            "You jump out from behind a rock with your sniper out. You try and 360 NoScope the "
                            "servitor but your aim is terrible. You get hit by more lasers and die. You respawn back to"
                            " before you see the servitor.")
                    else:
                        print("\nWrong input. Please try again.")
                if combustion_boss_weapon == '2':  # again, different line depending on class
                    if destiny_class == '1':
                        print("You spray the servitor with your auto rifle, making it flinch. You also have your rally "
                              "barricade allowing you to auto reload and finish off the servitor easily.")
                        combustion_boss = False
                        combustion_boss_weapon = False
                    elif destiny_class == '2':
                        print(
                            "You spray the servitor with your auto rifle, making it flinch. The servitor gets in close,"
                            " but you dodge out of the way and can keep your distance so you can finish it off from "
                            "afar.")
                        combustion_boss = False
                        combustion_boss_weapon = False
                    elif destiny_class == '3':
                        print(
                            "You spray the servitor with your auto rifle, making it flinch. You have your healing rift"
                            "to keep you alive for the time you need to reload. You finish it off with ease and full "
                            "health.")
                        combustion_boss = False
                        combustion_boss_weapon = False

                elif combustion_boss_weapon == '3':
                    print(
                        "You try to pull out your sniper to kill the servitor. You forget your aim is garbage and you "
                        "miss horribly. You die and respawn before you reach the servitor.")
                else:
                    print("\nWrong input. Please try again.")
            else:
                print("\nWrong input. Please try again.")
        print("You get it into the elevator and make your way back to Devrim. Information from the servitor reads: "
              "12\n\nYou have completed the EDZ.")
        # the edz concludes and it is set to false. it sets edz_complete to true and checks if all planets are done.
        # if it is true, to_farm is set to false and you are sent to the final boss. if not, it sends you back to
        # complete another planet.
        edz = False
        edz_complete = True
        if edz_complete == True and titan_complete == True and nessus_complete == True and io_complete == True:
            to_farm = False
            ghaul = True

    while titan:
        print("\nYou meet up with Sloane, another friend of Zavala's. She tells you that the control centre is swarmed"
              " by the hive.\nYou make your way through to the centre. You find yourself standing in front of a spooky "
              "red tower. You turn around and see hive surrounding you.\n")
        while take_back_docks:
            print("\nWhat would you like to do?\n1. Fight the Hive\n2. Run into the tower")
            fighthive_or_run = input("")
            if fighthive_or_run == '1':
                print("You fight the hive. You lose your balance and almost fall into the abyss of water below. "
                      "You regain your balance at the last second and finish off the hive. Your only way to the "
                      "control centre is through the red tower. You enter.")
                take_back_docks = False
                red_tower = True
            elif fighthive_or_run == '2':
                print("You run into the tower but get killed by the hive surrounding you.\n")

            else:
                print("\nWrong input. Please try again.")
        print("You go up the red tower and are greeted by a hive knight.")
        while red_tower:
            print("What would you like to do?\n1. Fight back\n2. Hide")
            fight_hide = input("")
            if fight_hide == '1':
                print("You pull out your sniper and hit the knight in the head. It's a complete fluke, but you kill it."
                      " You make it through to the control centre.")
                red_tower = False
            elif fight_hide == '2':
                print("You hide behind some sandbags nearby. The hive doesn't seem to notice you. Looking around, you "
                      "see a small hole around the knight you can fit through. \nWhat would you like to do?\n1. "
                      "Crawl through\n2. Fight the Knight")
                fight_crawl = input("")
                if fight_crawl == '1':
                    print("You sneak past the knight and reach the control centre.")
                    red_tower = False
                elif fight_crawl == '2':
                    print("You charge at the knight with your auto rifle. It slashes you with it's sword. knocking"
                          " you into the water. You respawn back before you see the knight.")
                else:
                    print("\nWrong input. Please try again.")
            else:
                print("\nWrong input. Please try again.")
        print("You reach the control centre and restore power to the docks. Sloane meets up with you and thanks you. "
              "Information from the Knight reads: 69\nYou have completed Titan")
        titan = False
        titan_complete = True
        if edz_complete == True and titan_complete == True and nessus_complete == True and io_complete == True:
            to_farm = False
            ghaul = True

    while nessus:
        print("You are tasked with finding Cayde-6. You find him as soon as you enter Nessus. He is stuck in a "
              "teleportation loop. He yells for help, but vanishes out of your sight once the teleporter activates"
              ". Your ghost senses his presence further in the Vex cave. As you walk, you see a shiny thing.")
        while find_cayde:
            print("What would you like to do?\n1. Follow him\n2. Check out the shiny thing")
            shine_or_cayde = input("")
            if shine_or_cayde == '1':
                print("You walk further into the cave for what seems like hours. After reaching the area your ghost "
                      "senses Cayde, you are confronted by a Hydra, a mechanical monster with a rotating shield"
                      "\nWhat would you like to do?\n1. Use you super\n2. Use your power ammo")
                super_or_power = input("")
                if super_or_power == '1':
                    if element == '1' and destiny_class == '1':
                        print("You cast Fists of Havoc. Your explosive arc damage takes the hydra to 1HP."
                              "\n\nWould you like to use your rocket launcher to finish it off? There is a 50% "
                              "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(
                                random.randint(1, 2))  # randomly chooses whether or not it shoot using random
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '1' and destiny_class == '2':
                        print(
                            "You cast Arc Staff. Your explosive arc damage takes the hydra to 1HP."
                            "\n\nWould you like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '1' and destiny_class == '3':
                        print(
                            "You cast Stormtrance. Your explosive arc damage takes the hydra to 1HP. \n\nWould you "
                            "like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '2' and destiny_class == '1':
                        print(
                            "You cast Sentinel Shield. Your explosive void damage takes the hydra to 1HP."
                            " \n\nWould you like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '2' and destiny_class == '2':
                        print(
                            "You cast Shadowshot. Your explosive void damage takes the hydra to 1HP. \n\nWould you "
                            "like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '3' and destiny_class == '1':
                        print(
                            "You cast Hammer of Sol. Your explosive solar damage takes the hydra to 1HP. "
                            "\n\nWould you like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '3' and destiny_class == '2':
                        print(
                            "You cast Golden Gun. Your explosive solar damage takes the hydra to 1HP. \n\nWould you"
                            " like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                    elif element == '3' and destiny_class == '3':
                        print(
                            "You cast Daybreak. Your explosive solar damage takes the hydra to 1HP. \n\nWould you"
                            " like to use your rocket launcher to finish it off? There is a 50% "
                            "chance of it missing.\n1. Yes\n2. No, use my auto rifle")
                        rpg_yesorno = input("")
                        if rpg_yesorno == '1':
                            shootrpg = str(random.randint(1, 2))
                            if shootrpg == '1':
                                print("The rpg hit. You killed the hydra.")
                                find_cayde = False
                            elif shootrpg == '2':
                                print("The rpg missed. However, you were able to recover and finish off the "
                                      "hydra with your auto rifle")
                        elif rpg_yesorno == '2':
                            print("You finish off the Hydra with ease with your auto rifle, but there was no "
                                  "cool explosion.")
                            find_cayde = False
                        else:
                            print("\nWrong input. Please try again.")
                elif super_or_power == '2':
                    print("You take out your Thunderlord and spam bullets into the Hydra's skull. ")
                    find_cayde = False
                else:
                    print("\nWrong input. Please try again.")
            elif shine_or_cayde == '2':
                print("You check out the shiny object. When you pick it up, it seems as though it is only a useless"
                      " metal rock reflecting light.")
            else:
                print("\nWrong input. Please try again.")

        print("You free Cayde-6 from the teleportation loop the hydra was keeping him in. He thanks you. The "
              "information from the Hydra reads: 43 \nYou have "
              "completed Nessus")
        nessus = False
        nessus_complete = True
        if edz_complete == True and titan_complete == True and nessus_complete == True and io_complete == True:
            to_farm = False
            ghaul = True

    while io:
        print("You meet Ikora. She explains there is a disturbance in the Light here in IO. You go investigate. "
              "You come across an army of Taken Cabal funnelling the Traveler's Light into the sky. They are located"
              " in a small run-down facility.")
        cabal_or_explore = True
        while cabal_or_explore:
            print("\nWhat would you like to do?\n1. Go in head first and attack\n2. See what they are up to. Go sneaky-"
                  "beaky-like")
            attack_or_sneak = input("")
            if attack_or_sneak == '1':
                print("You run in and kill the first few Taken Cabal. As you attack the next one, you feel the power of"
                      " the corrupt light suck you in and consume you. You respawn back at the entrance to the "
                      "facility")
            elif attack_or_sneak == '2':
                print("You sneak around the facility. You notice a control panel heavily guarded by the Taken Cabal."
                      " Beside the door to the controls, you notice a couple of barrels.")

                control_panel_io = True

                while control_panel_io:
                    blow_up_barrels = input("\nWhat would you like to do?\n1. Shoot the barrels, hoping they have "
                                            "explosives inside of them\n2. Wait for the Taken Cabal to leave")
                    if blow_up_barrels == '1':
                        print("You shoot the barrels and see a large explosion. After the smoke clears, the Taken Cabal"
                              " are sent into panic. You see an opportunity to get to the control panel. When you get "
                              "there, you see multiple buttons.\nWhat would you like to do?\n1. Blue Button\n2. "
                              "Red Button\n3. Yellow Button\n4. Orange Button\n5. Random Button")
                        button_choose = input("")  # random use when picking a button to press
                        if button_choose == '1':
                            print("You chose the blue button. The control panel explodes and you die.")
                        elif button_choose == '2':
                            print("You chose the red button. An alarm goes off and you are surrounded by Taken "
                                  "Cabal. You try to fight them off but their numbers overwhelm you. You die")
                        elif button_choose == '3':
                            print("You chose the yellow button. You hear a 'ding' sound and the corruption of Light "
                                  "fades. A Taken Centurion, Irausk, Herald of Savathun.")
                            cabal_or_explore = False
                            control_panel_io = False
                            fight_irausk = True
                        elif button_choose == '4':
                            print("A chute under you opens and you fall. You die of fall damage.")
                        elif button_choose == '5':
                            button_choose = str(random.randint(1, 4))
                            if button_choose == '1':
                                print("You chose the blue button. The control panel explodes and you die.")
                            elif button_choose == '2':
                                print("You chose the red button. An alarm goes off and you are surrounded by Taken "
                                      "Cabal. You try to fight them off but their numbers overwhelm you. You die")
                            elif button_choose == '3':
                                print(
                                    "You chose the yellow button. You hear a 'ding' sound and the corruption of Light "
                                    "fades. A Taken Centurion, Irausk, Herald of Savathun.")
                                cabal_or_explore = False
                                control_panel_io = False
                                fight_irausk = True
                            elif button_choose == '4':
                                print("A chute under you opens and you fall. You die of fall damage.")
                            else:
                                print("\nWrong input. Please try again.")
                    elif blow_up_barrels == '2':
                        print("You wait for a few hours hidden behind a garbage can. You start getting bored out of "
                              "your mind")

                    else:
                        print("\nWrong input. Please try again.")
            else:
                print("\nWrong input. Please try again.")
        while fight_irausk:
            print("You run out of the facility and confront the centurion. Your power is no match for it. You need "
                  "to find another way to kill it. It lunges toward you. A giant Taken ball of light zips through the "
                  "air. It narrowly misses you.\nWhat would you like to do?\n1. Deflect the next attack with your sword"
                  "\n2. Attack it now")
            deflect_or_attack = input("")
            if deflect_or_attack == '1':
                print("You deflect the next attack with your sword. It works, sending the ball back to the centurion. "
                      "The ball pierces him, creating a huge explosion. Once the smoke clears, you see the defeated "
                      "Cabal, no longer taken.")
                fight_irausk = False
            if deflect_or_attack == '2':
                print("You know that you are no match for the centurion, but attack anyway. It punches you into the "
                      "ground, killing you instantly.")

            else:
                print("\nWrong input. Please try again.")

        print("You return to Ikora with the good news. She thanks you. The information from the Centurion reads: 52"
              "\nYou have completed IO.")
        io = False
        io_complete = True
        if edz_complete == True and titan_complete == True and nessus_complete == True and io_complete == True:
            to_farm = False
            ghaul = True

while ghaul:  # this is activated when all planets are complete.
    print("You head back to the EDZ to finish off Ghaul once and for all. His evil schemes you've been stopping must "
          "come to an end. Zavala, Ikora, Hawthorne and the Vanguard all attack the city to create a distraction."
          " You are able to sneak onto the Almighty, Ghaul's ship, and infiltrate it. \n\nYou make it to the throne "
          "room undetected. Thanks to the Vanguard, the majority of the Cabal are fighting in the city.")
    throne_room = True
    while throne_room:
        print("\nWhat would you like to do?\n1. Enter the room\n2. Chicken out")
        enter_or_not = input("")
        if enter_or_not == '1':
            print("You reach the door, but it needs a special code.")
            planetnumber = 1
            total_code = 0
            for x in range(0, 4):  # asks you for 4 numbers you saw at each of the 4 planets
                # they add of to 176 as they are 12, 43, 69 and 52.
                # It checks if it equals 176 then if it doesn, it moves on. if it doesn't, it asks again.
                code = int(input('Please enter the number from planet ' + str(planetnumber) + '. '))
                planetnumber += 1  # it adds 1 to planet number so it asks "enter number for planet 1" then
                # "enter number for planet 2" and so on
                total_code += code  # add code to total code so it keeps the values of what is input.
            if total_code == 176:
                print("The door unlocks. Ghaul appears. 'I've been expecting you, ", name, ". Welcome to your "
                                                                                           "downfall.' You know this is it. You have to defeat Ghaul if humanity wants another chance "
                                                                                           "at survival.")  # uses name so the boss addresses the player
                throne_room = False
                final_fight = True
                start_of_fight = True
            else:
                print("error... access denied")  # if it doesn't equal 176
        elif enter_or_not == '2':
            print("You can't chicken out now! Go fight Ghaul!")
        else:
            print("\nWrong input. Please try again.")
    while final_fight:

        while start_of_fight:
            print("\nWhat would you like to do?\n1. Taunt him by doing a dance\n2. Draw your weapon")
            dance_or_fight = input("")
            if dance_or_fight == '1':
                print(
                    "You whip and nae nae in front of Ghaul. He gets angry as his terrifying power doesn't phase you. He"
                    "runs are you with his hand cannon, firing after every step. You are able to dodge all of them, "
                    "forcing him to reload.")
                start_of_fight = False
                middle_of_fight = True
            if dance_or_fight == '2':
                print(
                    "You draw your sniper. He runs are you with his hand cannon, firing after every step. You are able "
                    "to dodge all of them, forcing him to reload.")
                start_of_fight = False
                middle_of_fight = True

        while middle_of_fight:
            print("\nWhat would you like to do?\n1. Cast you super\n2. Use your sniper\n3. Pull"
                  " out your Thunderlord\n4. Hide\n5. Random")
            ghaul_attack1 = input("")
            if ghaul_attack1 == '1':
                super_ghaul = True
                if element == '1' and destiny_class == '1':
                    print(
                        "You cast Fists of Havoc. Your explosive arc damage hits Ghaul causing him to stagger back.")
                    middle_of_fight = False
                elif element == '1' and destiny_class == '2':
                    print(
                        "You cast Arc Staff. You slice Ghaul and cause him to stagger.")
                    middle_of_fight = False
                elif element == '1' and destiny_class == '3':
                    print(
                        "You cast Stormtrance. You electrocute Ghaul causing him to stagger")
                    middle_of_fight = False
                elif element == '2' and destiny_class == '1':
                    print(
                        "You cast Sentinel Shield. You slice Ghaul with your shield, causing him to stagger.")
                    middle_of_fight = False
                elif element == '2' and destiny_class == '2':
                    print(
                        "You cast Shadowshot. Ghaul slows and staggers. You throw in your grenade for extra damage."
                        "Ghaul staggers.")
                    middle_of_fight = False
                elif element == '2' and destiny_class == '3':
                    print(
                        "You cast Nova Bomb. You hurl an explosive bolt of Void Light causing Ghaul to stagger.")
                    middle_of_fight = False
                elif element == '3' and destiny_class == '1':
                    print(
                        "You cast Hammer of Sol. You hurl fire-forges hammers at Ghaul, causing him to stagger.")
                    middle_of_fight = False
                elif element == '3' and destiny_class == '2':
                    print(
                        "You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets at "
                        "Ghaul. He staggers")
                    middle_of_fight = False
                elif element == '3' and destiny_class == '3':
                    print(
                        "You cast Daybreak. You weave Solar Light into blades and slice Ghaul, causing him to stagger")
                    middle_of_fight = False
                else:
                    print("\nWrong input. Please try again.")

            elif ghaul_attack1 == '2':
                print("You take you your Beloved sniper and hit Ghaul in the body. He staggers back.")
                middle_of_fight = False
                super_ghaul = True
            elif ghaul_attack1 == '3':
                print("Your Thunderlord starts melting Ghaul but he uses the energy of it and funnels it back into "
                      "you. You die")
            elif ghaul_attack1 == '4':
                print("You try to hide but Ghaul knows where you are. The pillar you hide behind is obliterated along "
                      "with you.")
            elif ghaul_attack1 == '5':
                ghaul_attack1 = str(random.randint(1, 4))
                if ghaul_attack1 == '1':
                    super_ghaul = True
                    if element == '1' and destiny_class == '1':
                        print(
                            "You cast Fists of Havoc. Your explosive arc damage hits Ghaul causing him to stagger back.")
                        middle_of_fight = False
                    elif element == '1' and destiny_class == '2':
                        print(
                            "You cast Arc Staff. You slice Ghaul and cause him to stagger.")
                        middle_of_fight = False
                    elif element == '1' and destiny_class == '3':
                        print(
                            "You cast Stormtrance. You electrocute Ghaul causing him to stagger")
                        middle_of_fight = False
                    elif element == '2' and destiny_class == '1':
                        print(
                            "You cast Sentinel Shield. You slice Ghaul with your shield, causing him to stagger.")
                        middle_of_fight = False
                    elif element == '2' and destiny_class == '2':
                        print(
                            "You cast Shadowshot. Ghaul slows and staggers. You throw in your grenade for extra damage."
                            "Ghaul staggers.")
                        middle_of_fight = False
                    elif element == '2' and destiny_class == '3':
                        print(
                            "You cast Nova Bomb. You hurl an explosive bolt of Void Light causing Ghaul to stagger.")
                        middle_of_fight = False
                    elif element == '3' and destiny_class == '1':
                        print(
                            "You cast Hammer of Sol. You hurl fire-forges hammers at Ghaul, causing him to stagger.")
                        middle_of_fight = False
                    elif element == '3' and destiny_class == '2':
                        print(
                            "You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets at "
                            "Ghaul. He staggers")
                        middle_of_fight = False
                    elif element == '3' and destiny_class == '3':
                        print(
                            "You cast Daybreak. You weave Solar Light into blades and slice Ghaul, causing him to stagger")
                        middle_of_fight = False
                    else:
                        print("\nWrong input. Please try again.")

                elif ghaul_attack1 == '2':
                    print("You take you your Beloved sniper and hit Ghaul in the body. He staggers back.")
                    middle_of_fight = False

                elif ghaul_attack1 == '3':
                    print("Your Thunderlord starts melting Ghaul but he uses the energy of it and funnels it back into "
                          "you. You die")
                elif ghaul_attack1 == '4':
                    print(
                        "You try to hide but Ghaul knows where you are. The pillar you hide behind is obliterated along "
                        "with you.")
                else:
                    print("Wrong input. Please try again.")

        while super_ghaul:
            print("Ghaul is now at half health. He becomes enrages. His power increases, but he is stuck in place "
                  "regenerating. Now is your chance. You see a column of boundless light. It restores your super"
                  "fully.")
            super_ghaul2 = True
            while super_ghaul2:
                print("\nWhat would you like to do?\n1. Restore your super\n2. Snipe Ghaul")
                restore_or_snipe = input("")
                if restore_or_snipe == '1':
                    print("You dive to the column of boundless light. It restores your super. While Ghaul is still"
                          " regenerating, ")
                    if element == '1' and destiny_class == '1':
                        print(
                            "you cast Fists of Havoc. Your explosive arc damage electrocutes Ghaul to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '1' and destiny_class == '2':
                        print(
                            "You cast Arc Staff. You slice Ghaul and electrocute him to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '1' and destiny_class == '3':
                        print(
                            "You cast Stormtrance. You electrocute Ghaul to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '2' and destiny_class == '1':
                        print(
                            "You cast Sentinel Shield. You slice Ghaul to shreds as he falls to the ground.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '2' and destiny_class == '2':
                        print(
                            "You cast Shadowshot. Ghaul's regeneration is slowed. Your void light slowly shreds"
                            " him apart.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '2' and destiny_class == '3':
                        print(
                            "You cast Nova Bomb. You hurl an explosive bolt of Void Light obliterating Ghaul.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '3' and destiny_class == '1':
                        print(
                            "You cast Hammer of Sol. You hurl fire-forges hammers at Ghaul, slowly melting Ghaul.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '3' and destiny_class == '2':
                        print(
                            "You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets "
                            "at Ghaul and exploding him to bits.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    elif element == '3' and destiny_class == '3':
                        print(
                            "You cast Daybreak. You weave Solar Light into blades and slice Ghaul to shreds.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True
                    else:
                        print("\nWrong input. Please try again.")

                if restore_or_snipe == '2':
                    print("You try to pull out your sniper to hit him. You are too slow to do so and Ghaul attacks in "
                          "a split second. You are immediately killed.")

        while sniper_ghaul:
            print("Ghaul is now at 3/4 health.\nWhat would you like to do?\n1. Snipe again\n2. Thunderlord")
            snipe_or_thunderlord = input("")
            if snipe_or_thunderlord == '1':
                print("You shoot once more, hitting him in a the head. He staggers once more.")
                sniper_ghaul = False
                super_ghaul = True

        while super_ghaul:
            print("Ghaul is now at half health. He becomes enraged. His power increases, but he is stuck in place "
                  "regenerating. Now is your chance. You see a column of boundless light. It restores your super"
                  "fully.")
            super_ghaul2 = True
            while super_ghaul2:
                print("\nWhat would you like to do?\n1. Restore your super\n2. Snipe Ghaul")
                restore_or_snipe = input("")
                if restore_or_snipe == '1':
                    print("You dive to the column of boundless light. It restores your super. While Ghaul is still"
                          " regenerating, ")
                    if element == '1' and destiny_class == '1':
                        print(
                            "you cast Fists of Havoc. Your explosive arc damage electrocutes Ghaul to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '1' and destiny_class == '2':
                        print(
                            "You cast Arc Staff. You slice Ghaul and electrocute him to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '1' and destiny_class == '3':
                        print(
                            "You cast Stormtrance. You electrocute Ghaul to a crisp.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '2' and destiny_class == '1':
                        print(
                            "You cast Sentinel Shield. You slice Ghaul to shreds as he falls to the ground.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '2' and destiny_class == '2':
                        print(
                            "You cast Shadowshot. Ghaul's regeneration is slowed. Your void light slowly shreds"
                            " him apart.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '2' and destiny_class == '3':
                        print(
                            "You cast Nova Bomb. You hurl an explosive bolt of Void Light obliterating Ghaul.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '3' and destiny_class == '1':
                        print(
                            "You cast Hammer of Sol. You hurl fire-forges hammers at Ghaul, slowly melting Ghaul.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True

                    elif element == '3' and destiny_class == '2':
                        print(
                            "You cast Golden Gun. You fuel your pistol with solar light, shooting explosive bullets "
                            "at Ghaul and exploding him to bits.")
                        super_ghaul2 = False
                    elif element == '3' and destiny_class == '3':
                        print(
                            "You cast Daybreak. You weave Solar Light into blades and slice Ghaul to shreds.")
                        super_ghaul2 = False
                        super_ghaul = False
                        end_of_fight = True


                    else:
                        print("\nWrong input. Please try again.")

                if restore_or_snipe == '2':
                    print(
                        "You try to pull out your sniper to hit him. You are too slow to do so and Ghaul attacks in "
                        "a split second. You are immediately killed.")

        while end_of_fight:
            print("Ghaul collapses to the ground, groaning. The traveler's light pierces his body as he slowly fades "
                  "away. \n\nYou make it back to the Farm. Reuniting with everyone else, you celebrate your saving of"
                  " humanity.")
            end_of_fight = False  # you finish the game and you win!
