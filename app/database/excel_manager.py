import os
from datetime import datetime

import pandas as pd


class ExcelManager:

    def __init__(self):
        self.file_path = "data/Recruiters_Master.xlsx"

        self.columns = [
            "Agency",
            "Recruiter Name",
            "Designation",
            "Email",
            "Phone",
            "LinkedIn",
            "Website",
            "City",
            "Hiring For",
            "Experience Required",
            "Work Mode",
            "Current Opening",
            "Job Link",
            "Hiring Location",
            "Source",
            "Verified",
            "Contacted",
            "Applied",
            "Reply Received",
            "Follow Up Date",
            "Last Verified",
            "Priority",
            "Notes",
            "Added Date"
        ]

    def create_file(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_excel(self.file_path, index=False)

    def add_recruiter(self, recruiter):

        self.create_file()

        df = pd.read_excel(self.file_path)

        duplicate = df[df["Email"] == recruiter.email]

        if not duplicate.empty:
            return "Duplicate recruiter skipped"

        row = {

            "Agency": recruiter.agency,
            "Recruiter Name": recruiter.recruiter_name,
            "Designation": recruiter.designation,
            "Email": recruiter.email,
            "Phone": recruiter.phone,
            "LinkedIn": recruiter.linkedin,
            "Website": recruiter.website,
            "City": recruiter.city,
            "Hiring For": recruiter.hiring_for,
            "Experience Required": recruiter.experience_required,
            "Work Mode": recruiter.work_mode,
            "Current Opening": recruiter.current_opening,
            "Job Link": recruiter.job_link,
            "Hiring Location": recruiter.hiring_location,
            "Source": recruiter.source,
            "Verified": recruiter.verified,
            "Contacted": recruiter.contacted,
            "Applied": recruiter.applied,
            "Reply Received": recruiter.reply_received,
            "Follow Up Date": recruiter.follow_up_date,
            "Last Verified": datetime.now().strftime("%Y-%m-%d"),
            "Priority": recruiter.priority,
            "Notes": recruiter.notes,
            "Added Date": datetime.now().strftime("%Y-%m-%d")
        }

        df.loc[len(df)] = row

        df.to_excel(self.file_path, index=False)

        return "Recruiter added successfully"