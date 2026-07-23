from app.models.recruiter import Recruiter


class SampleSource:

    def fetch(self):

        return [

            Recruiter(
                agency="Sample Recruitment",
                recruiter_name="Rahul Sharma",
                designation="Technical Recruiter",
                email="sample@example.com",
                phone="+91xxxxxxxxxx",
                linkedin="https://linkedin.com/in/sample",
                website="https://example.com",
                city="Pune",
                hiring_for="QA Automation Engineer",
                experience_required="2-4 Years",
                work_mode="Hybrid",
                current_opening="Automation Test Engineer",
                job_link="https://example.com/job",
                hiring_location="Pune",
                source="Sample Source",
                verified=True
            )

        ]