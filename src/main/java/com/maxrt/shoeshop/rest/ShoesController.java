package com.maxrt.shoeshop.rest;

import com.maxrt.shoeshop.shoes.Shoes;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
@RequestMapping(path = "/shoes")
public final class ShoesController {
    @Autowired
    private ShoesService shoesService;

    @GetMapping(produces = "application/json")
    public Iterable<Shoes> getShoes() {
        return shoesService.getShoes();
    }

    @GetMapping(path = "/{id}", produces = "application/json")
    public ResponseEntity<Shoes> getShoesById(@PathVariable("id") final int id) {
        return shoesService.getShoesById(id);
    }

    @PostMapping(consumes = "application/json", produces = "application/json")
    public ResponseEntity<Shoes> createShoes(@RequestBody Shoes newShoes) throws IOException {
        return shoesService.createShoes(newShoes);
    }

    @PutMapping(path = "/{id}", consumes = "application/json", produces = "application/json")
    public ResponseEntity<Shoes> updateShoes(
            @PathVariable("id") final int id,
            @RequestBody final Shoes updatedShoes) {
        return shoesService.updateShoes(id, updatedShoes);
    }

    @DeleteMapping(path = "/{id}")
    public ResponseEntity<String> deleteShoes(@PathVariable("id") final int id) {
        return shoesService.deleteShoes(id);
    }
}
