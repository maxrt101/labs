# lab1.py/20 by maxrt101

class Farm:
  farm_count: int = 0

  def __init__(self, location: str = "", animal_count: int = 0, vents_power: int = 0) -> None:
    self.location = location
    self.animal_count = animal_count
    self.vents_power = vents_power
    Farm.farm_count += 1

  def __del__(self):
    Farm.farm_count -= 1

  def __str__(self) -> str:
    return f"Farm({self.location}, {self.animal_count}, {self.vents_power})"

  @classmethod
  def get_count(cls) -> int:
    return cls.farm_count


def main():
  farms: list[Farm] = [Farm("Lviv", 150, 400), Farm("Kyiv", 250, 700), Farm("Ternopil", 100, 300)]
  for farm in farms:
    print(farm)


if __name__ == "__main__":
  main()

