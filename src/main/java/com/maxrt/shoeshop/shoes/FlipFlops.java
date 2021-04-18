package com.maxrt.shoeshop.shoes;

import lombok.ToString;

@ToString(callSuper = true, includeFieldNames = true)
public class FlipFlops extends Shoes {
    public FlipFlops(final int size, final String manufacturer) {
        super(ShoeType.SUMMER, size, manufacturer);
    }
}