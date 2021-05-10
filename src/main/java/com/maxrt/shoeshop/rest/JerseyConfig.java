package com.maxrt.shoeshop.rest;

import org.glassfish.jersey.server.ResourceConfig;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.ws.rs.ApplicationPath;

@Component
@ApplicationPath("/")
public final class JerseyConfig extends ResourceConfig {
    @PostConstruct
    public void init() {
        registerClasses(ShoesController.class);
    }
}
