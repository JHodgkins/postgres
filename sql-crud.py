from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# exercuting the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for the "programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaaker, then point to our engine (the db)
Session = sessionmaker(db)

# open an actual session by calling the session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Creating records on our "Programmers" table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL langusge"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_burners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

steve_jobs = Programmer(
    first_name="Steve",
    last_name="Jobs",
    gender="M",
    nationality="American",
    famous_for="Apple"
)

james_hodgkins = Programmer(
    first_name="James",
    last_name="Hodgkins",
    gender="M",
    nationality="British",
    famous_for="Blind programmer"
)

# Add each instane of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_burners_lee)
session.add(steve_jobs)
session.add(james_hodgkins)

# commit our session to the database
session.commit()

# Query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
