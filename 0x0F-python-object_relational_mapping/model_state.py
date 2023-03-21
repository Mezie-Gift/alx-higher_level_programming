#!/usr/bin/python3
"""Module defines a `state` class"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
