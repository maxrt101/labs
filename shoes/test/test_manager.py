import unittest

from .. import ShoesManager, Shoes, Sneakers, Boots, FlipFlops


class ManagerTest(unittest.TestCase):
  def test_add_shoe(self):
    shoes = [
      Sneakers(10, 'Adidas'),
      FlipFlops(20, 'Adidas')
    ]
    
    mngr = ShoesManager()
    
    mngr.add_shoe(shoes[0])
    self.assertListEqual(mngr.shoes, [shoes[0]])
    
    mngr.add_shoe(shoes[1])
    self.assertListEqual(mngr.shoes, shoes)


  def test_add_shoes(self):
    shoes = [
      Sneakers(10, 'Adidas'),
      FlipFlops(20, 'Adidas'),
      Sneakers(20, 'Nike'),
      Boots(10, 'Adidas'),
      Sneakers(30, 'Nike'),
      FlipFlops(17, 'Nike'),
      Boots(14, 'Adidas')
    ]

    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    self.assertListEqual(mngr.shoes, shoes)

