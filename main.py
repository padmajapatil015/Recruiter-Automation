from app.sources.sample_source import SampleSource
from app.database.excel_manager import ExcelManager


def main():

    source = SampleSource()

    recruiters = source.fetch()


    database = ExcelManager()


    for recruiter in recruiters:

        result = database.add_recruiter(recruiter)

        print(result)


if __name__ == "__main__":
    main()