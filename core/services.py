from .exceptions import InvalidInputsError

class Service:

    def __init__(self, data, strict=True):
        self.fields = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        self.data = data
        self.errors = {}
        self.non_field_errors = {}
        self.strict = strict

        for key, value in data.items():
            try:
                getattr(self, key).value = value
            except:
                self.non_field_errors[key] = f"'{key}' is not a valid field"
            
    def is_valid(self):
        valid = True
        for field in self.data:
            attr = getattr(self, field)
            if not (self.strict or attr.value):
                continue
            if not attr.is_valid():
                self.errors[attr] = attr.errors
                valid = False
        return valid
    
    def service_clean(self):
        if not self.is_valid():
            raise InvalidInputsError(
                self.errors, self.non_field_errors
            )

    def process(self):
        raise NotImplementedError()
    
    @classmethod
    async def execute(cls, data, static=True):
        instance = cls(data, static)
        instance.service_clean()
        assert hasattr(instance, 'process'), "'Process' method undefined"
        return await instance.process()
