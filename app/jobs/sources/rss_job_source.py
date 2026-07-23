import feedparser
from app.jobs.models.job import Job


class RSSJobSource:


    def __init__(self):

        self.feeds = [
            "https://stackoverflow.com/jobs/feed"
        ]


    def fetch_jobs(self):

        jobs = []


        for feed_url in self.feeds:

            print(
                "Reading RSS:",
                feed_url
            )


            feed = feedparser.parse(
                feed_url
            )


            for item in feed.entries:


                title = item.get(
                    "title",
                    ""
                )


                description = item.get(
                    "summary",
                    ""
                )


                text = (
                    title +
                    " " +
                    description
                ).lower()



                keywords = [
                    "qa",
                    "automation",
                    "selenium",
                    "testing",
                    "sdet"
                ]


                if any(
                    keyword in text
                    for keyword in keywords
                ):


                    job = Job()

                    job.company = item.get(
                        "author",
                        "Unknown"
                    )

                    job.job_title = title

                    job.location = "Not Mentioned"

                    job.experience = "Not Mentioned"

                    job.work_mode = "Not Mentioned"

                    job.skills = (
                        "Automation Testing, "
                        "Selenium, Python"
                    )

                    job.apply_link = item.get(
                        "link",
                        ""
                    )

                    job.source = "RSS"

                    job.date_found = "Today"


                    jobs.append(job)


                    print(
                        "Found RSS job:",
                        title
                    )


        return jobs