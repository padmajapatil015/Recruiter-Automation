from dataclasses import dataclass


@dataclass
class Recruiter:

    agency: str

    recruiter_name: str

    email: str

    phone: str

    linkedin: str

    website: str

    city: str

    specialization: str

    current_opening: str

    hiring_location: str

    source: str

    verified: bool = False
