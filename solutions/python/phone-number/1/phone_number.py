import string

class PhoneNumberValidator(object):
    # if a phone number has more than 11 digits.
    @staticmethod
    def not_greater_than_eleven(number):
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")

    # if a phone number has 11 digits, but starts with a number other than 1.
    @staticmethod
    def when_eleven_starts_with_one(number):
        if number[0] != "1" and len(number) == 11:
            raise ValueError("11 digits must start with 1")

    # if a phone number has an exchange code that starts with 0.
    @staticmethod
    def exchange_starts_with_zero(number):
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

    # if a phone number has an exchange code that starts with 1.
    @staticmethod
    def exchange_starts_with_one(number):
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

    # if a phone number has an area code that starts with 0.
    @staticmethod
    def area_code_starts_with_zero(number):
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")

    # if a phone number has an area code that starts with 1.
    @staticmethod
    def area_code_starts_with_one(number):
        if number[0] == "1":
            raise ValueError("area code cannot start with one")

    # if a phone number has punctuation in place of some digits.
    @staticmethod
    def has_punctuation(number):
        for char in string.punctuation:
            if char in number:
                raise ValueError("punctuations not permitted")

    # if a phone number has less than 10 digits.
    @staticmethod
    def has_less_than_ten_digits(number):
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

    # if a phone number has letters in place of some digits.
    @staticmethod
    def has_letters(number):
        for char in string.ascii_letters:
            if char in number:
                raise ValueError("letters not permitted")


class PhoneNumber:
    _validator = PhoneNumberValidator()

    def __init__(self, number):
        self.number = self.parse_number(number)
        self.area_code = self.number[0:3]

    def parse_number(self, number):
        self._validator.has_letters(number)

        for char in [".", "(", ")", "-", "+"]:
            if char in number:
                number = number.replace(char, "")
        self._validator.has_punctuation(number)

        number = number.replace(" ", "")
        self._validator.has_less_than_ten_digits(number)
        self._validator.not_greater_than_eleven(number)
        
        self._validator.when_eleven_starts_with_one(number)
        length = len(number)
        if length == 11:
            number = number[1:]

        self._validator.exchange_starts_with_zero(number)
        self._validator.exchange_starts_with_one(number)
        self._validator.area_code_starts_with_zero(number)
        self._validator.area_code_starts_with_one(number)

        return number

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
        