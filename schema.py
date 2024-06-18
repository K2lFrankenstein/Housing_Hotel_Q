from pydantic import BaseModel
from typing import Optional

# hotel schema
class HotelBase(BaseModel):
    chain_id: int
    name: str
    address: str
    city: str
    country: str
    phone: str
    email: str
    description: Optional[str] = None
    amenities_id: int
    timezone: str
    star_rating: int


class HotelCreate(HotelBase):
    pass


class Hotel(HotelBase):
    hotel_id: int

    class Config:
        orm_mode = True

# room schema

class RoomBase(BaseModel):
    hotel_id: int
    room_type_id: int
    room_number: str
    capacity: int
    basepay_per_night: float
    floor: int
    description: Optional[str] = None
    status: str


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    room_id: int

    class Config:
        orm_mode = True

# customer schema

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    chain_loyalty_no: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True

# roomtype schema

class RoomTypeBase(BaseModel):
    name: str
    description: Optional[str] = None
    capacity: int


class RoomTypeCreate(RoomTypeBase):
    pass


class RoomType(RoomTypeBase):
    room_type_id: int

    class Config:
        orm_mode = True

# chaine schema

class ChainBase(BaseModel):
    name: str
    description: Optional[str] = None
    active_coupons: Optional[str] = None
    contact_info: Optional[str] = None


class ChainCreate(ChainBase):
    pass


class Chain(ChainBase):
    chain_id: int

    class Config:
        orm_mode = True
        
# amenity schema
       
class AmenityBase(BaseModel):
    service_name: str
    fees: float
    description: Optional[str] = None


class AmenityCreate(AmenityBase):
    pass


class Amenity(AmenityBase):
    amenities_id: int

    class Config:
        orm_mode = True

# reservation schema

class ReservationBase(BaseModel):
    room_id: int
    customer_id: int
    check_in_date: str
    check_out_date: str
    number_of_guests: int
    status: str
    message_by_user: Optional[str] = None
    total_bill: float
    payment_till_date: float
    system_status: str


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    reservation_id: int

    class Config:
        orm_mode = True

# payment schema

class PaymentBase(BaseModel):
    reservation_id: int
    amount: float
    payment_date: str
    mode_of_payment: str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True


# serviceOrder schema

class ServiceOrderBase(BaseModel):
    service_name: str
    order_date: str
    total_bill: float
    reservation_id: int


class ServiceOrderCreate(ServiceOrderBase):
    pass


class ServiceOrder(ServiceOrderBase):
    order_id: int

    class Config:
        orm_mode = True
