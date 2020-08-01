from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------')
    print('    WIZARD GAME APP')
    print('------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print("A {} of level {} appears from a dark and foggy forest...".format(
            active_creature.name, active_creature.level))
        print()

        cmd = input('[a]ttack, [r]un, [l]ook? ').lower()
        print()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("Wizard returns revitalized!")
        elif cmd == 'r':
            print("The wizard wisely flees!")
        elif cmd == 'l':
            print("The wizard {} takes in the surroundings and sees:".format(hero.name))
            for creature in creatures:
                print(" A {} or level {}".format(
                    creature.name, creature.level))
        else:
            print("OK, exiting game...BYE!")
            break

        if not creatures:
            print("{}, you've defeated all the creature!".format(hero.name))
            break

        print()


if __name__ == '__main__':
    main()
