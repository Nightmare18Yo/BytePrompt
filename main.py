while True:
    code = input("Code: ")

    if code == 'print':
        string = input("Enter String: ")
        print(string)
    elif code == 'varint':
        try:
            var_name = input('Enter Variable Name: ')
            if var_name.isidentifier():
                variable = int(input('Enter Integer Value: '))
                globals()[var_name] = variable
            else:
                print("Invalid variable name. Please enter a valid identifier.")
        except ValueError:
            print("Invalid input for integer variable. Please enter an integer.")
    elif code == 'varfloat':
        try:
            var_name = input('Enter Variable Name: ')
            if var_name.isidentifier():
             variable = float(input('Enter Float Value: '))
             globals()[var_name] = variable
            else:
                print("Invalid variable name. Please enter a valid identifier.")
        except ValueError:
            print("Invalid input for float variable. Please enter a float.")
    elif code == 'varstr':
        var_name = input('Enter Variable Name: ')
        variable = input('Enter String Value: ')
        globals()[var_name] = variable
    elif code == 'printvar':
        var_name = input('Enter Variable Name: ')
        if var_name in globals():
            print(globals()[var_name])
        else:
            print(f"Variable {var_name} not found.")
    elif code == 'finloop':
        try:
            lopcom = input("Enter Command to be repeated: ")
            lop = int(input('Enter Number of Repeations: '))

            for _ in range(lop):
                if lopcom == "print":
                    string = input('Enter String: ')
                    print(string)
                elif lopcom == 'printvar':
                    var_name = input('Enter Variable Name: ')
                    if var_name in globals():
                        print(globals()[var_name])
                    else:
                        print(f"Variable {var_name} not found.")
                else:
                    print("Invalid loop command.")
        except ValueError:
            print("Invalid input for loop repeats. Please enter an integer.")
    elif code == 'infinloop':
        lopcom = input("Enter Command to be repeated: ")

        if lopcom == "print":
            string = input('Enter String: ')
            while True:
                print(string)
        elif lopcom == 'printvar':
            var_name = input('Enter Variable Name: ')
            if var_name in globals():
                while True:
                    print(globals()[var_name])
            else:
                print(f"Variable {var_name} not found.")
        else:
            print("Invalid loop command.")
    elif code == 'exit':
        break
    else:
        print("Invalid command.")


    