import pack

def main():
    while True:
        x = input("GO: ")
        if x == "add":
            cont = ""
            while cont == "":
                cont = pack.main()

main()
