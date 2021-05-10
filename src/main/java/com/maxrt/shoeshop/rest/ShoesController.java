package com.maxrt.shoeshop.rest;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.maxrt.shoeshop.shoes.Shoes;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

@Path("/shoes")
public final class ShoesController {
    private static final HashMap<Integer, Shoes> SHOES = new HashMap<>();
    private static int nextId;

    private int getNextId() {
        return nextId++;
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public ArrayList<Shoes> getShoes() {
        return new ArrayList<>(SHOES.values());
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response postShoes(final String body) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Shoes newShoes = mapper.readValue(body, Shoes.class);
        newShoes.setId(getNextId());
        SHOES.put(newShoes.getId(), newShoes);
        return Response.ok(newShoes).build();
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getShoesById(@PathParam("id") final String id) {
        Shoes searchedShoes = SHOES.get(Integer.parseInt(id));
        if (searchedShoes == null) {
            return Response.status(Response.Status.NOT_FOUND)
                    .entity("Shoes not found for id = " + id)
                    .build();
        }
        return Response.ok(searchedShoes).build();
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response updateShoes(
            @PathParam("id") final String id,
            final Shoes updatedShoes) {
        Shoes oldShoes = SHOES.get(Integer.parseInt(id));

        if (oldShoes == null) {
            return Response.status(Response.Status.NOT_FOUND)
                    .entity("Shoes not found for id = " + id)
                    .build();
        }

        updatedShoes.setId(oldShoes.getId());

        SHOES.replace(updatedShoes.getId(), updatedShoes);

        return Response.ok(oldShoes).build();
    }

    @DELETE
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response deleteShoes(@PathParam("id") final String id) {
        Shoes oldShoes = SHOES.get(Integer.parseInt(id));

        if (oldShoes == null) {
            return Response.status(Response.Status.NOT_FOUND)
                    .entity("Shoes not found for id = " + id)
                    .build();
        }

        return Response.ok(SHOES.remove(oldShoes.getId())).build();
    }
}
