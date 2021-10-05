#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def main():
    # input
    integer1 = input("How many number are you going to add: ")
    answer = 0

    # process & output
    try:
        number_of_numbers = int(integer1)
        for loop_counter in range(number_of_numbers):
            if loop_counter == number_of_numbers:
                continue
            else:
                integer = input("Enter a number to add: ")
                try:
                    number = int(integer)
                    if number < 0:
                        answer = answer
                    else:
                        answer = answer + number
                except Exception:
                    print("This was not a number")
        print("Sum of just the positive number is ={0}".format(answer))

    except Exception:
        print("This was not a number")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
