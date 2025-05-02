class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CanteenMixin:
    def pay_canteen(self):
        print("paying for canteen")


class Teacher(User, CanteenMixin):
    def take_attandence(self):
        print("taking attandence...")
    
    def put_marks(self):
        print("puting marks...")


class Student(User, CanteenMixin):
    is_canteen_allowed = True

    def __init__(self, name, age, dept, is_free_enrl):
        super().__init__(name, age)
        self.dept = dept
        self.is_free_enrl = is_free_enrl
    
    def move_to_next_year(self):
        print("moving to next year...")

    def graduate_class(self):
        print("graduate the class...")

    def __repr__(self):
        return f"Student: {self.name} (dept: {self.dept})"
    
