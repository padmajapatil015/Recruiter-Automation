from app.services.recruiter_service import RecruiterService
from app.jobs.job_service import JobService
from app.reports.recommendation_report import RecommendationReport



def main():

    print(
        "Starting Recruiter Automation System..."
    )


    recruiter_service = RecruiterService()

    recruiter_service.run()


    job_service = JobService()

    job_service.collect_jobs()


    report = RecommendationReport()

    report.generate()


    print(
        "Automation completed successfully!"
    )



if __name__ == "__main__":

    main()