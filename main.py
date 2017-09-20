import pack, load, os

def main():
    setup()
    while True:
        x = str.lower(input("GO: "))
        if x == "add":
            cont = ""
            while cont == "":
                cont = pack.main()
        elif x == "out":
            load.main()
        elif x == "list":
            load.list_poke()
        elif x == "del":
            load.delete()
        elif x == "help":
            print("Commands:"
                  "\nadd = regester a new Pokemon"
                  "\nout = output how many Pokemon you can evolve"
                  "\nlist = list all Pokemon you currently have"
                  "\ndel = delete a pokemon, will prompt for name \"all\" will delete all")
        else:
            print("Try typing \"help\"")

def setup():
    if not os.path.exists("storage"):
        os.makedirs("storage")

main()
