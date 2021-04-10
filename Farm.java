// Farm.java by maxrt101

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Farm {
  private static int farmsCreated = 0;

  private String location = "-";
  private int animalCount = 0;
  private int ventsPowerWatts = 0;
  
  private int area = 0;
  private int monthlyIncome = 0;
  private int workersAmmount = 0;
  private String ownerName = "-";
  private List<String> animalSpecies;
  
  protected String farmName = "-";
  protected Map<String, Integer> productPrices;


  Farm() {
    farmsCreated += 1;
    this.animalSpecies = new ArrayList<String>();
    this.productPrices = new HashMap<String, Integer>();
  }

  Farm(int area, int monthlyIncome, int workersAmmount, String ownerName) {
    this();
    this.area = area;
    this.monthlyIncome = monthlyIncome;
    this.workersAmmount = workersAmmount;
    this.ownerName = ownerName;
  }

  Farm(String location, int animalCount, int ventsPowerWatts, int area, int monthlyIncome,
       int workersAmmount, String ownerName, List<String> animalSpecies, String farmName,
       Map<String, Integer> productPrices) {
    this(area, monthlyIncome, workersAmmount, ownerName);
    this.location = location;
    this.animalCount = animalCount;
    this.ventsPowerWatts = ventsPowerWatts;
    this.animalSpecies = animalSpecies;
    this.farmName = farmName;
    this.productPrices = productPrices;
  }


  static public int getStaticFarmCount() {
    return farmsCreated;
  }

  static public void printFarmCount() {
    System.out.println(farmsCreated);
  }

  public int getArea() {
    return area;
  }

  public void setArea(int area) {
    this.area = area;
  }

  public int getMonthlyIncome() {
    return this.monthlyIncome;
  }

  public void setMonthlyIncome(int monthlyIncome) {
    this.monthlyIncome = monthlyIncome;
  }

  public int getWorkersAmmount() {
    return this.workersAmmount;
  }

  public void setWorkersAmmount(int workersAmmount) {
    this.workersAmmount = workersAmmount;
  }

  public String getOwnerName() {
    return this.ownerName;
  }

  public void setOwnerName(String ownerName) {
    this.ownerName = ownerName;
  }

  public int getAnimalSpeciesSize() {
    return this.animalSpecies.size();
  }

  public String getAnimalSpecies(int index) {
    return this.animalSpecies.get(index);
  }

  public void addAnimalSpecie(String species) {
    this.animalSpecies.add(species);
  }


  public void resetValues(String location, int animalCount, int ventsPowerWatts, int area, int monthlyIncome,
       int workersAmmount, String ownerName, List<String> animalSpecies, String farmName,
       Map<String, Integer> productPrices) {
    this.area = area;
    this.monthlyIncome = monthlyIncome;
    this.workersAmmount = workersAmmount;
    this.location = location;
    this.animalCount = animalCount;
    this.ventsPowerWatts = ventsPowerWatts;
    this.ownerName = ownerName;
    this.animalSpecies = animalSpecies;
    this.farmName = farmName;
    this.productPrices = productPrices;
  }

  @Override
  public String toString() {
    return String.format("Area: %d\nMonthly Income: %d\nWorkers Ammount: %d\nLocation: %s\nAnimal Count: %d\n" +
            "Vents Power: %d\nOwner Name: %s\nAnimal Species: %s\nFarm Name: %s\nProductPrices: %s\n",
            this.area, this.monthlyIncome, this.workersAmmount, this.location, this.animalCount, this.ventsPowerWatts,
            this.ownerName, this.animalSpecies, this.farmName, this.productPrices);
  }


  public static void main(String[] args) {
    Farm farm1 = new Farm();
    Farm farm2 = new Farm(6400, 150000, 120, "Ivan");
    Farm farm3 = new Farm("Lviv", 150, 2000, 5500, 125000, 80, "Pavlo",
        Arrays.asList("Pigs", "Sheeps", "Cows"), "Vesela Ferma", Map.of("Eggs", 5, "Milk", 30, "Wool", 120));

    System.out.println("Farm #1:\n" + farm1.toString());
    System.out.println("Farm #2:\n" + farm2.toString());
    System.out.println("Farm #3:\n" + farm3.toString());
  
    System.out.print("Farm Count: ");
    Farm.printFarmCount();
    System.out.println();
  }
}

