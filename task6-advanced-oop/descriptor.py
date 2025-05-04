class PositiveInt:
    
    """Descriptor for positive integers."""

    def __init__(self, name:str):
        self.name = f"__{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer.")
        setattr(instance, self.name, value)
        