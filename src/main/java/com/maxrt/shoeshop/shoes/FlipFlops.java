package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true, includeFieldNames = true)
public class FlipFlops extends Shoes {
    private boolean hasMembrane;

    public FlipFlops(final int size,
                     final String manufacturer,
                     final boolean membrane) {
        super(ShoeType.SUMMER, size, manufacturer);
        this.hasMembrane = membrane;
    }
}
