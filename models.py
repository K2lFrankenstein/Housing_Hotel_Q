from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hotel(Base):
    __tablename__ = "hotels"

    hotel_id = Column(Integer, primary_key=True, index=True)
    chain_id = Column(Integer, ForeignKey("chains.chain_id"))
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    description = Column(Text)
    amenities_id = Column(Integer, ForeignKey("amenities.amenities_id"))
    timezone = Column(String, nullable=False)
    star_rating = Column(Integer, nullable=False)

    chain = relationship("Chain")
    amenities = relationship("Amenity")

class Room(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"))
    room_type_id = Column(Integer, ForeignKey("room_types.room_type_id"))
    room_number = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    basepay_per_night = Column(Float, nullable=False)
    floor = Column(Integer, nullable=False)
    description = Column(Text)
    status = Column(String, nullable=False)

    hotel = relationship("Hotel")
    room_type = relationship("RoomType")

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    chain_loyalty_no = Column(String)

class RoomType(Base):
    __tablename__ = "room_types"

    room_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    capacity = Column(Integer, nullable=False)

class Chain(Base):
    __tablename__ = "chains"

    chain_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    active_coupons = Column(Text)
    contact_info = Column(Text)

class Amenity(Base):
    __tablename__ = "amenities"

    amenities_id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    fees = Column(Float, nullable=False)
    description = Column(Text)

class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    check_in_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    number_of_guests = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    message_by_user = Column(Text)
    total_bill = Column(Float, nullable=False)
    payment_till_date = Column(Float, nullable=False)
    system_status = Column(String, nullable=False)

    room = relationship("Room")
    customer = relationship("Customer")

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservations.reservation_id"))
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    mode_of_payment = Column(String, nullable=False)

    reservation = relationship("Reservation")

class ServiceOrder(Base):
    __tablename__ = "service_orders"

    order_id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    order_date = Column(Date, nullable=False)
    total_bill = Column(Float, nullable=False)
    reservation_id = Column(Integer, ForeignKey("reservations.reservation_id"))

    reservation = relationship("Reservation")
