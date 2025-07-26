from colorama import Fore, Style

total = 0
for i in range(1, 51):
    total += i
print(f"The {Fore.YELLOW}sum{Style.RESET_ALL} of numbers {Fore.CYAN}from {Fore.RED}1{Fore.CYAN} to {Fore.RED}50 {Fore.CYAN}is{Style.RESET_ALL}: {Fore.MAGENTA}{total}")


# output
# The sum of numbers from 1 to 50 is: 1275
