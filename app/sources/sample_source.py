from app.models.recruiter import Recruiter


class SampleSource:

    def fetch(self):

        return [

            Recruiter(

                agency="Sample Recruitment",

                recruiter_name="Rahul Sharma",

                email="rahul@example.com",

                phone="+91xxxxxxxxxx",

                linkedin="https://linkedin.com/in/sample",

                website="https://example.com",

                city="Pune",

                specialization="Automation Testing",

                current_opening="QA Automation Engineer",

                hiring_location="Pune",

                source="Sample Source",

                verified=True

            )

        ]
