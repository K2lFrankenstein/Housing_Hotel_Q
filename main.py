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

# CRUD Endpoints for Customer
@app.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = DBCustomer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/", response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    customers = db.query(DBCustomer).offset(skip).limit(limit).all()
    return customers

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(DBCustomer).filter(DBCustomer.customer_id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(DBCustomer).filter(DBCustomer.customer_id == customer_id).first()
    if db_customer:
        for attr, value in customer.dict().items():
            setattr(db_customer, attr, value)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{customer_id}", response_model=Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(DBCustomer).filter(DBCustomer.customer_id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return db_customer
    raise HTTPException(status_code=404, detail="Customer not found")

# CRUD Endpoints for RoomType
@app.post("/room_types/", response_model=RoomType)
def create_room_type(room_type: RoomTypeCreate, db: Session = Depends(get_db)):
    db_room_type = DBRoomType(**room_type.dict())
    db.add(db_room_type)
    db.commit()
    db.refresh(db_room_type)
    return db_room_type

@app.get("/room_types/", response_model=List[RoomType])
def read_room_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    room_types = db.query(DBRoomType).offset(skip).limit(limit).all()
    return room_types

@app.get("/room_types/{room_type_id}", response_model=RoomType)
def read_room_type(room_type_id: int, db: Session = Depends(get_db)):
    room_type = db.query(DBRoomType).filter(DBRoomType.room_type_id == room_type_id).first()
    if room_type is None:
        raise HTTPException(status_code=404, detail="Room type not found")
    return room_type

@app.put("/room_types/{room_type_id}", response_model=RoomType)
def update_room_type(room_type_id: int, room_type: RoomTypeCreate, db: Session = Depends(get_db)):
    db_room_type = db.query(DBRoomType).filter(DBRoomType.room_type_id == room_type_id).first()
    if db_room_type:
        for attr, value in room_type.dict().items():
            setattr(db_room_type, attr, value)
        db.commit()
        db.refresh(db_room_type)
        return db_room_type
    raise HTTPException(status_code=404, detail="Room type not found")

@app.delete("/room_types/{room_type_id}", response_model=RoomType)
def delete_room_type(room_type_id: int, db: Session = Depends(get_db)):
    db_room_type = db.query(DBRoomType).filter(DBRoomType.room_type_id == room_type_id).first()
    if db_room_type:
        db.delete(db_room_type)
        db.commit()
        return db_room_type
    raise HTTPException(status_code=404, detail="Room type not found")

# CRUD Endpoints for Chain
@app.post("/chains/", response_model=Chain)
def create_chain(chain: ChainCreate, db: Session = Depends(get_db)):
    db_chain = DBChain(**chain.dict())
    db.add(db_chain)
    db.commit()
    db.refresh(db_chain)
    return db_chain

@app.get("/chains/", response_model=List[Chain])
def read_chains(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    chains = db.query(DBChain).offset(skip).limit(limit).all()
    return chains

@app.get("/chains/{chain_id}", response_model=Chain)
def read_chain(chain_id: int, db: Session = Depends(get_db)):
    chain = db.query(DBChain).filter(DBChain.chain_id == chain_id).first()
    if chain is None:
        raise HTTPException(status_code=404, detail="Chain not found")
    return chain

@app.put("/chains/{chain_id}", response_model=Chain)
def update_chain(chain_id: int, chain: ChainCreate, db: Session = Depends(get_db)):
    db_chain = db.query(DBChain).filter(DBChain.chain_id == chain_id).first()
    if db_chain:
        for attr, value in chain.dict().items():
            setattr(db_chain, attr, value)
        db.commit()
        db.refresh(db_chain)
        return db_chain
    raise HTTPException(status_code=404, detail="Chain not found")

@app.delete("/chains/{chain_id}", response_model=Chain)
def delete_chain(chain_id: int, db: Session = Depends(get_db)):
    db_chain = db.query(DBChain).filter(DBChain.chain_id == chain_id).first()
    if db_chain:
        db.delete(db_chain)
        db.commit()
        return db_chain
    raise HTTPException(status_code=404, detail="Chain not found")

# CRUD Endpoints for Amenity
@app.post("/amenities/", response_model=Amenity)
def create_amenity(amenity: AmenityCreate, db: Session = Depends(get_db)):
    db_amenity = DBAmenity(**amenity.dict())
    db.add(db_amenity)
    db.commit()
    db.refresh(db_amenity)
    return db_amenity

@app.get("/amenities/", response_model=List[Amenity])
def read_amenities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    amenities = db.query(DBAmenity).offset(skip).limit(limit).all()
    return amenities

@app.get("/amenities/{amenities_id}", response_model=Amenity)
def read_amenity(amenities_id: int, db: Session = Depends(get_db)):
    amenity = db.query(DBAmenity).filter(DBAmenity.amenities_id == amenities_id).first()
    if amenity is None:
        raise HTTPException(status_code=404, detail="Amenity not found")
    return amenity

@app.put("/amenities/{amenities_id}", response_model=Amenity)
def update_amenity(amenities_id: int, amenity: AmenityCreate, db: Session = Depends(get_db)):
    db_amenity = db.query(DBAmenity).filter(DBAmenity.amenities_id == amenities_id).first()
    if db_amenity:
        for attr, value in amenity.dict().items():
            setattr(db_amenity, attr, value)
        db.commit()
        db.refresh(db_amenity)
        return db_amenity
    raise HTTPException(status_code=404, detail="Amenity not found")

@app.delete("/amenities/{amenities_id}", response_model=Amenity)
def delete_amenity(amenities_id: int, db: Session = Depends(get_db)):
    db_amenity = db.query(DBAmenity).filter(DBAmenity.amenities_id == amenities_id).first()
    if db_amenity:
        db.delete(db_amenity)
        db.commit()
        return db_amenity
    raise HTTPException(status_code=404, detail="Amenity not found")

# CRUD Endpoints for Reservation
@app.post("/reservations/", response_model=Reservation)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = DBReservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@app.get("/reservations/", response_model=List[Reservation])
def read_reservations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservations = db.query(DBReservation).offset(skip).limit(limit).all()
    return reservations

@app.get("/reservations/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(DBReservation).filter(DBReservation.reservation_id == reservation_id).first()
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@app.put("/reservations/{reservation_id}", response_model=Reservation)
def update_reservation(reservation_id: int, reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = db.query(DBReservation).filter(DBReservation.reservation_id == reservation_id).first()
    if db_reservation:
        for attr, value in reservation.dict().items():
            setattr(db_reservation, attr, value)
        db.commit()
        db.refresh(db_reservation)
        return db_reservation
    raise HTTPException(status_code=404, detail="Reservation not found")

@app.delete("/reservations/{reservation_id}", response_model=Reservation)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = db.query(DBReservation).filter(DBReservation.reservation_id == reservation_id).first()
    if db_reservation:
        db.delete(db_reservation)
        db.commit()
        return db_reservation
    raise HTTPException(status_code=404, detail="Reservation not found")

# CRUD Endpoints for Payment
@app.post("/payments/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = DBPayment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@app.get("/payments/", response_model=List[Payment])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    payments = db.query(DBPayment).offset(skip).limit(limit).all()
    return payments

@app.get("/payments/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(DBPayment).filter(DBPayment.payment_id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = db.query(DBPayment).filter(DBPayment.payment_id == payment_id).first()
    if db_payment:
        for attr, value in payment.dict().items():
            setattr(db_payment, attr, value)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    raise HTTPException(status_code=404, detail="Payment not found")

@app.delete("/payments/{payment_id}", response_model=Payment)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(DBPayment).filter(DBPayment.payment_id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
        return db_payment
    raise HTTPException(status_code=404, detail="Payment not found")

# CRUD Endpoints for ServiceOrder
@app.post("/service_orders/", response_model=ServiceOrder)
def create_service_order(service_order: ServiceOrderCreate, db: Session = Depends(get_db)):
    db_service_order = DBServiceOrder(**service_order.dict())
    db.add(db_service_order)
    db.commit()
    db.refresh(db_service_order)
    return db_service_order

@app.get("/service_orders/", response_model=List[ServiceOrder])
def read_service_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service_orders = db.query(DBServiceOrder).offset(skip).limit(limit).all()
    return service_orders

@app.get("/service_orders/{order_id}", response_model=ServiceOrder)
def read_service_order(order_id: int, db: Session = Depends(get_db)):
    service_order = db.query(DBServiceOrder).filter(DBServiceOrder.order_id == order_id).first()
    if service_order is None:
        raise HTTPException(status_code=404, detail="Service order not found")
    return service_order

@app.put("/service_orders/{order_id}", response_model=ServiceOrder)
def update_service_order(order_id: int, service_order: ServiceOrderCreate, db: Session = Depends(get_db)):
    db_service_order = db.query(DBServiceOrder).filter(DBServiceOrder.order_id == order_id).first()
    if db_service_order:
        for attr, value in service_order.dict().items():
            setattr(db_service_order, attr, value)
        db.commit()
        db.refresh(db_service_order)
        return db_service_order
    raise HTTPException(status_code=404, detail="Service order not found")

@app.delete("/service_orders/{order_id}", response_model=ServiceOrder)
def delete_service_order(order_id: int, db: Session = Depends(get_db)):
    db_service_order = db.query(DBServiceOrder).filter(DBServiceOrder.order_id == order_id).first()
    if db_service_order:
        db.delete(db_service_order)
        db.commit()
        return db_service_order
    raise HTTPException(status_code=404, detail="Service order not found")
# Define CRUD endpoints for Customer, RoomType, Chain, Amenity,
# Reservation, Payment, and ServiceOrder similarly.

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
