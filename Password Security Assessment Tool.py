import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = "(),+-*."
forbidden_characters = {'!', '#', '$', '%', '&', "'", '\\', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'Ğ', 'ğ', 'Ü', 'ü', 'Ş', 'ş', 'Ö', 'ö', 'Ç', 'ç', 'ı', 'İ'}

password = input("Enter your password:")

if len(password) < 4 or len(password) > 8:
    print("Invalid Password \nPassword must be at least 4, at most 8 characters long")
elif not any(c in lowercase_letters for c in password):
    print("Invalid Password \nPassword must contain at least one lowercase letter")
elif not any(c in uppercase_letters for c in password):
    print("Invalid Password \nPassword must contain at least one uppercase letter")
elif not any(c in digits for c in password):
    print("Invalid Password \nPassword must contain at least one digit")
elif not any(c in special_characters for c in password):
    print("Invalid Password \nPassword must contain at least one of the allowed special characters")
elif any(c in forbidden_characters for c in password):
    print("Invalid Password \nPassword cannot contain forbidden characters or Turkish characters")
else:
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_character_count = 0

    for char in password:
        if char in lowercase_letters:
            lowercase_count += 1
        elif char in uppercase_letters:
            uppercase_count += 1
        elif char in digits:
            digit_count += 1
        elif char in special_characters:
            special_character_count += 1

    G = 3 * (lowercase_count + 1) * 5 * (uppercase_count + 1) * 2 * (digit_count + 1) * 4 * (special_character_count + 1) - 120

    if G < 2000:
        print("Valid Password \nVery Weak Password")
    elif 2000 <= G < 4000:
        print("Valid Password \nWeak Password")
    elif 4000 <= G < 6000:
        print("Valid Password \nModerate Password")
    elif 6000 <= G < 9000:
        print("Valid Password \nStrong Password")
    else:
        print("Valid Password \nVery Strong Password")
