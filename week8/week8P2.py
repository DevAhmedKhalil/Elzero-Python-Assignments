print("تكليفات الدروس من الدرس 060 إلى 064")

print("-----------------------------------")
print("Assignment - (1)")
print("-----------------------------------")


# Ass 1)
def get_score(**score):
    for score_key, score_value in score.items():
        print(f'{score_key} => {score_value}')


# Tests
get_score(Math=90, Science=80, Language=70)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"

print("-----------------------------------")
print("Assignment - (2)")
print("-----------------------------------")


# Ass 2)
def get_people_scores(name=None, **scores):
    if name:
        if scores:
            print(f"Hello {name}, This Is Your Score Table:")
            for score_key, score_value in scores.items():
                print(f"{score_key} => {score_value}")
        else:
            print(f"Hello {name}, You Have No Scores To Show")
    else:
        print("Score Table:")
        for score_key, score_value in scores.items():
            print(f"{score_key} => {score_value}")


# Testing the function
get_people_scores("Osama", Math=90, Science=80, Language=70)
print("#" * 40)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("#" * 40)
get_people_scores(Logic=70, Problems=60)
print("#" * 40)
get_people_scores("Ahmed")  # No scores provided

print("-----------------------------------")
print("Assignment - (3)")
print("-----------------------------------")

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70,
}


def get_the_scores(name=None, **scores):
    if name:
        if scores:
            print(f"Hello {name}, This Is Your Score Table:")
            for score_key, score_value in scores.items():
                print(f"{score_key} => {score_value}")
        else:
            print(f"Hello {name}, You Have No Scores To Show")
    else:
        print("Score Table:")
        for score_key, score_value in scores.items():
            print(f"{score_key} => {score_value}")


get_the_scores("Osama", **scores_list)
print("/" * 40)
get_the_scores("Osama")
print("/" * 40)
get_the_scores(**scores_list)
