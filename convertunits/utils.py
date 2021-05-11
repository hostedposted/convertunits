from typing import Any

NoneType = type(None)

def is_none(item: Any) -> bool:
    return isinstance(item, NoneType)

class Base:
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{key} = {val!r}' for key, val in self.__dict__.items())})"