from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
  user_id: Primary Key [int]
  email: str Unique
  password: str
  role: str

@dataclass
class House:
  house_id: Primary Key [int]
  owner_name: str
  house_name: str
  house_address: str
  monthly_rent: float
  bedrooms: int
  bathrooms: int
  house_type: str
  date_added: str
  availability: str = "AVAILABLE", "RENTED", "NOT AVAILABLE"
  image_filename: str
  
@dataclass
class Rental:
  rental_id: PRIMARY KEY [int]
  house_id: int
  user_id: int
  renter_name: str
  contact_num: str
  date_rented: str
  duration_months: int
  status: str = "ACTIVE", "RETURNED", "CANCELLED"
  closed_date: Optional[str] = None
  cancel_reason: Optional[str] = None