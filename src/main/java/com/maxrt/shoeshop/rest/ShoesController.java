package com.maxrt.shoeshop.rest;

import com.maxrt.shoeshop.shoes.Shoes;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.Optional;

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
        Optional<Shoes> shoes = shoesService.getShoesById(id);
        return shoes.map(value -> new ResponseEntity<>(value, HttpStatus.OK))
                 .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @PostMapping(consumes = "application/json", produces = "application/json")
    public ResponseEntity<Shoes> createShoes(@RequestBody Shoes newShoes) throws IOException {
        return new ResponseEntity<>(shoesService.createShoes(newShoes), HttpStatus.OK);
    }

    @PutMapping(path = "/{id}", consumes = "application/json", produces = "application/json")
    public ResponseEntity<Shoes> updateShoes(
            @PathVariable("id") final int id,
            @RequestBody final Shoes updatedShoes) {
        Optional<Shoes> shoes = shoesService.updateShoes(id, updatedShoes);
        return shoes.map(value -> new ResponseEntity<>(value, HttpStatus.OK))
                 .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }

    @DeleteMapping(path = "/{id}")
    public ResponseEntity<?> deleteShoes(@PathVariable("id") final int id) {
        boolean isDeleted = shoesService.deleteShoes(id);
        if (isDeleted) {
            return new ResponseEntity<>(HttpStatus.OK);
        }
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
