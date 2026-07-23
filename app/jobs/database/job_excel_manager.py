import os
import pandas as pd


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
            "Match Score"
        ]


    def create_file(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):

            df = pd.DataFrame(columns=self.columns)

            df.to_excel(
                self.file_path,
                index=False
            )


    def is_duplicate(self, job):

        df = pd.read_excel(
            self.file_path
        )


        if df.empty:
            return False


        duplicate = df[
            (df["Company"] == job.company) &
            (df["Job Title"] == job.job_title)
        ]


        return not duplicate.empty



    def add_job(self, job):

        self.create_file()


        if self.is_duplicate(job):

            print(
                "Duplicate job skipped:",
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
            "Match Score": job.match_score

        }


        df = pd.read_excel(
            self.file_path
        )


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
            "Job added:",
            job.company,
            job.job_title
        )