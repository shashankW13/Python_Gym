import random

from art import logo, vs
from game_data import data

print(logo)

game_continue = True
score = 0
A = {}
B = {}

celeb_data = [celebs for celebs in random.choices(data, k=2)]

def compare_followers(celeb1, celeb2):
      return 'a' if celeb1["follower_count"] > celeb2["follower_count"] else 'b'

while game_continue:
      if not score:
            A = celeb_data[0]
            B = celeb_data[1]
      print(f'Compare A: {A["name"]}, '
            f'a {A["description"]}, '
            f'from {A["country"]}')

      print(vs)

      print(f'Compare B: {B["name"]}, '
            f'a {B["description"]}, '
            f'from {B["country"]}')

      choice = input("Who has more followers? Type 'A' or 'B': ").lower()

      result = compare_followers(celeb1=A, celeb2=B)

      if choice != result:
            game_continue = False
            print(f'That was wrong, Final Score: {score}')
      else:
            score += 1
            print(f'You are right, Score: {score} \n')
            A = B
            repeating_data = True
            while repeating_data:
                  next_data = data[random.randint(0, len(data))]
                  repeating_data = False if next_data != A else True
                  if not repeating_data:
                        B = next_data



