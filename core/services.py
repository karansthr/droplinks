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
                self.errors[field] = attr.errors
                valid = False
        return valid

    def process(self):
        raise NotImplementedError()
    
    @classmethod
    async def execute(cls, data, static=True):
        instance = cls(data, static)
        if instance.is_valid():
            return await instance.process()
        # log instance.non_field_errors
        return instance.errors, 400
