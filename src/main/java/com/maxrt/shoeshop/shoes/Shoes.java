package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class Shoes {
    private static int nextId;

    private int id;
    private ShoeType type;
    private int size;
    private String manufacturer;

    Shoes(final ShoeType shoeType,
          final int shoeSize,
          final String shoeManufacturer) {
        type = shoeType;
        size = shoeSize;
        manufacturer = shoeManufacturer;
    }
}
