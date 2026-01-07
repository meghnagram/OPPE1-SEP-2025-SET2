


points = list(map(float, input().split()))

# Number line marker
LINE = list(('-'*9).join('|'*6))

line = LINE.copy()
for point in points:
    line[round(point*10)] = 'X'
print(''.join(line))
print((' '*9).join(map(str,range(0,6))))


# Number Line Marker
# Given n numbers between 0 to 5 with precision of 1 decimal digit, print a formatted number-line marking the values given with 'X' (uppercase) in the corresponding position.

# NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

# Number line formatting:

# Range is from 0 to 5.
# "|" character marks the interger points.
# "-" marks the 9 decimal places between two integers corresponding to 'n.1,n.2,...,n.9'.
# The corresponding integer number is printed below the "|" character.
# "X" should be present in the marked positions instead of "|" or "-".
# Input Format

# Input will contain single line with the points to mark(separated by whitespace).

# Output Format

# The corresponding number line with the given points marked. There should be no blank spaces at the end of each line.

# Example

# Input

# 0 3.1 5 1.8  4.5 1
# Output

# X---------X-------X-|---------|-X-------|----X---X|
# 0         1         2         3         4         5
