import my_mod

my_mod.say_hello("ahmed")
my_mod.say_welcome("Ahmed")

from my_mod import say_welcome
say_welcome("Osama")

from my_mod import say_welcome as newWelcome
newWelcome("Khalil")

