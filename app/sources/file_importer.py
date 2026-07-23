import os
import pandas as pd

from app.models.recruiter import Recruiter


class FileImporter:

    def __init__(self):
        self.import_folder = "imports"

    def fetch(self):

        recruiters = []

        if not os.path.exists(self.import_folder):
            return recruiters

        for file in os.listdir(self.import_folder):

            path = os.path.join(self.import_folder, file)

            if file.endswith(".csv"):
                df = pd.read_csv(path)

            elif file.endswith(".xlsx"):
                df = pd.read_excel(path)

            else:
                continue

            for _, row in df.iterrows():

                recruiter = Recruiter()

                recruiter.agency = str(row.get("Agency", ""))
                recruiter.recruiter_name = str(row.get("Recruiter Name", ""))
                recruiter.designation = str(row.get("Designation", ""))
                recruiter.email = str(row.get("Email", ""))
                recruiter.phone = str(row.get("Phone", ""))
                recruiter.linkedin = str(row.get("LinkedIn", ""))
                recruiter.website = str(row.get("Website", ""))
                recruiter.city = str(row.get("City", ""))
                recruiter.hiring_for = str(row.get("Hiring For", ""))
                recruiter.experience_required = str(row.get("Experience Required", ""))
                recruiter.work_mode = str(row.get("Work Mode", ""))
                recruiter.current_opening = str(row.get("Current Opening", ""))
                recruiter.job_link = str(row.get("Job Link", ""))
                recruiter.hiring_location = str(row.get("Hiring Location", ""))
                recruiter.source = str(row.get("Source", ""))
                recruiter.verified = str(row.get("Verified", ""))
                recruiter.contacted = str(row.get("Contacted", ""))
                recruiter.applied = str(row.get("Applied", ""))
                recruiter.reply_received = str(row.get("Reply Received", ""))
                recruiter.follow_up_date = str(row.get("Follow Up Date", ""))
                recruiter.priority = str(row.get("Priority", ""))
                recruiter.notes = str(row.get("Notes", ""))

                recruiters.append(recruiter)

        return recruiters