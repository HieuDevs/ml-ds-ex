from Ex1 import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8


def run():
    print("-----Welcome to the AI Menu!-----")
    print("1. Run Exercise 1")
    print("2. Run Exercise 2")
    print("3. Run Exercise 3")
    print("4. Run Exercise 4")
    print("5. Run Exercise 5")
    print("6. Run Exercise 6")
    print("7. Run Exercise 7")
    print("8. Run Exercise 8")
    print("9. Quit")
    print("-----Welcome to the AI Menu!-----")
    while True:
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid choice. Please try again.")
        else:
            match choice:
                case "1":
                    ex1.reslove()
                case "2":
                    ex2.resolve()
                case "3":
                    ex3.resolve()
                case "4":
                    ex4.resolve()
                case "5":
                    ex5.resolve()
                case "6":
                    ex6.resolve()
                case "7":
                    ex7.reslove()
                case "8":
                    ex8.resolve()
                case "9":
                    print("Goodbye!")
                    break
