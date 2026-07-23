import os
import pandas as pd
from datetime import datetime


class JobExcelManager:

    def __init__(self):

        self.file_path = "data/Today_Jobs.xlsx"

        self.columns = [
            "Company",
            "Job Title",
            "Location",
            "Experience",
            "Work Mode",
            "Skills",
            "Salary",
            "Apply Link",
            "Source",
            "Date Found",
            "Match Score",
            "Status",
            "First Seen",
            "Last Seen"
        ]


    def create_file(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):

            df = pd.DataFrame(
                columns=self.columns
            )

            df.to_excel(
                self.file_path,
                index=False
            )


    def find_job(self, job):

        df = pd.read_excel(
            self.file_path
        )

        if df.empty:
            return None


        result = df[
            (df["Company"] == job.company) &
            (df["Job Title"] == job.job_title)
        ]


        if not result.empty:
            return result.index[0]


        return None



    def add_job(self, job):

        self.create_file()

        today = datetime.now().strftime(
            "%d-%b-%Y"
        )


        df = pd.read_excel(
            self.file_path
        )


        existing_index = self.find_job(job)


        if existing_index is not None:

            df.loc[
                existing_index,
                "Status"
            ] = "Existing"


            df.loc[
                existing_index,
                "Last Seen"
            ] = today


            df.to_excel(
                self.file_path,
                index=False
            )


            print(
                "Existing job updated:",
                job.company,
                job.job_title
            )

            return



        new_row = {

            "Company": job.company,
            "Job Title": job.job_title,
            "Location": job.location,
            "Experience": job.experience,
            "Work Mode": job.work_mode,
            "Skills": job.skills,
            "Salary": job.salary,
            "Apply Link": job.apply_link,
            "Source": job.source,
            "Date Found": job.date_found,
            "Match Score": job.match_score,
            "Status": "New",
            "First Seen": today,
            "Last Seen": today

        }


        df = pd.concat(
            [
                df,
                pd.DataFrame([new_row])
            ],
            ignore_index=True
        )


        df.to_excel(
            self.file_path,
            index=False
        )


        print(
            "New job added:",
            job.company,
            job.job_title
        )