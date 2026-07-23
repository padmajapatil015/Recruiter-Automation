from dataclasses import dataclass


@dataclass
class Recruiter:

    agency: str
    email: str
    phone: str
    website: str
    city: str
    specialization: str
    hiring_location: str
    verified: bool = False