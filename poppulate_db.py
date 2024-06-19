from sqlalchemy.orm import Session
from faker import Faker
import random

from db import engine, SessionLocal
from models import Base, Hotel, Room, Customer, RoomType, Chain, Amenity, Reservation, Payment, ServiceOrder

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize Faker
fake = Faker()

# Create a new database session
db = SessionLocal()

def create_fake_hotels(n):
    hotels = []
    for _ in range(n):
        hotel = Hotel(
            chain_id=random.randint(1, 5),
            name=fake.company(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            phone=fake.phone_number(),
            email=fake.email(),
            description=fake.text(max_nb_chars=200),
            amenities_id=random.randint(1, 10),
            timezone=fake.timezone(),
            star_rating=random.randint(1, 5)
        )
        hotels.append(hotel)
        db.add(hotel)
    db.commit()
    return hotels

def create_fake_rooms(n):
    rooms = []
    for _ in range(n):
        room = Room(
            hotel_id=random.randint(1, 10),
            room_type_id=random.randint(1, 5),
            room_number=fake.bothify(text='Room ###'),
            capacity=random.randint(1, 5),
            basepay_per_night=round(random.uniform(50, 500), 2),
            floor=random.randint(1, 10),
            description=fake.text(max_nb_chars=200),
            status=random.choice(['available', 'not available'])
        )
        rooms.append(room)
        db.add(room)
    db.commit()
    return rooms

def create_fake_customers(n):
    customers = []
    for _ in range(n):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            chain_loyalty_no=fake.bothify(text='Loyalty-####')
        )
        customers.append(customer)
        db.add(customer)
    db.commit()
    return customers

def create_fake_room_types(n):
    room_types = []
    room_name = [
        "Standard Room",
        "Deluxe Room",
        "Suite",
        "Executive Suite",
        "Presidential Suite",
        "Family Room",
        "Accessible Room",
        "Smoking Room",
        "Non-Smoking Room",
        "Ocean View Room",
        "City View Room",
    ]
    for _ in range(n):
        room_type = RoomType(
            name=random.choice(room_name),
            description=fake.text(max_nb_chars=200),
            capacity=random.randint(1, 5)
        )
        room_types.append(room_type)
        db.add(room_type)
    db.commit()
    return room_types

def create_fake_chains(n):
    chains = []
    for _ in range(n):
        chain = Chain(
            name=fake.company(),
            description=fake.text(max_nb_chars=200),
            active_coupons=fake.word(),
            contact_info=fake.phone_number()
        )
        chains.append(chain)
        db.add(chain)
    db.commit()
    return chains

def create_fake_amenities(n):
    amenities = []
    for _ in range(n):
        amenity = Amenity(
            service_name=random.choice(['Restaurant', 'Spa', 'Dry Cleaning', 'Extra Bed']),
            fees=round(random.uniform(10, 100), 2),
            description=fake.text(max_nb_chars=200)
        )
        amenities.append(amenity)
        db.add(amenity)
    db.commit()
    return amenities

def create_fake_reservations(n):
    reservations = []
    for _ in range(n):
        reservation = Reservation(
            room_id=random.randint(1, 10),
            customer_id=random.randint(1, 10),
            check_in_date=fake.date_this_year(),
            check_out_date=fake.date_this_year(),
            number_of_guests=random.randint(1, 4),
            status=random.choice(['booked', 'checked-in', 'checked-out', 'canceled']),
            message_by_user=fake.text(max_nb_chars=200),
            total_bill=round(random.uniform(100, 1000), 2),
            payment_till_date=round(random.uniform(50, 500), 2),
            system_status=random.choice(['clear', 'error'])
        )
        reservations.append(reservation)
        db.add(reservation)
    db.commit()
    return reservations

def create_fake_payments(n):
    payments = []
    for _ in range(n):
        payment = Payment(
            reservation_id=random.randint(1, 10),
            amount=round(random.uniform(50, 500), 2),
            payment_date=fake.date_this_year(),
            mode_of_payment=random.choice(['credit card', 'cash', 'online'])
        )
        payments.append(payment)
        db.add(payment)
    db.commit()
    return payments

def create_fake_service_orders(n):
    service_orders = []
    for _ in range(n):
        service_order = ServiceOrder(
            service_name=random.choice(['Spa', 'Room Service', 'Laundry']),
            order_date=fake.date_this_year(),
            total_bill=round(random.uniform(20, 200), 2),
            reservation_id=random.randint(1, 10)
        )
        service_orders.append(service_order)
        db.add(service_order)
    db.commit()
    return service_orders

# Create fake data
create_fake_chains(5)
create_fake_amenities(10)
create_fake_hotels(10)
create_fake_room_types(5)
create_fake_rooms(20)
create_fake_customers(10)
create_fake_reservations(15)
create_fake_payments(20)
create_fake_service_orders(15)

# Close the database session
db.close()
