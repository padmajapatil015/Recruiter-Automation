import json


class ResumeMatcher:

    def __init__(self):

        with open("data/config.json", "r") as f:
            self.config = json.load(f)

        self.profile = self.config["profile"]


    def calculate_score(self, job):

        score = 0


        # Skills (50%)
        profile_skills = [
            skill.lower()
            for skill in self.config.get("skills", [])
        ]

        job_skills = [
            skill.strip().lower()
            for skill in job.skills.split(",")
            if skill.strip()
        ]


        matched = len(set(profile_skills) & set(job_skills))


        if job_skills:
            score += (matched / len(job_skills)) * 50



        # Location (15%)
        if job.location.lower() == self.profile["location"].lower():
            score += 15



        # Work Mode (15%)
        if job.work_mode in self.profile["preferred_work_mode"]:
            score += 15



        # Experience (20%)
        score += 20


        return round(score, 1)