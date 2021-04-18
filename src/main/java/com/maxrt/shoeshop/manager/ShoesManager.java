package com.maxrt.shoeshop.manager;

import java.util.Collections;
import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.List;

import com.maxrt.shoeshop.shoes.ShoeType;
import com.maxrt.shoeshop.shoes.Shoes;

public class ShoesManager {
    private final List<Shoes> shoes = new ArrayList<>();

    public ShoesManager() { }

    public void addShoe(Shoes shoe) {
        shoes.add(shoe);
    }

    public void addShoes(final List<Shoes> shoes) {
        this.shoes.addAll(shoes);
    }

    public List<Shoes> getShoes() {
        return shoes;
    }

    public List<Shoes> sortBySize(final SortOrder order) {
        return sortBySize(order, shoes);
    }

    public List<Shoes> sortBySize(final SortOrder order, final List<Shoes> shoes) {
        List<Shoes> sorted = new ArrayList<>(shoes);
        sorted.sort((s1, s2) -> s1.getSize() - s2.getSize());
        if (order == SortOrder.DESC) {
            Collections.reverse(sorted);
        }
        return sorted;
    }

    public List<Shoes> sortByType(final SortOrder order) {
        return sortByType(order, shoes);
    }

    public List<Shoes> sortByType(final SortOrder order, final List<Shoes> shoes) {
        List<Shoes> sorted = new ArrayList<>(shoes);
        sorted.sort((s1, s2) -> s1.getType().compareTo(s2.getType()));
        if (order == SortOrder.DESC) {
            Collections.reverse(sorted);
        }
        return sorted;
    }

    public List<Shoes> sortByManufacturer(final SortOrder order) {
        return sortByManufacturer(order, shoes);
    }

    public List<Shoes> sortByManufacturer(final SortOrder order, final List<Shoes> shoes) {
        List<Shoes> sorted = new ArrayList<>(shoes);
        sorted.sort((s1, s2) -> s1.getManufacturer().compareTo(s2.getManufacturer()));
        if (order == SortOrder.DESC) {
            Collections.reverse(sorted);
        }
        return sorted;
    }

    public List<Shoes> findByType(final ShoeType type) {
        return findByType(type, shoes);
    }

    public List<Shoes> findByType(final ShoeType type, final List<Shoes> shoes) {
        return shoes.stream()
                .filter(s -> s.getType() == type)
                .collect(Collectors.toList());
    }

    public List<Shoes> findBySize(final int size) {
        return findBySize(size, shoes);
    }

    public List<Shoes> findBySize(final int size, List<Shoes> shoes) {
        return shoes.stream()
                .filter(s -> s.getSize() == size)
                .collect(Collectors.toList());
    }
}
