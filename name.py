# Class Name
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        
        if not self.first_name or not self.last_name:
            raise ValueError("First and last names cannot be empty")
        