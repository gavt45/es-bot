from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import logging

import locales
from config import Config
from util import Singleton

Base = declarative_base()


class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True)
    first_interaction = Column(DateTime, default=func.now())
    name = Column(String)
    last_name = Column(String)

    sex = Column(String)

    test_result = relationship("TestResult", back_populates="candidate")

    def __str__(self):
        return f"Candidate(id={self.id} first_interaction={self.first_interaction} name={self.name})"


class TestResult(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    candidate = relationship("Candidate", back_populates="test_result")

    answers = relationship("QuestionAnswer", back_populates="user", cascade="all, delete-orphan")


class QuestionAnswer(Base):
    __tablename__ = "test_answers"
    id = Column(Integer, primary_key=True)

    test_result_id = Column(Integer, ForeignKey("test_results.id"), nullable=False)
    user = relationship("TestResult", back_populates="answers")

    question = Column(Integer)
    answer = Column(String)


class DB(metaclass=Singleton):
    def __init__(self):
        self._engine = create_engine(f'postgresql+psycopg2://{Config.PG_USER}:{Config.PG_PASS}@{Config.PG_ADDR}/db')
        self._Session = sessionmaker()
        self._Session.configure(bind=self._engine)
        self._session = self._Session()
        Base.metadata.create_all(self._engine)
        logging.debug("Db connection succeeded!")

    def get_user(self, user_id: int) -> Candidate:
        return self._session.query(Candidate).filter(Candidate.id == user_id).first()

    def set_name(self, user_id: int, name: str):
        self._session.query(Candidate).filter(Candidate.id == user_id).update({Candidate.name: name})
        self._session.commit()

    def update_test_result(self, user_id: int, question: int, answer: str):
        user = self._session.query(Candidate).filter(Candidate.id == user_id).first()
        user.test_result[0].answers.append(QuestionAnswer(question=question, answer=answer))
        self._session.commit()

    def add_candidate(self, candidate: Candidate):
        tres = TestResult(answers=[])
        candidate.test_result = [tres]
        self._session.add(candidate)
        self._session.commit()
