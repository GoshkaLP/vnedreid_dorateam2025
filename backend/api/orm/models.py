from sqlalchemy import Boolean, Column, Date, Float, Integer, Text

from api.orm.base import Base


class Vacancies(Base):
    vacancy_date = Column(Date, nullable=True)
    specialization = Column(Text, nullable=True)
    region = Column(Text, nullable=True)
    work_experience = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Text, nullable=True)
    salary_specified = Column(Boolean, default=False, nullable=True)
    salary_amount = Column(Float, nullable=True)
    company = Column(Text, nullable=True)
    vacancy_source = Column(Text, nullable=True)


class Resume(Base):
    vacancy_date = Column(Date, nullable=True)
    specialization = Column(Text, nullable=True)
    region = Column(Text, nullable=True)
    work_experience = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Text, nullable=True)
    salary_specified = Column(Boolean, default=False, nullable=True)
    salary_amount = Column(Float, nullable=True)
    company = Column(Text, nullable=True)
    vacancy_source = Column(Text, nullable=True)


class Radar(Base):
    vacancy_date = Column(Date, nullable=True)
    specialization = Column(Text, nullable=True)
    region = Column(Text, nullable=True)
    work_experience = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Text, nullable=True)
    salary_specified = Column(Boolean, default=False, nullable=True)
    salary_amount = Column(Float, nullable=True)
    company = Column(Text, nullable=True)
    vacancy_source = Column(Text, nullable=True)
    medical_insurance = Column(Boolean, default=False, nullable=True)
    meal = Column(Boolean, default=False, nullable=True)
    gym = Column(Boolean, default=False, nullable=True)
    flexible_schedule = Column(Boolean, default=False, nullable=True)
    training = Column(Boolean, default=False, nullable=True)


# class User(Base):
#     username = Column(Text, nullable=False)
#     password = Column(Text, nullable=False)
#     role_id = Column(UUID, ForeignKey("role.id"), nullable=False)
#
#     role = relationship("Role", back_populates="users", uselist=False)
#     reviews = relationship("Review", back_populates="user", uselist=True)
#
#
# class Role(Base):
#     title = Column(Text, nullable=False)
#
#     users = relationship("User", back_populates="role", uselist=True)
#
#
# class File(Base):
#     path = Column(Text, nullable=False)
#
#
# class Movie(Base):
#     title = Column(Text, nullable=False)
#     description = Column(Text, nullable=False)
#     imdb_rating = Column(NUMERIC, nullable=False)
#     logo_file_id = Column(UUID, ForeignKey("file.id"), nullable=False)
#
#     logo_file = relationship("File", uselist=False)
#     reviews = relationship("Review", back_populates="movie", uselist=True)
#
#
# class Review(Base):
#     user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
#     movie_id = Column(UUID, ForeignKey("movie.id"), nullable=False)
#     content = Column(Text, nullable=False)
#     rating = Column(NUMERIC, nullable=False)
#     status = Column(Text, nullable=False)
#
#     user = relationship("User", back_populates="reviews", uselist=False)
#     movie = relationship("Movie", back_populates="reviews", uselist=False)
