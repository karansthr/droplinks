import re


class Validator:
    def __init__(self):
        self.value = None
        self.errors = []

    def is_valid(self):
        raise NotImplementedError()


class String(Validator):
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__()

    def is_valid(self):
        if not isinstance(self.value, str):
            self.errors.append("It must be a string")
            return False
        if self.min_length and len(self.value) < self.min_length:
            self.errors.append(f"It must be atleast {self.min_length} character long")
            return False
        if self.max_length and len(self.value) > self.max_length:
            self.errors.append(f"Maximum allowed length is {self.max_length}")
            return False
        return True


class Boolean(Validator):
    def is_valid(self):
        if not isinstance(self.value, bool):
            self.errors.append("It must be a boolean")
            return False
        return True


class Decimal(Validator):
    def is_valid(self):
        if not isinstance(self.value, (int, float)):
            self.errors.append("It must be a string")
            return False
        return True


class Email(String):
    def is_valid(self):
        regex = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
        if not bool(re.search(regex, self.value)):
            self.errors.append("Invalid email")
            return False
        return True
