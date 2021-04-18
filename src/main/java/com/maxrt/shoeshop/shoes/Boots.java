package com.maxrt.shoeshop.shoes;

import lombok.ToString;

@ToString(callSuper = true, includeFieldNames = true)
public class Boots extends Shoes {
    public Boots(final int size, final String manufacturer) {
        super(ShoeType.WINTER, size, manufacturer);
    }
}
