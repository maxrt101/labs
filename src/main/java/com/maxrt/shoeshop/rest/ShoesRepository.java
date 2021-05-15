package com.maxrt.shoeshop.rest;

import com.maxrt.shoeshop.shoes.Shoes;
import org.springframework.data.repository.CrudRepository;

public interface ShoesRepository extends CrudRepository<Shoes, Integer> { }
