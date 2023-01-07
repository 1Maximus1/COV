import logarithm
import factorial
import exp_root
from math import inf


def main():
    def try_input(type, input_text, error_text, overflow_text, fr=-inf, to=inf):
        correct = False
        while not correct:
            i = input(input_text)
            try:
                i = type(i)
                if i >= fr and i <= to:
                    correct = True
                else:
                    print(overflow_text)
                    print('-'*50)
            except:
                print(error_text)
                print('-'*50)
        return i

    description = (
        'All offered functions:\n',
        '1. Factorial;\n',
        '2. Square of a number;\n',
        '3. Сube of a number;\n',
        '4. Square root of a number;\n',
        '5. Cube root of a number;\n',
        '6. log(a,b) (a - the base of the logarithm, b - the argument of the logarithm);\n',
        '7. ln(b);\n',
        '8. log10(b).\n'
    )
    print(*description)
    print('-'*50)
    user_task = try_input(int, "Please, enter the number of task: ",
                          "Error: invalid value", 'Error: have no such a task', 1, 8)
    print('-'*50)
    if user_task == 1:
        user_number = try_input(int, "Please, enter the integer: ",
                                "Error: invalid value", "Error: invalid value", 0)
        print('-'*50)
        result = factorial.factorial.fact(user_number)
        print('Factorial of number:', result)
    elif user_task == 2:
        user_number = try_input(float, "Please, enter the number: ",
                                "Error: invalid value", "Error: invalid value")
        print('-'*50)
        result = exp_root.exponentiation.exp2(user_number)
        print('The square of a number:', result)
    elif user_task == 3:
        user_number = try_input(float, "Please, enter the number: ",
                                "Error: invalid value", "Error: invalid value")
        print('-'*50)
        result = exp_root.exponentiation.exp3(user_number)
        print('The cube of a number:', result)
    elif user_task == 4:
        user_number = try_input(float, "Please, enter the number: ",
                                "Error: invalid value", "Error: invalid value", 0)
        print('-'*50)
        result = exp_root.root.root2(user_number)
        print('The square root of a number:', result)
    elif user_task == 5:
        user_number = try_input(float, "Please, enter the number: ",
                                "Error: invalid value", "Error: invalid value")
        print('-'*50)
        result = exp_root.root.root3(user_number)
        print('The cube root of a number:', result)
    elif user_task == 6:
        correct1 = False
        while not correct1:
            a = try_input(float, "Please, enter the a: ",
                          "Error: invalid value", "Error: invalid value")
            print('-'*50)
            if a > 0 and a != 1:
                b = try_input(float, "Please, enter the b: ",
                              "Error: invalid value", "Error: invalid value")
                print('-'*50)
                correct1 = True
                correct2 = False
                while not correct2:
                    if b > 0:
                        result = logarithm.logarithm.log(a, b)
                        print('log(a,b) =', result)
                        correct2 = True
                    else:
                        print("Error: invalid value")
                        print('-'*50)
                        b = try_input(float, "Please, enter the b: ",
                                      "Error: invalid value", "Error: invalid value")
                        print('-'*50)
            else:
                print("Error: invalid value")
                print('-'*50)
    elif user_task == 7:
        correct = False
        while not correct:
            b = try_input(float, "Please, enter the b: ",
                          "Error: invalid value", "Error: invalid value")
            print('-'*50)
            if b > 0:
                result = logarithm.logarithm.ln(b)
                print('ln(b) =', result)
                correct = True
            else:
                print("Error: invalid value")
                print('-'*50)
    elif user_task == 8:
        correct = False
        while not correct:
            b = try_input(float, "Please, enter the b: ",
                          "Error: invalid value", "Error: invalid value")
            print('-'*50)
            if b > 0:
                result = logarithm.logarithm.lg(b)
                print('lg(b) =', result)
                correct = True
            else:
                print("Error: invalid value")
                print('-'*50)


if __name__ == '__main__':
    main()
