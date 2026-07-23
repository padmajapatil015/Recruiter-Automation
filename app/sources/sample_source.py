from app.models.recruiter import Recruiter


class SampleSource:

    def fetch(self):

        recruiters = [

            Recruiter(
                agency="Sample Recruitment",
                email="sample@example.com",
                phone="+91xxxxxxxxxx",
                website="https://example.com",
                city="Pune",
                specialization="Automation Testing",
                hiring_location="Pune",
                verified=True
            )

        ]

        return recruiters