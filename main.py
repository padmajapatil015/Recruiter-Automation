from app.sources.sample_source import SampleSource


def main():

    source = SampleSource()

    recruiters = source.fetch()

    print("\nToday's Recruiters\n")

    for recruiter in recruiters:

        print("-" * 40)
        print(f"Agency       : {recruiter.agency}")
        print(f"Email        : {recruiter.email}")
        print(f"Phone        : {recruiter.phone}")
        print(f"Website      : {recruiter.website}")
        print(f"Location     : {recruiter.city}")
        print(f"Specialization : {recruiter.specialization}")


if __name__ == "__main__":
    main()
