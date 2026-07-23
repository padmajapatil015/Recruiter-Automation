from app.jobs.sources.job_aggregator import JobAggregator
from app.jobs.database.job_excel_manager import JobExcelManager
from app.matching.matcher import ResumeMatcher
from app.matching.priority_engine import PriorityEngine


class JobService:

    def __init__(self):

        self.aggregator = JobAggregator()

        self.excel = JobExcelManager()

        self.matcher = ResumeMatcher()

        self.priority = PriorityEngine()



    def collect_jobs(self):

        jobs = self.aggregator.collect_all_jobs()


        for job in jobs:

            # Calculate resume match score
            job.match_score = self.matcher.calculate_score(job)


            # Calculate priority
            job.priority = self.priority.calculate_priority(job)


            # Save job
            self.excel.add_job(job)



        print(
            "Jobs collected, matched, prioritized and saved successfully"
        )