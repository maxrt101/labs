package com.maxrt.shoeshop.shoes;

import lombok.Data;
import lombok.ToString;

@Data
@ToString(callSuper = true, includeFieldNames = true)
public class Sneakers extends Shoes {
    private int amortizationIndex;

    public Sneakers(final int size, final String manufacturer, int amortizationIndex) {
        super(ShoeType.SPORT, size, manufacturer);
        this.amortizationIndex = amortizationIndex;
    }
}
