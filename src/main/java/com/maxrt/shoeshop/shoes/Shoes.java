package com.maxrt.shoeshop.shoes;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder(toBuilder=true)
public class Shoes {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
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
