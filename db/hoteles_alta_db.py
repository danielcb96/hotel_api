# from typing import  Dict
# from pydantic import BaseModel

# class HotelsInDB_alta(BaseModel):
#     hotelname: str
#     estrellas: str
#     tipo_habitacion: str
#     tarifa_inicial:float
#     ciudad: str
#     zona: str
    
# database_hotels_alta = Dict[str, HotelsInDB_alta]

# database_hotels_alta = {
#     "Bogotá": HotelsInDB_alta(**{"hotelname":"Tequendama", 
#                             "estrellas":"4",
#                             "tarifa_inicial":350000,
#                             "tipo_habitacion":"Doble",
#                             "ciudad":"Bogotá", 
#                             "zona":"Centro"}),
#     "Bogotá1": HotelsInDB_alta(**{"hotelname":"Hotel NoTeVayas", 
#                             "estrellas":"1",
#                             "tarifa_inicial":25000,
#                             "tipo_habitacion":"Cama individual",
#                             "ciudad":"Bogotá", 
#                             "zona":"Sur"}),
#     "Bogotá2": HotelsInDB_alta(**{"hotelname":"Hotel aquiTeQuedas", 
#                             "estrellas":"4",
#                             "tarifa_inicial":70000,
#                             "tipo_habitacion":"sencilla",
#                             "ciudad":"Bogotá", 
#                             "zona":"Centro"}),
#     "Bogotá3": HotelsInDB_alta(**{"hotelname":"Decameron", 
#                             "estrellas":"5",
#                             "tarifa_inicial":950000,
#                             "tipo_habitacion":"Doble",
#                             "ciudad":"Bogotá", 
#                             "zona":"Norte"}),
#     "Bogotá4": HotelsInDB_alta(**{"hotelname":"Camaleon", 
#                             "estrellas":"5",
#                             "tarifa_inicial":450000,
#                             "tipo_habitacion":"Sencilla",
#                             "ciudad":"Bogotá", 
#                             "zona":"Centro"}),
# }

# def get_hotel_alta(hotelname: str):
#     if hotelname in database_hotels_alta.keys():
#         return database_hotels_alta[hotelname]
#     else: 
#         return None
    
    
# def update_hotel(hotel_in_db: HotelsInDB):
#     for clave in database_hotels.keys():
#         if get_hotel(clave).ciudad == hotel_in_db.ciudad:
#             if get_hotel(clave).hotelname == hotel_in_db.hotelname:
#                 get_hotel(clave).tarifa_inicial=hotel_in_db.tarifa_inicial
#                 database_hotels[clave] = get_hotel(clave)
#                 return hotel_in_db
