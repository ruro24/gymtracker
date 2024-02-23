from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from datetime import datetime
Base = declarative_base()


class Workout(Base):
    
    __tablename__ = "workouts"
    workout_id  = Column("workout_id", Integer,primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    crn_date = Column("crn_date", DateTime)
    
    def __init__(self, workout_id, name, description, crn_date):
        self.workout_id  = workout_id
        self.name = name
        self.description = description
        self.crn_date = crn_date
    
    def __repr__(self):
        return f"{self.workout_id}:{self.name} - {self.description} - {self.crn_date}"


class Exercise(Base):
    __tablename__ = "exercises"
    ex_id  = Column("ex_id", Integer,primary_key=True)
    ex_name = Column("ex_name", String)
    description = Column("description", String)
    
    def __init__(self,ex_id, ex_name, description):
        self.ex_id = ex_id
        self.ex_name = ex_name
        self.description=description
    
    def __repr__(self):
        return f"{self.ex_id} - {self.ex_name} - {self.description}"
  
class Log(Base):
    __tablename__ = "logs"
    log_id  = Column("log_id", Integer,primary_key=True)
    crn_date = Column("crn_date", DateTime)
    workout = Column(Integer,ForeignKey("Workout.workout_id"))
    exercise = Column(Integer,ForeignKey("Excercise.ex_id"))
    
    def __init__(self,log_id , crn_date , workout, exercise):
        self.log_id  = log_id 
        self.crn_date  = crn_date 
        self.workout= workout
        self.exercise = exercise
        
      
engine = create_engine("sqlite:///mydb.db",echo=True)

    

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

exercise = Exercise(6,"RDL","")
session.add(exercise)
# workout = Workout(1,"Core","no weight core exercise",datetime.now())
# session.add(workout)
# session.commit()
# workout2 = Workout(2,"Legs","no weight core exercise",datetime.now())
# workout3 = Workout(3,"Full-body","no weight core exercise",datetime.now())
# session.add(workout2)
# session.add(workout3)

# session.commit()

results = session.query(Exercise).all()#filter(Workout.description.like ("no%")).all()

print(results)