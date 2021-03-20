# boots.py by maxrt101

from shoes import Shoes, ShoeType


class Boots(Shoes):
    def __init__(self, size: int = 0, manufacturer: str = '') -> None:
        super().__init__(ShoeType.WINTER, size, manufacturer)
