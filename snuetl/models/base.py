from typing import Any, List

class ETLModel:
    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)
    
    @classmethod
    def list_from_dicts(cls, data_list: List[dict[str, Any]]):
        return [cls.from_dict(data) for data in data_list]
    
    def to_dict(self) -> dict[str, Any]:
        return self.__dict__