import unittest

from .. import ShoesManager, Shoes, Sneakers, Boots, FlipFlops

shoes = [
  Sneakers(10, 'Adidas'),
  FlipFlops(20, 'Adidas'),
  Sneakers(20, 'Nike'),
  Boots(10, 'Adidas'),
  Sneakers(30, 'Nike'),
  FlipFlops(17, 'Nike'),
  Boots(14, 'Adidas')
]

class SortTest(unittest.TestCase):
  def test_sort_by_size(self):
    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    self.assertListEqual(mngr.sort_by_size(), sorted(shoes, key=lambda s: s.size))
    self.assertListEqual(mngr.sort_by_size(True), sorted(shoes, key=lambda s: s.size, reverse=True))

  def test_sort_by_type(self):
    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    self.assertListEqual(mngr.sort_by_type(), sorted(shoes, key=lambda s: s.type.name.lower()))
    self.assertListEqual(mngr.sort_by_type(True), sorted(shoes, key=lambda s: s.type.name.lower(), reverse=True))


  def test_sort_by_manufacturer(self):
    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    self.assertListEqual(mngr.sort_by_manufacturer(), sorted(shoes, key=lambda s: s.manufacturer.lower()))
    self.assertListEqual(mngr.sort_by_manufacturer(True), sorted(shoes, key=lambda s: s.manufacturer.lower(), reverse=True))


