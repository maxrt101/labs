package com.maxrt.shoeshop.shoes;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor(access = AccessLevel.PUBLIC)
public class Shoes {
    protected ShoeType type;
    protected int size;
    protected String manufacturer;
}
