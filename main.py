from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schema import Hotel, HotelCreate, Room, RoomCreate, Customer, CustomerCreate, RoomType, RoomTypeCreate
from schema import Chain, ChainCreate, Amenity, AmenityCreate, Reservation, ReservationCreate, Payment, PaymentCreate
from schema import ServiceOrder, ServiceOrderCreate
from db import SessionLocal, engine
from models import Base, Hotel as DBHotel, Room as DBRoom, Customer as DBCustomer
from models import RoomType as DBRoomType, Chain as DBChain, Amenity as DBAmenity
from models import Reservation as DBReservation, Payment as DBPayment, ServiceOrder as DBServiceOrder

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Endpoints for Hotel
@app.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = DBHotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

@app.get("/hotels/", response_model=List[Hotel])
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    hotels = db.query(DBHotel).offset(skip).limit(limit).all()
    return hotels

@app.get("/hotels/{hotel_id}", response_model=Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(DBHotel).filter(DBHotel.hotel_id == hotel_id).first()
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@app.put("/hotels/{hotel_id}", response_model=Hotel)
def update_hotel(hotel_id: int, hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = db.query(DBHotel).filter(DBHotel.hotel_id == hotel_id).first()
    if db_hotel:
        for attr, value in hotel.dict().items():
            setattr(db_hotel, attr, value)
        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    raise HTTPException(status_code=404, detail="Hotel not found")

@app.delete("/hotels/{hotel_id}", response_model=Hotel)
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = db.query(DBHotel).filter(DBHotel.hotel_id == hotel_id).first()
    if db_hotel:
        db.delete(db_hotel)
        db.commit()
        return db_hotel
    raise HTTPException(status_code=404, detail="Hotel not found")

# CRUD Endpoints for Room
@app.post("/rooms/", response_model=Room)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    db_room = DBRoom(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@app.get("/rooms/", response_model=List[Room])
def read_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rooms = db.query(DBRoom).offset(skip).limit(limit).all()
    return rooms

@app.get("/rooms/{room_id}", response_model=Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(DBRoom).filter(DBRoom.room_id == room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.put("/rooms/{room_id}", response_model=Room)
def update_room(room_id: int, room: RoomCreate, db: Session = Depends(get_db)):
    db_room = db.query(DBRoom).filter(DBRoom.room_id == room_id).first()
    if db_room:
        for attr, value in room.dict().items():
            setattr(db_room, attr, value)
        db.commit()
        db.refresh(db_room)
        return db_room
    raise HTTPException(status_code=404, detail="Room not found")

@app.delete("/rooms/{room_id}", response_model=Room)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = db.query(DBRoom).filter(DBRoom.room_id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
        return db_room
    raise HTTPException(status_code=404, detail="Room not found")

# Define CRUD endpoints for Customer, RoomType, Chain, Amenity,
# Reservation, Payment, and ServiceOrder similarly.

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
