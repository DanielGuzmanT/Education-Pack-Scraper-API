from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ToolEntity(Base):
    __tablename__ = "tool"

    id          = Column(Integer, primary_key=True)
    business_id = Column(Integer)

    business = relationship('BusinessEntity', uselist=False, back_populates='tool')
    benefits = relationship('BenefitEntity')
    tags     = relationship('TagEntity')


class BusinessEntity(Base):
    __tablename__ = "business"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100))
    description = Column(String(250))
    webpage     = Column(String(100))

    logo = relationship('LogoEntity', uselist=False, back_populates='business')


class LogoEntity(Base):
    __tablename__ = "logo"

    id          = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey('business.id'))
    url         = Column(String(500))


class BenefitEntity(Base):
    __tablename__ = "benefit"

    id          = Column(Integer, primary_key=True)
    description = Column(String(500))
    tool_id     = Column(Integer, ForeignKey('tool.id'))


class TagEntity(Base):
    __tablename__ = "tag"

    id          = Column(Integer, primary_key=True)
    name        = Column(String( 50))
    description = Column(String(250))
    business_id = Column(Integer, ForeignKey('tool.id'))
