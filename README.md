# Question 1: A Room Reservation System for a Global Hotel Chain:

## Schema and Reasoning for Schema

![image](https://github.com/K2lFrankenstein/Housing_Hotel_Q/assets/68675641/63e2ce42-6f68-4899-a169-e6a5e9f3e5d3)


#### Hotels Table
- **hotel_id (PK)**: Unique identifier for each hotel.
- **chain_id (FK)**: Foreign key linking to the Chain table to identify which chain the hotel belongs to.
- **Name**: Name of the hotel.
- **Address, City, Country**: Physical location details of the hotel.
- **Phone, Email**: Contact information for the hotel.
- **Description**: Additional information or description about the hotel.
- **Amenities_ID (FK)**: Foreign key linking to the Amenities table to specify available amenities.
- **Timezone**: Timezone in which the hotel operates.
- **Star Rating**: Rating of the hotel typically used for quality assessment.

#### Rooms Table
- **room_id (PK)**: Unique identifier for each room.
- **Hotel_id (FK)**: Foreign key linking to the Hotels table to identify which hotel the room belongs to.
- **Room_type_id (FK)**: Foreign key linking to the Room_type table to specify the type of room.
- **Room_number**: Room number or identifier within the hotel.
- **Capacity**: Maximum capacity (number of guests) the room can accommodate.
- **Basepay_per_night**: Base price per night for renting the room.
- **Floor**: Floor number where the room is located.
- **Description - amenities**: Description of amenities available in the room.
- **Status**: Current availability status of the room (available/not).

#### Customer Table
- **customer_id (PK)**: Unique identifier for each customer.
- **First Name, Last Name**: Customer's name.
- **Email, Phone number, Address**: Contact details and location information for the customer.
- **Chain_loyalty_no**: Loyalty number or identifier if the customer is part of a loyalty program within the hotel chain.

#### Room_type Table
- **room_type_id (PK)**: Unique identifier for each room type.
- **Name**: Name of the room type (e.g., standard, double).
- **Description**: Description of the room type.
- **Capacity**: Maximum capacity (number of guests) the room type can accommodate.

#### Chain Table
- **chain_id (PK)**: Unique identifier for each hotel chain.
- **Name**: Name of the hotel chain.
- **Description**: Description or additional information about the hotel chain.
- **Active_coupons**: Information about active promotional coupons or discounts available within the chain.
- **Contact_info**: Contact information for the hotel chain.

#### Amenities Table
- **amenities_id (PK)**: Unique identifier for each amenity.
- **ServiceName**: Name of the service or amenity provided (e.g., restaurant, spa, dry cleaning).
- **Fees**: Fees associated with using the amenity.
- **Description**: Description or additional details about the amenity.

#### Reservation Table
- **reservation_id (PK)**: Unique identifier for each reservation.
- **Room_id (FK)**: Foreign key linking to the Rooms table to identify the room reserved.
- **Customer_id (FK)**: Foreign key linking to the Customers table to identify the customer who made the reservation.
- **Check_in_date, Check_out_date**: Dates specifying when the guest checks in and checks out.
- **Number of Guests**: Number of guests covered by the reservation.
- **Status**: Current status of the reservation (booked, checked-in, checked-out, canceled).
- **Message_by_user**: Any additional messages or notes provided by the user during reservation.
- **Total Bill**: Total amount due for the reservation.
- **Payment_tillday**: Payment status or amount paid till date.
- **System_status**: System status messages related to the reservation (error messages, verification issues, payment status).

#### Payments Table
- **payment_id (PK)**: Unique identifier for each payment.
- **reservation_id (FK)**: Foreign key linking to the Reservation table to identify the reservation for which payment is made.
- **Amount**: Amount paid.
- **Payment_date**: Date and time when the payment was made.
- **Mode_of_Payment**: Mode of payment used (credit card, cash, etc.).

#### ServiceOrders Table
- **Order_id (PK)**: Unique identifier for each service order.
- **Service_Name**: Name of the service ordered (e.g., spa, restaurant).
- **OrderDate**: Date when the service order was placed.
- **Total_bill**: Total amount due for the service order.
- **reservation_id (FK)**: Foreign key linking to the Reservation table to identify the reservation associated with the service order.

## Business and Complex Operations Support

The schema supports the following complex operations crucial for a room reservation system by establishing clear relationships between entities:

1. **Searching Hotels and Filtering Based on Room Prices**: Implemented through endpoints that allow filtering by city and price range.
   
2. **Reservation Finalization**: Creation of reservations, updating room availability, and managing payment transactions.

3. **Checkout**: Retrieving guest information, calculating total costs including service charges, and updating reservation status to checked-out.

4. **Adding Service Charges**: Handling additional charges for amenities used during the stay, reflected in the reservation and payment records.

## Why it is Scalable ?

1. **Modular Design**: By breaking down the schema into separate tables (Hotels, Rooms, Customers, etc.), each serving a specific entity or relationship, I ensured that changes or expansions to one part of the system do not necessitate restructuring the entire database. This modularity allows for agile development and easier management of schema evolution over time.
   
2. **Indexes and Foreign Keys**: Careful selection and application of indexes on commonly queried columns (such as Room_id, Customer_id) ensure that database operations remain efficient regardless of the data volume. Foreign keys enforce data consistency across related tables, preventing orphaned records and maintaining relational integrity as new data is added.
   
3. **Normalization**: Through normalization techniques (such as breaking down data into smaller logical units and reducing data redundancy), I optimized storage and retrieval efficiency. This approach supports the scalability of the database by minimizing the risk of data anomalies and improving overall system performance during complex operations.

## Steps to Perform to Keep it Scalable

1. **Regular Performance Monitoring**: Monitor database performance metrics and optimize queries as needed.
   
2. **Horizontal Scaling**: Consider partitioning large tables and implementing sharding as data volume grows.
   
3. **Schema Evolution**: Evolve the schema based on changing business requirements, ensuring it remains efficient and scalable.
   
This structured approach ensures that the room reservation system remains robust, performant, and adaptable to meet the evolving needs of a global hotel chain.

---

# Swagger API Endpoint

    This API Endpoints are created to show a quick demo operations of a room reservation system for a global hotel chain

    Here are the list of Endpoints:

    | Endpoint                                       | Description                                                                                      |
    |------------------------------------------------|--------------------------------------------------------------------------------------------------|
    | /hotels/                                       | CRUD operations for hotels: Create a new hotel, Read all hotels, .                               |
    | /hotels/{hotel_id}                             | Get, Update, or Delete a specific hotel by ID                                                    |
    | /hotels/search/?city={}&min_price={}           | Search hotels by city and filter based on room prices                                            |
    |                        &max_price={}           |                                                                                                  |
    | /rooms/                                        | CRUD operations for rooms: Create a new room, Read all rooms, .                                  |
    | /rooms/{room_id}                               | Get, Update, or Delete a specific room by ID                                                     |
    |                                                |                                                                                                  |
    | /customers/                                    | CRUD operations for customers: Create a new customer, Read all customers,                        |
    | /customers/{customer_id}                       | Get, Update, or Delete a specific customer by ID                                                 |
    |                                                |                                                                                                  |
    | /room_types/                                   | CRUD operations for room types: Create a new room type, Read all room types,                     |
    | /room_types/{room_type_id}                     | Get, Update, or Delete a specific room type by ID                                                |
    |                                                |                                                                                                  |
    | /chains/                                       | CRUD operations for hotel chains: Create a new chain, Read all chains, .                         |
    | /chains/{chain_id}                             | Get, Update, or Delete a specific chain by ID                                                    |
    |                                                |                                                                                                  |
    | /amenities/                                    | CRUD operations for amenities: Create a new amenity, Read all amenities, .                       |
    | /amenities/{amenity_id}                        | Get, Update, or Delete a specific amenity by ID                                                  |
    |                                                |                                                                                                  |
    | /reservations/                                 | CRUD operations for reservations: Create a new reservation, Read all reservations, .             |
    | /reservations/{reservation_id}                 | Get, Update, or Delete a specific reservation by ID                                              |
    | /reservations/{reservation_id}/checkout/       | Checkout operation: Finalizes the reservation, calculates costs, and updates status              |
    | /reservations/{reservation_id}/service_charge/ | Adds service charges to a reservation                                                            |
    |                                                |                                                                                                  |
    | /payments/                                     | CRUD operations for payments: Create a new payment, Read all payments, .                         |
    | /payments/{payment_id}                         | Get, Update, or Delete a specific payment by ID                                                  |
    |                                                |                                                                                                  |
    | /service_orders/                               | CRUD operations for service orders: Create a new service order, Read all service orders, .       |
    | /service_orders/{order_id}                     | Get, Update, or Delete a specific service order by ID                                            |
    |                                                |                                                                                                  |



---

# Question 2: ETL Process for Creating final.csv

## Overview

The goal of this ETL (Extract, Transform, Load) process is to merge data from multiple CSV files (`occupancy_data.csv`, `majors_data.csv`, `inventory_data.csv`, `persons_data.csv`) into a final CSV file (`final.csv`) that meets specific requirements. These requirements include creating a unified dataset with unique `personId`, handling missing values, and formatting data appropriately.


## 1. Extraction

Data is extracted from the following CSV files:
- `occupancy_data.csv`: Contains occupancy information including `personId`, `buildingName`, `roomName`, and `bedName`.
- `majors_data.csv`: Contains data on majors with `id`, `displayId`, `name`, and `description`.
- `inventory_data.csv`: Provides inventory details including `buildingName`, `roomName`, `bedName`, and `bedId`.
- `persons_data.csv`: Includes personal information such as `personId`, `firstName`, `lastName`, `email`, `dob`, `address`, and `majors`.

## 2. Transformation

#### Data Cleaning and Validations Applied:
- **Data staging**:
    - Checking the data's values, shapes and description to ensure consistency and requirements for any normalization to the columns.
- **Handling Duplicates**:
  - Ensuring each `personId` is unique across the dataset while handelling any `NAN` values and concerently generation UUID if necessary.
  - Removing duplicate `email` entries to maintain data integrity.
- **Handling Missing Values**: 
  - `NaN` values in `personId` are replaced with a new UUID to ensure uniqueness.
  - Missing addresses are handled by splitting and assigning components (`address1`, `address2`, `city`, `state`, `zip`) only if they exist in the data or else replacing it with `None`.
- **Data Formatting**:
  - Concatenation of `firstName` and `lastName` to create a `name` column.
  - Transforming and formatting `majorIds` by mapping major names to their corresponding IDs from `majors_data.csv` and performing it efficiently to reduce execution time using Hashmap.
  - The final required fields (`address1`, `address2`, `city`, `state`, `zip`) were formed out by deconstructing the `address` column.
  - The `bedId` was obtained by merging `occupancy_data` with `inventory_data`. 

## 3. Loading Final Output:
- The transformed data is saved into `final.csv`, which includes the following columns:
  1. `personId`: Unique identifier (UUID).
  2. `name`: Full name (concatenation of `firstName` and `lastName`).
  3. `email`: Unique email address.
  4. `dob`: Date of birth (formatted as a string).
  5. `address1`, `address2`, `city`, `state`, `zip`: Address components if available.
  6. `majorIds`: Comma-separated string of major IDs associated with each person.
  7. `bedId`: Identifier from inventory data associated with each occupancy record.

## Reasons for Steps taken

#### 1. Description of Data Cleaning Policies Applied:
- **Handling Missing Values**: `NaN` values in `personId` could be handled with a new UUID to ensure each person has a unique identifier. Missing addresses were handled by checking for existing components before splitting. The `majorIds` were mapped from HashMap for effective implementation and `Nan` handling.
- **Formatting**: Data such as `address` was deconstructed into `address1`, `address2`, `city`, `state`, `zip` to ensure consistency.
- **Duplicate Handling**: Duplicates in `personId` and `email` were managed to maintain data integrity and uniqueness.


#### 2. Rows Not Included in the Final Sheet:
- Rows that could not be included in the final sheet typically involved:
  - **Missing `personId` or `email`**: Entries without valid `personId` or `email` were excluded as these are essential for uniqueness and identification. A total of `4900` rows were deleted while removing the redundancy in `emails` because it was one of the base requirements of the new file that the `email` field should be unique.
    
    ![image](https://github.com/K2lFrankenstein/Housing_Hotel_Q/assets/68675641/685db7d9-38aa-42ee-8ca8-de7552c24fa1)
  
  - **Incomplete Address Information**: Entries with incomplete or missing address components (`address1`, `city`, `state`) were omitted to ensure data quality and completeness. It was implemented but was not required as all the addresses were present.
