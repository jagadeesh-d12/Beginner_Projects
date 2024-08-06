from sample_madlibs import Hp, Hunger_man, zombie
import random

if __name__ == "__main__":
    m = random.choice([Hp, Hunger_man, zombie])
    m.madlib()