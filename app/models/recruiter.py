class Recruiter:

    def __init__(
        self,
        agency="",
        recruiter_name="",
        designation="",
        email="",
        phone="",
        linkedin="",
        website="",
        city="",
        hiring_for="",
        experience_required="",
        work_mode="",
        current_opening="",
        job_link="",
        hiring_location="",
        source="",
        verified="No",
        contacted="No",
        applied="No",
        reply_received="No",
        follow_up_date="",
        priority="Medium",
        notes=""
    ):

        self.agency = agency
        self.recruiter_name = recruiter_name
        self.designation = designation
        self.email = email
        self.phone = phone
        self.linkedin = linkedin
        self.website = website
        self.city = city
        self.hiring_for = hiring_for
        self.experience_required = experience_required
        self.work_mode = work_mode
        self.current_opening = current_opening
        self.job_link = job_link
        self.hiring_location = hiring_location
        self.source = source
        self.verified = verified
        self.contacted = contacted
        self.applied = applied
        self.reply_received = reply_received
        self.follow_up_date = follow_up_date
        self.priority = priority
        self.notes = notes