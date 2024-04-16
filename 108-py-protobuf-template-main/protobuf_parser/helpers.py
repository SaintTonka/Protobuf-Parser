from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.message import DecodeError
from typing import TypeVar, Any, Type

T = TypeVar('T')

def parseDelimited(data: Any, cls: Type[T]) -> tuple[Type[T], int]:
    if data:
        try:
            size, ind = _DecodeVarint32(data, 0)
        except:
            raise IndexError
        if size + ind <= len(data): 
            message = cls()
            try:
                message.ParseFromString(data[ind:ind+size])
            except DecodeError as e:
                raise ValueError(str(e))
            return message, size + ind
    return None, 0