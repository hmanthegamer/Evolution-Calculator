import numpy
from os import listdir
from os.path import isfile, join

def get_names():
    files = [f for f in listdir("storage") if isfile(join("storage", f))]
    return(files)

def main():
    files = get_names()
    for i in files:
        pokemon = numpy.load("storage\\" + i)
        poke_num = pokemon[0]
        evolve = int(pokemon[1]) // int(pokemon[2])
        candy_remain = int(pokemon[1]) % int(pokemon[2])
        while (int(pokemon[2]) - int(candy_remain)) < (int(poke_num) - int(evolve) - 1):
            evolve += 1
            poke_num = int(poke_num) - (int(pokemon[2]) - int(candy_remain))
            evolve_remain = 0
        transfer = int(pokemon[0]) - int(poke_num)
        if evolve > 0:
            print("You can evolve", evolve, pokemon[3], "if you transfer", transfer)
def list_poke():
    files = get_names()
    for i in files:
        pokemon = numpy.load("storage\\" + i)
        print(pokemon[3])
