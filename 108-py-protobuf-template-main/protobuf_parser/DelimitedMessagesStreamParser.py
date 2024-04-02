from helpers import parse_delimited_message
from protobuf_parser.helpers import parseDelimited
from google.protobuf.internal.decoder import _DecodeVarint32


from typing import TypeVar, Type

T = TypeVar('T')

class DelimitedMessagesStreamParser:
    def __init__(self, cls: Type[T]) -> None:
        self.cls = cls

    def parse(self, data: bytes) -> list[Type[T]]:
        messages = []
        pos = 0
        while pos < len(data):
            message, bytes_consumed = parse_delimited_message(data, self.cls, pos)
            messages.append(message)
            pos += bytes_consumed

        return messages
