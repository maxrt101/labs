# sneakers.py by maxrt101

from shoes import Shoes, ShoeType

class Sneakers(Shoes):
  def __init__(self, size: int = 0, manufacturer: str = '') -> None:
    super().__init__(ShoeType.SPORT, size, manufacturer)


