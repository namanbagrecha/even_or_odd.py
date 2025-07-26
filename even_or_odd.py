from colorama import Fore, Style

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{Fore.RED}{number} {Fore.CYAN}is {Style.RESET_ALL}an even number.")
else:
    print(f"{Fore.RED}{number} {Fore.CYAN}is {Style.RESET_ALL}an odd number.")


# output

# Enter a number: 9
# 9 is an odd number.
