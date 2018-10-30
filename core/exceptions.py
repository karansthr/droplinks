class InvalidInputsError(Exception):

    def __init__(self, errors, non_field_errors):
        self.errors = errors
        self.non_field_errors = non_field_errors

    def __str__(self):
        return (
            f'{repr(self.errors)} '
            f'{repr(self.non_field_errors)}')