import sqlalchemy.orm
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///block.db')


Base = sqlalchemy.orm.declarative_base()



                                                #БАЗЫ ДАННЫХ:
class SteamBank(Base):
    __tablename__ = "sword"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)

    def __repr__(self):
        return f"<Sword(id={self.id}, name='{self.name}', material='{self.material}', damage={self.damage})>"



Base.metadata.create_all(engine)


SessionSteam = sessionmaker(bind=engine)
session_steam = SessionSteam()



user1 = SteamBank(
    name=f'vvpresense',
    balance=100)


user2 = SteamBank(
    name=f'pitfighter',
    balance=2000)


user3 = SteamBank(
    name=f'poopseek',
    balance=0)


session_steam.add_all([user1,user2,user3])



#первый коммит