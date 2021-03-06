# shoes_manager.py by maxrt101

from typing import List
from shoes import Shoes, ShoeType


class ShoesManager:
  def __init__(self) -> None:
    self.shoes = []


  def add_shoe(self, shoe: Shoes) -> None:
    self.shoes.append(shoe)


  def add_shoes(self, shoes: List[Shoes]) -> None:
    self.shoes += shoes


  def sort_by_size(self, reverse: bool = False, shoes: List[Shoes] = None) -> List[Shoes]:
    return sorted(shoes if shoes else self.shoes, key=lambda s: s.get_size(), reverse=reverse)


  def sort_by_type(self, reverse: bool = False, shoes: List[Shoes] = None) -> None:
    return sorted(shoes if shoes else self.shoes, key=lambda s: s.get_type().name.lower(), reverse=reverse)


  def sort_by_manufacturer(self, reverse: bool = False, shoes: List[Shoes] = None) -> None:
    return sorted(shoes if shoes else self.shoes, key=lambda s: s.get_manufacturer().lower(), reverse=reverse)


  def find_by_type(self, shoes_type: ShoeType) -> List[Shoes]:
    return [shoe for shoe in self.shoes if shoe.get_type() == shoes_type]


  def find_by_size(self, size: int) -> List[Shoes]:
    return [shoe for shoe in self.shoes if shoe.get_size() == size]


