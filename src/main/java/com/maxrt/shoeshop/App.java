package com.maxrt.shoeshop;

import com.maxrt.shoeshop.manager.ShoesManager;
import com.maxrt.shoeshop.manager.SortOrder;
import com.maxrt.shoeshop.shoes.ShoeType;
import com.maxrt.shoeshop.shoes.Sneakers;
import com.maxrt.shoeshop.shoes.Boots;
import com.maxrt.shoeshop.shoes.FlipFlops;

import java.util.Arrays;

public class App {
    public static void main(final String[] args) {
        ShoesManager manager = new ShoesManager();
        manager.addShoes(Arrays.asList(
            new Sneakers(10, "Adidas", 12),
            new FlipFlops(20, "Adidas", true),
            new Sneakers(20, "Nike", 14),
            new Boots(10, "Adidas", true),
            new Sneakers(30, "Nike", 17),
            new FlipFlops(17, "Nike", false),
            new Boots(14, "Adidas", false)
        ));

        System.out.print("Unsorted: ");
        manager.getShoes().forEach(shoe -> System.out.print(" " + shoe));

        System.out.print("\nSorted by size: ");
        manager.sortBySize(SortOrder.ASC)
                .forEach(shoe -> System.out.print(" " + shoe));

        System.out.print("\nSorted by type: ");
        manager.sortByType(SortOrder.ASC)
                .forEach(shoe -> System.out.print(" " + shoe));

        System.out.println("\nSorted by manufacturer: ");
        manager.sortByManufacturer(SortOrder.ASC)
                .forEach(shoe -> System.out.print(" " + shoe));

        System.out.println("\nAll sportswear by size: ");
        manager.sortBySize(SortOrder.ASC, manager.findByType(ShoeType.SPORT))
                .forEach(shoe -> System.out.print(" " + shoe));
    }
}
