import json
from typing import Any


class AttributeDict:
    def __init__(self, value={}, **kwargs):
        if isinstance(value, list):
            self.value = [
                self.__make(Item) if isinstance(Item, dict) else Item for Item in value
            ]
        else:
            self.value = dict(value, **kwargs)

    def __len__(self) -> int:
        return len(self.value)

    def __str__(self) -> str:
        return json.dumps(self.value, default=lambda x: x.__dict__())

    def __repr__(self) -> str:
        return self.value.__repr__()

    def __dict__(self) -> dict:
        return self.value

    def __bool__(self) -> bool:
        return bool(self.value)

    def __getattr__(self, name: str) -> Any:
        if isinstance(self.value, list):
            return self.value[name]

        return self.__get(name)

    def __getitem__(self, key: str) -> Any:
        return self.__getattr__(key)

    def __contains__(self, element: Any) -> bool:
        return element in self.value

    def __get(self, name: str) -> Any:
        Value = self.value.get(name)

        if name in self.value:
            if isinstance(Value, dict):
                Value = self.__make(Value)
            elif isinstance(Value, list):
                Value = [
                    Item if not isinstance(Item, dict) else self.__make(Item)
                    for Item in Value
                ]
            elif isinstance(Value, tuple):
                Value = (
                    Item if not isinstance(Item, dict) else self.__make(Item)
                    for Item in Value
                )
            elif isinstance(Value, set):
                Value = {
                    Item if not isinstance(Item, dict) else self.__make(Item)
                    for Item in Value
                }
        else:
            if hasattr(name, self.value):
                Value = getattr(name, self.value)

        return Value

    @classmethod
    def __make(cls, *args, **kwargs):
        return cls(*args, **kwargs)


class HeliotropeResponse(AttributeDict):
    def __init__(self, response: dict):
        super().__init__(response)


class GalleryInfo(HeliotropeResponse):
    pass


class Info(HeliotropeResponse):
    pass


class Integrated(HeliotropeResponse):
    pass


class List_(HeliotropeResponse):
    pass


class Index(HeliotropeResponse):
    pass

class Images(HeliotropeResponse):
    pass