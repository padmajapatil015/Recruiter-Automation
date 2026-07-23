import os
import pandas as pd
from datetime import datetime


class ExcelManager:

    def __init__(self):

        self.file_path = "data/Recruiters_Master.xlsx"

        self.columns = [
            "Agency",
            "Recruiter Name",
            "Email",
            "Phone",
            "LinkedIn",
            "Website",
            "City",
            "Specialization",
            "Current Opening",
            "Hiring Location",
            "Source",
            "Verified",
            "Contacted",
            "Applied",
            "Follow Up",
            "Notes",
            "Added Date"
        ]


    def create_file(self):

        if not os.path.exists(self.file_path):

            df = pd.DataFrame(columns=self.columns)

            df.to_excel(
                self.file_path,
                index=False
            )


    def add_recruiter(self, recruiter):

        self.create_file()

        df = pd.read_excel(self.file_path)


        if recruiter.email in df["Email"].values:
            return "Duplicate recruiter skipped"


        new_data = {

            "Agency": recruiter.agency,
            "Recruiter Name": recruiter.recruiter_name,
            "Email": recruiter.email,
            "Phone": recruiter.phone,
            "LinkedIn": recruiter.linkedin,
            "Website": recruiter.website,
            "City": recruiter.city,
            "Specialization": recruiter.specialization,
            "Current Opening": recruiter.current_opening,
            "Hiring Location": recruiter.hiring_location,
            "Source": recruiter.source,
            "Verified": recruiter.verified,
            "Contacted": "No",
            "Applied": "No",
            "Follow Up": "",
            "Notes": "",
            "Added Date": datetime.now().strftime("%Y-%m-%d")
        }


        df.loc[len(df)] = new_data


        df.to_excel(
            self.file_path,
            index=False
        )


        return "Recruiter added successfully"
