from pony.orm import Database, PrimaryKey, Required, Set, Optional, db_session
from datetime import date

from factory.ponyorm import PonyFactory

# this entities come from pony.orm.example.university1
db = Database()

buffer = memoryview

import unittest

import factory


class Department(db.Entity):
    number = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    place = Optional(str)
    # groups = Set("Group")
    # courses = Set("Course")


# class Group(db.Entity):
#     number = PrimaryKey(int)
#     major = Required(str)
#     dept = Required("Department")
#     students = Set("Student")

# class Course(db.Entity):
#     name = Required(str)
#     semester = Required(int)
#     lect_hours = Required(int)
#     lab_hours = Required(int)
#     credits = Required(int)
#     dept = Required(Department)
#     students = Set("Student")
#     PrimaryKey(name, semester)

# class Student(db.Entity):
#     # _table_ = "public", "Students"  # Schema support
#     id = PrimaryKey(int, auto=True)
#     name = Required(str)
#     dob = Required(date)
#     tel = Optional(str)
#     picture = Optional(buffer, lazy=True)
#     gpa = Required(float, default=0)
#     group = Required(Group)
#     courses = Set(Course)


class FacDepartement(PonyFactory):
    class Meta:
        model = Department

    number = factory.Sequence(lambda n: n)
    # name = factory.Sequence(lambda a: "name%s" % a)
    # name = factory.LazyAttribute(lambda obj: 'name%s' % obj.number)


class PonyORMTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):

    params = dict(provider='sqlite', filename=':memory:', create_db=True)
    db.bind(**params)

    db.generate_mapping(create_tables=True)

    def test_creation_out_session(self):
        dep = FacDepartement.create()
        self.assertEqual('name' + str(dep.number), dep.name)
        self.assertEqual(db.Department[dep.number] is dep)

    @db_session
    def test_creation_out_session(self):
        dep = FacDepartement.create()
        self.assertEqual('name' + str(dep.number), dep.name)
        self.assertIs(db.Department[dep.number], dep)

    @db_session
    def test_creation_out_session(self):
        dep = FacDepartement.create()
        self.assertEqual(dep.place, '')
        dep = FacDepartement.create(place="mokmokomk")
        self.assertEqual(dep.place, 'mokmokomk')
