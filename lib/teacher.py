#!/usr/bin/env python

from user import User

from random import randint

class Teacher(User):
    
    
    def __init__(self,first_name,last_name,knowledge = ["str is a data type in Python","programming is hard, but it's worth it","JavaScript async web request","Python function call definition","object-oriented teacher instance","programming computers hacking learning terminal","pipenv install pipenv shell", "pytest -x flag to fail fast",]):
        super().__init__(first_name,last_name)
        self.knowledge = knowledge

    def teach(self):
        length = len(self.knowledge)
        return self.knowledge[randint(0,length-1)]
