class Parent(object):

    def override(self):
        print("PARENTE implicit()")

class Child(Parent):

    def override(self):
        print("CHILD implicit()")

dad = Parent()
son = Child()

dad.override()
son.override()