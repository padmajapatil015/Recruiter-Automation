class DuplicateChecker:

    @staticmethod

    def is_duplicate(df, recruiter):

        return recruiter.email in df["Email"].values
