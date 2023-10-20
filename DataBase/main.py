from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def main():
    engine = create_engine('sqlite:///DataBase/database.sqlite')

    Session = sessionmaker(bind=engine)
    with Session() as session:
        Base = declarative_base()

        class Subject(Base):
            __tablename__ = 'subjects'

            id_subject = Column(Integer, primary_key=True)
            subject_name = Column(String)
            subject_description = Column(String)
            hours = Column(Integer)
            semester_number = Column(Integer)

        Base.metadata.create_all(engine)

        subjects_data = [
            {"subject_name": "Math", "subject_description": "Mathematics course", "hours": 60, "semester_number": 1},
            {"subject_name": "Physics", "subject_description": "Physics course", "hours": 50, "semester_number": 1},
            {"subject_name": "Chemistry", "subject_description": "Chemistry course", "hours": 45, "semester_number": 2},
            {"subject_name": "History", "subject_description": "History course", "hours": 40, "semester_number": 2},
            {"subject_name": "English", "subject_description": "English language course", "hours": 60, "semester_number": 3},
            {"subject_name": "Biology", "subject_description": "Biology course", "hours": 45, "semester_number": 3},
            {"subject_name": "Computer Science", "subject_description": "Computer Science course", "hours": 55, "semester_number": 4},
            {"subject_name": "Art", "subject_description": "Art course", "hours": 30, "semester_number": 4},
            {"subject_name": "Geography", "subject_description": "Geography course", "hours": 50, "semester_number": 2},
            {"subject_name": "Music", "subject_description": "Music course", "hours": 35, "semester_number": 3},
            {"subject_name": "Physical Education", "subject_description": "Physical Education course", "hours": 40, "semester_number": 1},
            {"subject_name": "Chemical Engineering", "subject_description": "Chemical Engineering course", "hours": 60, "semester_number": 6},
            {"subject_name": "Psychology", "subject_description": "Psychology course", "hours": 45, "semester_number": 5},
            {"subject_name": "Sociology", "subject_description": "Sociology course", "hours": 50, "semester_number": 4},
            {"subject_name": "Philosophy", "subject_description": "Philosophy course", "hours": 40, "semester_number": 4}
        ]


        for data in subjects_data:
            subject = Subject(**data)
            session.add(subject)

        session.commit()

        results = session.query(Subject.subject_name, Subject.semester_number).all()

        for result in results:
            print(f"Subject Name: {result.subject_name}, Semester Number: {result.semester_number}")


if __name__ == '__main__':
    main()