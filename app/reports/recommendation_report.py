import os
import pandas as pd


class RecommendationReport:


    def __init__(self):

        self.input_file = "data/Today_Jobs.xlsx"

        self.output_folder = "data/reports"

        self.output_file = (
            "data/reports/Daily_Top_Jobs.xlsx"
        )


    def generate(self):

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )


        df = pd.read_excel(
            self.input_file
        )


        if df.empty:
            print("No jobs available")
            return


        # Sort best opportunities first

        df = df.sort_values(
            by=[
                "Priority",
                "Match Score"
            ],
            ascending=[
                True,
                False
            ]
        )


        top_jobs = df.head(10)


        top_jobs.to_excel(
            self.output_file,
            index=False
        )


        with open(
            "data/reports/Job_Summary.txt",
            "w"
        ) as file:

            file.write(
                "Daily Job Recommendations\n"
            )

            file.write(
                "=========================\n\n"
            )


            for index, row in top_jobs.iterrows():

                file.write(
                    f"{row['Company']} | "
                    f"{row['Job Title']} | "
                    f"{row['Match Score']}% | "
                    f"{row['Priority']}\n"
                )


        print(
            "Recommendation report generated successfully"
        )