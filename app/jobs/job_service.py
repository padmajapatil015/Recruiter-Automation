from app.jobs.sources.job_aggregator import JobAggregator
from app.jobs.database.job_excel_manager import JobExcelManager
from app.matching.matcher import ResumeMatcher


class JobService:

    def __init__(self):

        self.aggregator = JobAggregator()
        self.excel = JobExcelManager()
        self.matcher = ResumeMatcher()


    def collect_jobs(self):

        jobs = self.aggregator.collect_all_jobs()


        for job in jobs:

            job.match_score = self.matcher.calculate_score(job)

            self.excel.add_job(job)


        print(
            "Jobs collected, matched and saved successfully"
        )