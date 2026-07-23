from app.database.excel_manager import ExcelManager
from app.sources.file_importer import FileImporter


class RecruiterService:

    def __init__(self):
        self.database = ExcelManager()
        self.source = FileImporter()

    def run(self):

        recruiters = self.source.fetch()

        print(f"\nFound {len(recruiters)} recruiter(s).\n")

        for recruiter in recruiters:

            result = self.database.add_recruiter(recruiter)

            print(result)