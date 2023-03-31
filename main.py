from sqlalchemy import Column
from sqlalchemy import Float, Date, String, Time, ARRAY
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Record(Base):
    __tablename__ = "records"
    date = Column(Date, nullable = False)
    name = Column(String, nullable = False)
    time = Column(Time, nullable = False)
    tags = Column(ARRAY, nullable = False)
    price = Column(Float, nullable = False)


class NotHandledCase(RuntimeError): pass

while True:
    match input("enter your action. `help` for help."):
        case "sum":
            pass            
        case "avg":
            pass
        case "min":
            pass
        case "max":
            pass
        case _:
            pass


if __name__ == "__main__":
    pass