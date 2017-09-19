import numpy

def main():
    name = input("Name: ")
    number_pokemon = input("Number of the Pokemon: ")
    number_candies = input("Number of candies: ")
    evolve = input("Amount of candies required to evolve: ")

    poke = [number_pokemon,number_candies,evolve]

    numpy.save("storage\\"+name,poke)

    ask = input("Add any character here to stop adding pokemon: ")
    return(ask)
