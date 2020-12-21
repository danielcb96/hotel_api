from pydantic import BaseModel

class HotelIn(BaseModel):
    #hotelname: str
    ciudad: str
    zona: str
    mes: str

class HotelIn1(BaseModel):
    #hotelname: str
    ciudad: str
    # zona: str
    mes: str

class HotelInU(BaseModel):
    hotelname: str
    ciudad: str
    zona: str
    tarifa_inicial: float
    #mes: str

class HotelOut(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_inicial:float
    #ciudad: str
    zona: str

class HotelOut_a(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_alta:float
    #ciudad: str
    zona: str

class HotelOut_b(BaseModel):
    hotelname: str
    estrellas: str
    tipo_habitacion: str
    tarifa_baja:float
    #ciudad: str
    zona: str
   
    
