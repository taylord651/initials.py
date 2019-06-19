def get_initials(fullname):
    names_split = fullname.split()
    init = ""
    for name in names_split:
        init = init + name[0]
    return init.upper()

def main():
    fullname = input("What is your full name?")
    print("The initials of " + fullname + " are, " +  get_initials(fullname) + ".")


if __name__ == '__main__':
    main()
