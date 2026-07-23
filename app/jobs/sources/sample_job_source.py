from app.jobs.models.job import Job


class SampleJobSource:


    def fetch_jobs(self):

        jobs = []


        job1 = Job()
        job1.company = "Infosys"
        job1.job_title = "QA Automation Engineer"
        job1.location = "Pune"
        job1.experience = "3+ Years"
        job1.work_mode = "Hybrid"
        job1.skills = "Selenium, Python, Pytest, REST API"
        job1.salary = "Not Mentioned"
        job1.apply_link = ""
        job1.source = "Sample"
        job1.date_found = "Today"

        jobs.append(job1)



        job2 = Job()
        job2.company = "Capgemini"
        job2.job_title = "SDET"
        job2.location = "Pune"
        job2.experience = "3 Years"
        job2.work_mode = "Remote"
        job2.skills = "Selenium, Python, SQL, API Testing"
        job2.salary = "Not Mentioned"
        job2.apply_link = ""
        job2.source = "Sample"
        job2.date_found = "Today"

        jobs.append(job2)


        return jobs