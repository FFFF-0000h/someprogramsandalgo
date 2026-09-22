"""
A simple calculator program.

Author: Itunuayo Adebiyi
"""
import sys

firstnum = float(input("Enter first number: "))
secondnum = float(input("Enter second number: "))

while True:
    try:
        while True:
            operatorr = input("Enter an operator: ")
            if operatorr != "+" and operatorr != "-" and operatorr != "/" and operatorr != "*":
                print("Invalid operator\nEnter a valid operator (+,-,/,*): ")

            if operatorr == "+":
                result = firstnum + secondnum
                print(result)
                break
            elif operatorr == "-":
                result = firstnum - secondnum
                print(result)
                break
            elif operatorr == "*":
                result = firstnum * secondnum
                print(result)
                break
            elif operatorr == "/":
                if secondnum == 0:
                    print("Cannot divide by zero!")
                    break
                else:
                    result = firstnum / secondnum
                    print(result)
                    break
    except KeyboardInterrupt:
        print("\n[!] Program interrupted by user (Ctrl+C). Exiting gracefully")
        sys.exit(0)
    except EOFError:
        print("\n[!] End of file reached (Ctrl+D). Exiting gracefully...")
        sys.exit(0)