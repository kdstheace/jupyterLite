import art
from game_data import data
import random

# Function to check whether the answer is correct or wrong
def check_answer(candidate_dict):
    '''Choose the bigger follower count among the given candidate_dict.
    Parameter: candidate_dict
    return: highger candidate'''
    candidate_a = candidate_dict["A"]
    candidate_b = candidate_dict["B"]
    if candidate_a["follower_count"] > candidate_b["follower_count"]:
        return candidate_a
    else:
        return candidate_b


# Function to print questions
def generate_question(data, second_candidate):
    '''The parameters are list of questions dictionary and previous_answer(optional)
  Choose 2 random candidates and remove it from the original data
  Return the dictioinary of candidates {'A': candidate_1, 'B': candidate_2}'''
    if second_candidate is None:
        first_candidate = random.choice(data)
        data.remove(first_candidate)
        second_candidate = random.choice(data)
        data.remove(second_candidate)

    else:
        if len(data) == 0:
            return
        first_candidate = second_candidate
        second_candidate = random.choice(data)
        data.remove(second_candidate)

    candidate_dict = {"A": first_candidate, "B": second_candidate}
    print()
    print("  ************************************  ")
    print(
        f"Compare A: {first_candidate['name']}, a {first_candidate['description']}, from {first_candidate['country']}."
    )
    print(art.vs)
    print()
    print(
        f"Against B: {second_candidate['name']}, a {second_candidate['description']}, from {second_candidate['country']}."
    )
    print("  ************************************  ")
    return candidate_dict


# Function to run game
def game():
    questions_data = data
    point = 0

    print(art.logo)
    candidate_dict = generate_question(questions_data, None)
    # loop until the user is wrong
    # for each loop, generates the questioins and check the answer
    continue_flag = True
    while continue_flag:
        answer = check_answer(candidate_dict)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if candidate_dict[guess] == answer:
            point += 1
            print(f"You're right! Current score: {point}.")
            candidate_dict = generate_question(questions_data, candidate_dict["B"])
            if candidate_dict is None:
                print(">>>>>>>>>>> You've correct every question")
                return
        else:
            continue_flag = False
            print(f"Sorry, that's wrong. Final score: {point}")


# Run game
game()
