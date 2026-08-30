def decode(string):
    if string == "":
        return ""

    decoded = ""
    amount = ""
    for char in string:
        if char.isdigit():
            amount += char
        else:
            decoded += char * int(amount) if amount else char
            amount = ""

    return decoded

def encode(string):
    if string == "":
        return ""

    encoded = ""
    current = string[0]
    amount = 1

    for char in string[1:]:
        if char == current:
            amount += 1
        else:
            encoded += str(amount) + current if amount > 1 else current
            current = char
            amount = 1

    encoded += str(amount) + current if amount > 1 else current
    return encoded