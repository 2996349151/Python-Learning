"""Caesar cipher"""

text = input("input text: ")
digit = int(input("input code: ")) % 26
choice = int(input("encryption or decryption (0 or 1): "))

if choice == 0:
    for each in text:
        x = ord(each)
        if 97 <= x <= 122:
            x += digit
            if x > 122:
                x-= 26
        elif 65 <= x <= 90:
            x += digit
            if x > 90:
                x -= 26
        print(chr(x), end="")
elif choice == 1:
    for each in text:
        x = ord(each)
        if 97 <= x <= 122:
            x -= digit
            if x < 97:
                x += 26
        elif 65 <= x <= 90:
            x -= digit
            if x < 65:
                x += 26
        print(chr(x), end="")
