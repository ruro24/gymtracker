from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
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
    target_muscle = Column("target_muscle", String)
    
    def __init__(self,ex_id, ex_name, target_muscle):
        self.ex_id = ex_id
        self.ex_name = ex_name
        self.target_muscle=target_muscle
    
    def __repr__(self):
        return f"{self.ex_id} - {self.ex_name} - {self.target_muscle}"
  
class WorkoutExercise(Base):
    __tablename__ = "workout_exercise"
    date = Column("date", DateTime)
    workout = Column(Integer,ForeignKey("workouts.workout_id"),primary_key=True)
    exercise = Column(Integer,ForeignKey("exercises.ex_id"),primary_key=True)
    s1r = Column("set1_rep", Integer)
    s1w = Column("set1_wgt_ kg", Integer)
    s2r = Column("set2_rep", Integer)
    s2w = Column("set2_wgt_ kg", Integer)
    s3r = Column("set3_rep", Integer)
    s3w = Column("set3_wgt_kg", Integer)
    
    def __init__(self, workout, exercise, date, s1r,s1w,s2r,s2w,s3r,s3w):
         
        
        self.workout= workout
        self.exercise = exercise
        self.date  = date 
        self.s1r = s1r
        self.s1w = s1w
        self.s2r = s2r
        self.s2w = s2w
        self.s3r = s3r
        self.s3w = s3w
    
    def __repr__(self):
        return f"{self.date} - {self.workout} - {self.exercise}"
  
relationship(Exercise, secondary=WorkoutExercise, backref='workout_instances')
 
engine = create_engine("sqlite:///mydb.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

#def create_workout(id, name, description, crn_date)

# exercise = Exercise(6,"RDL","")
# session.add(exercise)
# workout = Workout(1,"Core","no weight core exercise",datetime.now())
# workout2 = Workout(2,"Legs","no weight core exercise",datetime.now())
# workout3 = Workout(3,"Full-body","no weight core exercise",datetime.now())
# session.add(workout)
# session.add(workout2)
# session.add(workout3)

# log2 = Log(5,datetime.now(),1,2,10,5,10,5,10,5)
# session.add(log2)
# session.commit()

# results = session.query(Log).all()#filter(Workout.target_muscle.like ("no%")).all()

# print(results)
# l_results = session.query(Log,Workout).filter(Log.workout == Workout.workout_id).filter(Workout).all()
# print(l_results)