from app.jobs.sources.sample_job_source import SampleJobSource
from app.jobs.sources.company_career_source import CompanyCareerSource
from app.jobs.sources.rss_job_source import RSSJobSource


class JobAggregator:


    def __init__(self):

        self.sources = [
            SampleJobSource(),
            CompanyCareerSource(),
            RSSJobSource()
        ]


    def collect_all_jobs(self):

        all_jobs = []


        for source in self.sources:

            print(
                f"Running source: {source.__class__.__name__}"
            )


            jobs = source.fetch_jobs()

            all_jobs.extend(jobs)


        print(
            f"Total jobs collected: {len(all_jobs)}"
        )


        return all_jobs