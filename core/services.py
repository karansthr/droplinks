from . import validators
from utils import status_codes


class Service:
    def __init__(self, data, _strict=True):
        self.fields = [
            attr for attr in dir(self) if isinstance(getattr(self, attr), validators.Validator)
        ]
        self.data = data
        self.errors = {}
        self.non_field_errors = {}

    def is_valid(self):
        valid = True
        for field in self.fields:
            attr = getattr(self, field)
            attr.value = self.data.get(field) or None
            attr.errors = []
            if not attr.is_valid():
                self.errors[field] = attr.errors
                valid = False
        return valid

    def process(self):
        raise NotImplementedError()

    @classmethod
    async def execute(cls, data):
        instance = cls(data)
        if instance.is_valid():
            return await instance.process()
        # log instance.non_field_errors
        return instance.errors, status_codes.UNPROCESSABLE_ENTITY
