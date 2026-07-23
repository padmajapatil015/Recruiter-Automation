from app.database.excel_manager import ExcelManager

from app.sources.sample_source import SampleSource


class RecruiterService:

    def __init__(self):

        self.database = ExcelManager()

        self.source = SampleSource()


    def run(self):

        recruiters = self.source.fetch()

        for recruiter in recruiters:

            result = self.database.add_recruiter(recruiter)

            print(result)
