package com.maxrt.shoeshop.manager;

import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.List;

import com.maxrt.shoeshop.shoes.ShoeType;
import com.maxrt.shoeshop.shoes.Shoes;
import lombok.Getter;

public class ShoesManager {
    @Getter
    private final List<Shoes> shoes = new ArrayList<>();


    public void addShoe(final Shoes shoe) {
        shoes.add(shoe);
    }

    public void addShoes(final List<Shoes> shoesList) {
        this.shoes.addAll(shoesList);
    }

    public List<Shoes> sortBySize(final SortOrder order) {
        return sortBySize(order, shoes);
    }

    public List<Shoes> sortBySize(final SortOrder order,
                                  final List<Shoes> shoesList) {
        List<Shoes> sorted = new ArrayList<>(shoesList);
        if (order == SortOrder.ASC) {
            sorted.sort((shoe1, shoe2) -> shoe1.getSize() - shoe2.getSize());
        } else {
            sorted.sort((shoe1, shoe2) -> shoe2.getSize() - shoe1.getSize());
        }
        return sorted;
    }

    public List<Shoes> sortByType(final SortOrder order) {
        return sortByType(order, shoes);
    }

    public List<Shoes> sortByType(final SortOrder order,
                                  final List<Shoes> shoesList) {
        List<Shoes> sorted = new ArrayList<>(shoesList);
        if (order == SortOrder.ASC) {
            sorted.sort((shoe1, shoe2) ->
                    shoe1.getType().compareTo(shoe2.getType()));
        } else {
            sorted.sort((shoe1, shoe2) ->
                    shoe2.getType().compareTo(shoe1.getType()));
        }
        return sorted;
    }

    public List<Shoes> sortByManufacturer(final SortOrder order) {
        return sortByManufacturer(order, shoes);
    }

    public List<Shoes> sortByManufacturer(final SortOrder order,
                                          final List<Shoes> shoesList) {
        List<Shoes> sorted = new ArrayList<>(shoesList);
        if (order == SortOrder.ASC) {
            sorted.sort((shoe1, shoe2) ->
                    shoe1.getManufacturer().compareTo(shoe2.getManufacturer()));
        } else {
            sorted.sort((shoe1, shoe2) ->
                    shoe2.getManufacturer().compareTo(shoe1.getManufacturer()));
        }
        return sorted;
    }

    public List<Shoes> findByType(final ShoeType type) {
        return findByType(type, shoes);
    }

    public List<Shoes> findByType(final ShoeType type,
                                  final List<Shoes> shoesList) {
        return shoesList.stream()
                .filter(shoe -> shoe.getType() == type)
                .collect(Collectors.toList());
    }

    public List<Shoes> findBySize(final int size) {
        return findBySize(size, shoes);
    }

    public List<Shoes> findBySize(final int size, final List<Shoes> shoesList) {
        return shoesList.stream()
                .filter(shoe -> shoe.getSize() == size)
                .collect(Collectors.toList());
    }
}
