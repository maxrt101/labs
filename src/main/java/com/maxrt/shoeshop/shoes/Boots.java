package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.ToString;

@Data
@ToString(callSuper = true, includeFieldNames = true)
public class Boots extends Shoes {
    private boolean hasShoelaces;

    public Boots(final int size, final String manufacturer, final boolean hasShoelaces) {
        super(ShoeType.WINTER, size, manufacturer);
        this.hasShoelaces = hasShoelaces;
    }
}
