from db.hoteles_db import HotelsInDB, database_hotels
from db.hoteles_db import  get_hotel, update_hotel
from typing import  Dict
from models.hotel_models import HotelIn, HotelInU, HotelOut
import json
import datetime
from fastapi import FastAPI, HTTPException
api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://g1m2-e12-app.herokuapp.com",
    
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

hotel_out = []*100
hotel_out.clear()

@api.post("/hotel/search/")
async def auth_hotel(hotel_in: HotelIn):
    hotel_out.clear()
    hotel_in_db = get_hotel(hotel_in.ciudad)
    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail= "No hay hoteles registrados") 
    i=0
    for clave in database_hotels.keys():
        if get_hotel(clave).ciudad == hotel_in_db.ciudad:
            if hotel_in.zona == get_hotel(clave).zona:
                i+=1
                hotel_out.append(get_hotel(clave).dict())
    if i!=0:
        return hotel_out
    else:
        raise HTTPException(status_code=403)

@api.get("/hotelname/{ciudad}")
async def get_hoteles(ciudad: str):
    hotel_out.clear()
    hotel_in_db = get_hotel(ciudad)
    if hotel_in_db == None:
        raise HTTPException(status_code=404,detail="No hay hoteles registrados en " + ciudad)
    for clave in database_hotels.keys():
        if get_hotel(clave).ciudad == hotel_in_db.ciudad:
            hotel_out.append(get_hotel(clave).dict())
    return hotel_out

@api.put("/hotelname/precio/")
async def make_update(hotel_in: HotelInU):
    hotel_out.clear()
    h_in_db = get_hotel(hotel_in.ciudad)
    if h_in_db == None:
        raise HTTPException(status_code=404,detail="No hay hoteles registrados en " + hotel_in.ciudad)
    i=0
    for clave in database_hotels.keys():
        if get_hotel(clave).ciudad == hotel_in.ciudad:
            if get_hotel(clave).hotelname == hotel_in.hotelname:
                if get_hotel(clave).zona == hotel_in.zona:
                    i+=1
                    get_hotel(clave).tarifa_inicial=hotel_in.tarifa_inicial
                    update_hotel(get_hotel(clave))
                    print(get_hotel(clave))
                    hotel_out[i] = HotelOut(**get_hotel(clave).dict())
                    return hotel_out
    return "No hay hoteles " + hotel_in.hotelname + " al " + hotel_in.zona + " de " + hotel_in.ciudad