class College:
    college_name = "ABC College"

    @classmethod
    def change_name(cls, name):
        cls.college_name = name

print("Old Name:", College.college_name)

new_name = input("Enter new college name: ")
College.change_name(new_name)

print("Updated Name:", College.college_name)
