from typing import TypeVar, Any, Type
from google.protobuf.internal.decoder import _DecodeVarint32

T = TypeVar('T')

def parse_delimited_message(data: bytes, cls: Type[T], start: int = 0) -> tuple[T, int]:
    """
    \brief Расшифровывает сообщение,
    предваренное длиной из массива байтов.
        
    \param data Массив данных.
    \param cls Тип сообщения.

    \return Возвращает кортеж из
    расшифрованного сообщения и количество байт,
    которое потребовалось для расшифровки.
    """
    message_size, pos = _DecodeVarint32(data, start)
    if message_size < 0:
        raise ValueError("Invalid message size")

    end_pos = pos + message_size
    if end_pos > len(data):
        raise ValueError("Incomplete message data")

    message = cls()
    message.ParseFromString(data[pos:end_pos])
    return message, end_pos - start
