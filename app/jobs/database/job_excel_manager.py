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

            df.to_excel(self.file_path, index=False)



    def add_job(self, job):

        self.create_file()


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


        df = pd.read_excel(self.file_path)


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