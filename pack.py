import numpy

def main():
    name = input("Name: ")
    number_pokemon = input("Number of the Pokemon: ")
    number_candies = input("Number of candies: ")
    evolve = input("Amount of candies required to evolve: ")

    poke = [number_pokemon, number_candies, evolve, name]

    numpy.save("storage\\" + name, poke)

    ask = input("Add any character here to stop adding pokemon: ")
    return(ask)

def catch():
    name = input("Which Pokemon did you catch? ")
    number = int(input("How many? "))
    poke = numpy.load("storage\\" + name + ".npy")
    poke[0] = int(poke[0]) + number
    poke[1] = int(poke[1]) + (number * 3)
    numpy.save("storage\\" + name + ".npy", poke)
