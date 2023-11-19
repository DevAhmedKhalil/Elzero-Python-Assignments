print("#" * 40)
print("تكليفات الدروس من الدرس 103 إلى 116")
print("#" * 40)

print("Assignment 01")
print("-" * 20)


class Game:
    # Write Class Content
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return f"{self.price}"


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

print("\n")
print("-" * 20)
print("Assignment 02")
print("-" * 20)


class User:
    # Write Class Content
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname} {self.lname[0]}. [{40 - self.age}] Years To Reach 40"
        elif self.gender == "Female":
            return f"Hello Mr {self.fname} {self.lname[0]}. [{40 - self.age}] Years To Reach 40"
        else:
            return f"Hello {self.fname} {self.lname[0]}. [{40 - self.age}] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

print("-" * 20)
print("Assignment 03")
print("-" * 20)


class Message:
    def __init__(self):
        pass

    def print_message(self):
        return f"Hello From Class {self.__class__.__name__}"


Message = Message()

print(Message.print_message())

# Output
# Hello From Class Message

print("-" * 20)
print("Assignment 04")
print("-" * 20)


class Games:
    def __init__(self, oneGame=None, listGames=None, numOfGames=None):
        self.oneGame = oneGame
        self.listGames = listGames
        self.numOfGames = numOfGames

    def show_games(self):
        if isinstance(self.oneGame, str):
            print(f'I Have One Game Called "{self.oneGame}"')
        elif isinstance(self.listGames, list):
            print('I Have Many Games:')
            for game in self.listGames:
                print(f'-- {game}')
        elif isinstance(self.numOfGames, int):
            print(f'I Have {self.numOfGames} Game.')


my_game = Games("Shadow Of Mordor")
my_games_names = Games(listGames=["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(numOfGames=80)

my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()

print("-" * 20)
print("Assignment 05")
print("-" * 20)


# Main Class
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

    def show_info(self):
        return super().show_info()


class Moderators(Members):
    def __init__(self, n, p):
        Members.__init__(self, n, p)

    def show_info(self):
        return Members.show_info(self)


# Example usage
member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

print("-" * 20)
print("Assignment 06")
print("-" * 20)


class A:
    def __init__(self, one):
        self.one = one


class B:
    def __init__(self, two):
        self.two = two


class C:
    def __init__(self, three):
        self.three = three


class Name(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"


# Example usage
the_name = Name("El", "ze", "ro")
print(the_name.show_name())
