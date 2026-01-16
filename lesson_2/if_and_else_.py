from colorama import Fore, init


init(autorest=True)
print(f"{Fore.CYAN} Welcome to my first game!")
name = input("What is your name? ").strip().capitalize()
age = int(input(f"Hi {name}! How old are you? "))
if age >= 12:
    print(f"{Fore.GREEN}Great!, you are old enough to play this game.")
else:
    print(f"{Fore.RED}Sorry, but you don`t have the required age to play this game.")
attempts = 3
secret_color = "pink"
print(f"{Fore.CYAN} Guess the color I'm thinking of. You have 3 tries.")
while attempts > 0:
   guess = input("What is your guess? :D ").strip().lower()
   if guess == secret_color:
    print(f"{Fore.GREEN}Correct! {name}, you guessed the color! You win!")
    attempts = 0
    break
   else:
    attempts -= 1
    if attempts > 0:
        print(f"{Fore.RED}Nooo :( That's not the color. Try again :D")   
    else: 
        print(f"{Fore.RED}Sorry, {name} :( You ran out of lives. The color was {secret_color}.")

print(f"{Fore.CYAN}Thank's for playing, {name}!")
