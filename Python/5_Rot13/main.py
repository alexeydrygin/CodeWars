# 5 Kyu - Rot13
def rot13(message):
    # Create empty result string
    result = ""
    # Iterate over each character in the message string
    for char in message:
        # If the character is a letter, apply the ROT13 cipher
        if char.isalpha():
            # Determine the new position of the letter in the alphabet
            new_pos = ord(char) + 13
            if char.islower():
                # Wrap around to 'a' if the new position goes beyond 'z'
                new_pos = (new_pos - ord('a')) % 26 + ord('a')
            else:
                # Wrap around to 'A' if the new position goes beyond 'Z'
                new_pos = (new_pos - ord('A')) % 26 + ord('A')
            # Convert the new position back to a letter and append it to the result string
            result += chr(new_pos)
        else:
            # Append non-letter characters to the result string unchanged
            result += char
    return result

print(rot13("Test text"))