import pack, load

def main():
    while True:
        x = input("GO: ")
        if x == "add":
            cont = ""
            while cont == "":
                cont = pack.main()
        elif x == "out":
            print(load.main())

main()
