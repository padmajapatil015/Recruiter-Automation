from dataclasses import dataclass


@dataclass
class Recruiter:

    agency: str
    recruiter_name: str
    designation: str
    email: str
    phone: str
    linkedin: str
    website: str
    city: str
    hiring_for: str
    experience_required: str
    work_mode: str
    current_opening: str
    job_link: str
    hiring_location: str
    source: str
    verified: bool
    contacted: bool = False
    applied: bool = False
    reply_received: bool = False
    follow_up_date: str = ""
    last_verified: str = ""
    priority: str = "Medium"
    notes: str = ""