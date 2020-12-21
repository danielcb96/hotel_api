from db.hoteles_db import HotelsInDB, database_hotels
from db.hoteles_db import  get_hotel, update_hotel
from typing import  Dict
from models.hotel_models import HotelIn, HotelInU, HotelOut, HotelOut_a,HotelOut_b
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
a={}
hotel_out.clear()

@api.post("/hotel/search/")
async def auth_hotel(hotel_in: HotelIn):
    hotel_out.clear()
    hotel_in_db = get_hotel(hotel_in.ciudad)
    if hotel_in_db == None:
        raise HTTPException(status_code=404, detail= "No hay hoteles registrados") 
    i=0
    for clave in database_hotels.keys():
        a = get_hotel(clave)
        if a.ciudad == hotel_in_db.ciudad:
            if hotel_in.zona == a.zona:
                i+=1
                if(hotel_in.mes == "Marzo" or hotel_in.mes == "Abril" or hotel_in.mes == "Mayo" or hotel_in.mes == "Junio" ):
                    hotel_out.append(HotelOut(**a.dict()))

                if(hotel_in.mes == "Noviembre" or hotel_in.mes == "Diciembre" or hotel_in.mes == "Enero" or hotel_in.mes == "Febrero" ):
                    hotel_out.append(HotelOut_a(**a.dict()))

                if(hotel_in.mes == "Julio" or hotel_in.mes == "Agosto" or hotel_in.mes == "Septiembre" or hotel_in.mes == "Octubre" ):
                    hotel_out.append(HotelOut_b(**a.dict()))                                        
    if i!=0:       
        return hotel_out
    else:
        raise HTTPException(status_code=403)                               
                                       
@api.get("/hotelname/{ciudad}/{mes}")
async def get_hoteles(ciudad: str,mes: str):
    hotel_out.clear()
    hotel_in_db = get_hotel(ciudad)
    if hotel_in_db == None:
        raise HTTPException(status_code=404,detail="No hay hoteles registrados en " + ciudad)
    for clave in database_hotels.keys():
        a=get_hotel(clave)
        if a.ciudad == hotel_in_db.ciudad:
            if(mes == "Marzo" or mes == "Abril" or mes == "Mayo" or mes == "Junio" ):
                hotel_out.append(HotelOut(**a.dict()))

            if(mes == "Noviembre" or mes == "Diciembre" or mes == "Enero" or mes == "Febrero" ):
                hotel_out.append(HotelOut_a(**a.dict()))

            if(mes == "Julio" or mes == "Agosto" or mes == "Septiembre" or mes == "Octubre" ):
                hotel_out.append(HotelOut_b(**a.dict()))
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