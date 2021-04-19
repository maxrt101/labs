package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true, includeFieldNames = true)
public class Boots extends Shoes {
    private boolean hasShoelaces;

    public Boots(final int size,
                 final String manufacturer,
                 final boolean shoelaces) {
        super(ShoeType.WINTER, size, manufacturer);
        this.hasShoelaces = shoelaces;
    }
}
