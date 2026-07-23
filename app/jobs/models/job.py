class Job:

    def __init__(self):

        self.company = ""
        self.job_title = ""
        self.location = ""
        self.experience = ""
        self.work_mode = ""
        self.skills = ""
        self.salary = ""
        self.apply_link = ""
        self.source = ""
        self.date_found = ""

        # Resume Matching
        self.match_score = 0

        # Job Tracking
        self.status = "New"
        self.first_seen = ""
        self.last_seen = ""

        # Priority
        self.priority = "LOW"