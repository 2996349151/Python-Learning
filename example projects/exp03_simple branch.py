score = 66
level = (
    'F' if 0 <= score < 50 else
    'D' if 50 <= score < 60 else
    'C' if 60 <= score < 70 else
    'B' if 70 <= score < 80 else
    'A' if 80 <= score < 90 else
    'S' if 90 <= score <= 100 else
    False)
print(level)
