package com.maxrt.shoeshop.rest;

import com.maxrt.shoeshop.shoes.Shoes;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.context.annotation.ApplicationScope;

import java.io.IOException;
import java.util.Optional;

@Service
@ApplicationScope
public class ShoesService {
    @Autowired
    private ShoesRepository shoesRepository;

    public Iterable<Shoes> getShoes() {
        return shoesRepository.findAll();
    }

    public ResponseEntity<Shoes> createShoes(final Shoes newShoes) throws IOException {
        shoesRepository.save(newShoes);
        return new ResponseEntity<>(newShoes, HttpStatus.OK);
    }

    public ResponseEntity<Shoes> getShoesById(final int id) {
        Optional<Shoes> searchedShoes = shoesRepository.findById(id);
        if (searchedShoes.isPresent()) {
            return new ResponseEntity<>(searchedShoes.get(), HttpStatus.OK);
        }
        return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
    }

    public ResponseEntity<Shoes> updateShoes(
            final int id,
            final Shoes updatedShoes) {
        Optional<Shoes> shoesOptional = shoesRepository.findById(id);

        if (shoesOptional.isPresent()) {
            Shoes shoes = shoesOptional.get();

            shoes.setType(updatedShoes.getType());
            shoes.setSize(updatedShoes.getSize());
            shoes.setManufacturer(updatedShoes.getManufacturer());

            shoesRepository.save(shoes);

            return new ResponseEntity<>(shoes, HttpStatus.OK);
        }

        return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
    }

    public ResponseEntity<String> deleteShoes(final int id) {
        Optional<Shoes> oldShoes = shoesRepository.findById(id);

        if (oldShoes.isPresent()) {
            shoesRepository.delete(oldShoes.get());
            return new ResponseEntity<>("", HttpStatus.OK);
        }

        return new ResponseEntity<>("", HttpStatus.NOT_FOUND);
    }
}
