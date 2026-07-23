from app.services.recruiter_service import RecruiterService
from app.jobs.job_service import JobService


def main():

    print("Starting Recruiter Automation System...")


    # Recruiter Database
    recruiter_service = RecruiterService()
    recruiter_service.run()


    # Job Finder + Resume Matching
    job_service = JobService()
    job_service.collect_jobs()


    print("Automation completed successfully!")


if __name__ == "__main__":

    main()