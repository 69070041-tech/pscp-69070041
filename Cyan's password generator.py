"""password createor"""
def main():
    """start func"""
    name = str(input())
    lastname = str(input())
    age = str(input())

    check_name = len(name)
    check_lastname = len(lastname)
    check_age = len(age)

    name1 = name[0]
    lastname1 = lastname[check_lastname-1]



    if check_name >= 5 and check_lastname >= 5:
        name2 = name[1]

        age1 = age[check_age-1]

        print(name1+name2+lastname1+age1)
    else:
        print(name1+age+lastname1)

main()
