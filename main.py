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
            print(load.main())
        #elif x == "list":
        #    print(load.list_poke)
        elif x == "help":
            print("Commands:"
                  "\nadd = regester a new pokemon"
                  "\nout = output how many pokemon you can evolve")
        else:
            print("Try typing \"help\"")

def setup():
    if not os.path.exists("storage"):
        os.makedirs("storage")

main()
