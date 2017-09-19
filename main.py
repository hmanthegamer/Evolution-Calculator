import pack, load, os

def main():
    setup()
    while True:
        x = input("GO: ")
        if x == "add":
            cont = ""
            while cont == "":
                cont = pack.main()
        elif x == "out":
            print(load.main())

def setup():
    if not os.path.exists("storage"):
        os.makedirs("storage")

main()
