# shoes.py by maxrt101

from enum import Enum


class ShoeType(Enum):
  SPORT = 0
  SUMMER = 1
  WINTER = 2


class Shoes:
  def __init__(self, shoes_type: ShoeType, size: int = 0, manufacturer: str = '') -> None:
    self._size = size
    self._shoes_type = ShoeType(shoes_type)
    self._manufacturer = manufacturer

  def get_size(self) -> int:
    return self._size

  def get_type(self) -> ShoeType:
    return self._shoes_type

  def get_manufacturer(self) -> str:
    return self._manufacturer

  def __str__(self) -> str:
    return f'{self._manufacturer} {self.__class__.__name__} size: {self._size} type: {self._shoes_type.name}'

