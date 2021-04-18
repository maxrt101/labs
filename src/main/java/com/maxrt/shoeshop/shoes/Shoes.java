package com.maxrt.shoeshop.shoes;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor(access = AccessLevel.PUBLIC)
public class Shoes {
    protected ShoeType type;
    protected int size;
    protected String manufacturer;
}
