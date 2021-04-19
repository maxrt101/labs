package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true, includeFieldNames = true)
public class Sneakers extends Shoes {
    private int amortizationIndex;

    public Sneakers(final int size,
                    final String manufacturer,
                    final int amortization) {
        super(ShoeType.SPORT, size, manufacturer);
        this.amortizationIndex = amortization;
    }
}
