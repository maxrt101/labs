package com.maxrt.shoeshop.shoes;

import lombok.ToString;

@ToString(callSuper = true, includeFieldNames = true)
public class Sneakers extends Shoes {
    public Sneakers(final int size, final String manufacturer) {
        super(ShoeType.SPORT, size, manufacturer);
    }
}