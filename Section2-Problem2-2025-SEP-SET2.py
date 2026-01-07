

n = int(input())
score_groups = {}
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score not in score_groups:
        score_groups[score] = []
    score_groups[score].append(name)

for i, score in enumerate(sorted(score_groups, reverse=True),1):
    names = ', '.join(sorted(score_groups[score]))
    print(f'{i}. {names}')


# Leaderboard List by Scores
# Write a program to create a leaderboard list from player names and scores.
# Players are ranked based on their scores in descending order.
# If multiple players have the same score, they share the same rank (alphabetically sorted).
# The output should be a numbered list containing leaderboard entries in the format shown below.

# NOTE:
# This is an I/O type question -- you must write the complete code to read input and print the output.

# Input Format
# The first line contains an integer n, the number of players.
# The next n lines each contain a player's name and score separated by a space.
# Output Format
# A numbered list, where each line has the rank and the comma separated list of names in that rank.
# There is a single space after the point after the rank and a space after every comma.
# Example

# Input

# 5
# Alice 50
# Bob 70
# Charlie 70
# David 60
# Eve 50
# Output

# 1. Bob, Charlie
# 2. David
# 3. Alice, Eve
# Explanation

# Bob and Charlie share the highest score (70), so they get rank 1.
# David (60) comes next with rank 2.
Alice and Eve share the lowest score (50), so they get rank 3.\
