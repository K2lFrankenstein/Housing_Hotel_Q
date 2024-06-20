## Question 1: A Room Reservation System for a Global Hotel Chain:



## Question 2: ETL Process for Creating final.csv

## Overview

The goal of this ETL (Extract, Transform, Load) process is to merge data from multiple CSV files (`occupancy_data.csv`, `majors_data.csv`, `inventory_data.csv`, `persons_data.csv`) into a final CSV file (`final.csv`) that meets specific requirements. These requirements include creating a unified dataset with unique `personId`, handling missing values, and formatting data appropriately.

## Steps and Processes

### 1. Extraction

Data is extracted from the following CSV files:
- `occupancy_data.csv`: Contains occupancy information including `personId`, `buildingName`, `roomName`, and `bedName`.
- `majors_data.csv`: Contains data on majors with `id`, `displayId`, `name`, and `description`.
- `inventory_data.csv`: Provides inventory details including `buildingName`, `roomName`, `bedName`, and `bedId`.
- `persons_data.csv`: Includes personal information such as `personId`, `firstName`, `lastName`, `email`, `dob`, `address`, and `majors`.

### 2. Transformation

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

### 3. Loading

#### Final Output:
- The transformed data is saved into `final.csv`, which includes the following columns:
  1. `personId`: Unique identifier (UUID).
  2. `name`: Full name (concatenation of `firstName` and `lastName`).
  3. `email`: Unique email address.
  4. `dob`: Date of birth (formatted as a string).
  5. `address1`, `address2`, `city`, `state`, `zip`: Address components if available.
  6. `majorIds`: Comma-separated string of major IDs associated with each person.
  7. `bedId`: Identifier from inventory data associated with each occupancy record.

### Reasons for Steps taken

#### 1. Description of Data Cleaning Policies Applied:
- **Handling Missing Values**: `NaN` values in `personId` could be handled with a new UUID to ensure each person has a unique identifier. Missing addresses were handled by checking for existing components before splitting. The `majorIds` were mapped from HashMap for effective implementation and `Nan` handling.
- **Formatting**: Data such as `address` was deconstructed into `address1`, `address2`, `city`, `state`, `zip` to ensure consistency.
- **Duplicate Handling**: Duplicates in `personId` and `email` were managed to maintain data integrity and uniqueness.


#### 2. Rows Not Included in the Final Sheet:
- Rows that could not be included in the final sheet typically involved:
  - **Missing `personId` or `email`**: Entries without valid `personId` or `email` were excluded as these are essential for uniqueness and identification. A total of `4900` rows were deleted while removing the redundancy in `emails` because it was one of the base requirements of the new file that the `email` field should be unique.
    
    ![image](https://github.com/K2lFrankenstein/Housing_Hotel_Q/assets/68675641/685db7d9-38aa-42ee-8ca8-de7552c24fa1)
  
  - **Incomplete Address Information**: Entries with incomplete or missing address components (`address1`, `city`, `state`) were omitted to ensure data quality and completeness. It was implemented but was not required as all the addresses were present.
