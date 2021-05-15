package com.maxrt.shoeshop.rest;

import com.maxrt.shoeshop.shoes.Shoes;
import org.springframework.beans.factory.annotation.Autowired;
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

    public Shoes createShoes(final Shoes newShoes) throws IOException {
        shoesRepository.save(newShoes);
        return newShoes;
    }

    public Optional<Shoes> getShoesById(final int id) {
        return shoesRepository.findById(id);
    }

    public Optional<Shoes> updateShoes(
            final int id,
            final Shoes updatedShoes) {
        Optional<Shoes> shoesOptional = shoesRepository.findById(id);

        if (shoesOptional.isPresent()) {
            updatedShoes.setId(id);
            shoesRepository.save(updatedShoes);

            return Optional.of(updatedShoes);
        }

        return Optional.empty();
    }

    public boolean deleteShoes(final int id) {
        Optional<Shoes> oldShoes = shoesRepository.findById(id);

        if (oldShoes.isPresent()) {
            shoesRepository.delete(oldShoes.get());
            return true;
        }

        return false;
    }
}
