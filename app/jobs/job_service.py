from app.jobs.sources.sample_job_source import SampleJobSource
from app.jobs.database.job_excel_manager import JobExcelManager
from app.matching.matcher import ResumeMatcher


class JobService:

    def __init__(self):

        self.source = SampleJobSource()
        self.excel = JobExcelManager()
        self.matcher = ResumeMatcher()


    def collect_jobs(self):

        jobs = self.source.fetch_jobs()

        for job in jobs:

            # Calculate Resume Match Score
            job.match_score = self.matcher.calculate_score(job)

            # Save job into Excel
            self.excel.add_job(job)


        print("Jobs collected and match scores generated successfully")