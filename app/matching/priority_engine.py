class PriorityEngine:


    def calculate_priority(self, job):

        score = job.match_score


        if (
            score >= 85
            and job.location.lower() == "pune"
            and job.work_mode in ["Hybrid", "Remote"]
        ):
            return "HIGH"


        elif score >= 70:
            return "MEDIUM"


        else:
            return "LOW"