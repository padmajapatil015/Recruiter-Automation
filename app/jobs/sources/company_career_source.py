import json
import requests
from bs4 import BeautifulSoup


class CompanyCareerSource:


    def __init__(self):

        with open("data/companies/company_list.json", "r") as f:
            self.companies = json.load(f)



    def fetch_jobs(self):

        jobs = []


        for company in self.companies:

            print(
                f"Checking careers page: {company['company']}"
            )


            try:

                response = requests.get(
                    company["career_url"],
                    timeout=10,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                )


                if response.status_code == 200:

                    soup = BeautifulSoup(
                        response.text,
                        "html.parser"
                    )


                    text = soup.get_text(
                        " ",
                        strip=True
                    )


                    if "automation" in text.lower():

                        print(
                            f"Possible QA opening found: {company['company']}"
                        )


            except Exception as e:

                print(
                    f"Error checking {company['company']}: {e}"
                )


        return jobs