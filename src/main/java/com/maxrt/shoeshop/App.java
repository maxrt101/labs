package com.maxrt.shoeshop;

import com.maxrt.shoeshop.manager.ShoesManager;
import com.maxrt.shoeshop.manager.SortOrder;
import com.maxrt.shoeshop.shoes.Shoes;
import com.maxrt.shoeshop.shoes.ShoeType;
import com.maxrt.shoeshop.shoes.Sneakers;
import com.maxrt.shoeshop.shoes.Boots;
import com.maxrt.shoeshop.shoes.FlipFlops;

import java.util.ArrayList;
import java.util.Arrays;

public class App {
    public static void main(final String[] args) {
        ShoesManager manager = new ShoesManager();
        manager.addShoes(Arrays.asList(
            new Sneakers(10, "Adidas"),
            new FlipFlops(20, "Adidas"),
            new Sneakers(20, "Nike"),
            new Boots(10, "Adidas"),
            new Sneakers(30, "Nike"),
            new FlipFlops(17, "Nike"),
            new Boots(14, "Adidas")
        ));

        System.out.print("Unsorted: ");
        manager.getShoes().forEach(s -> System.out.print(" " + s));

        System.out.print("\nSorted by size: ");
        manager.sortBySize(SortOrder.ASC)
                .forEach(s -> System.out.print(" " + s));

        System.out.print("\nSorted by type: ");
        manager.sortByType(SortOrder.ASC)
                .forEach(s -> System.out.print(" " + s));

        System.out.println("\nSorted by manufacturer: ");
        manager.sortByManufacturer(SortOrder.ASC)
                .forEach(s -> System.out.print(" " + s));

        System.out.println("\nAll sportswear by size: ");
        manager.sortBySize(SortOrder.ASC, manager.findByType(ShoeType.SPORT))
                .forEach(s -> System.out.print(" " + s));
    }
}
