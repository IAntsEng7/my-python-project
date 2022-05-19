class User:
    def __init__(self, email, name, password, current_job_title):
        # self is a reference to the current instance of the class.

        # 1. Object will create with initial values
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # 2. Call functions on that object to change its password
    #    ex. tom.change_password("2t0t")
    # Functions that belong to an object are called methods.
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(
            f"User {self.name} currently works as {self.current_job_title}."
            f"You can connect them at {self.email}")

# Basically it can create object here,
# but what if it needs to create hundreds or thousands user info?

# # Create Object
# tom = User("tt@tt.com", "Tom", "t2t0", "Developer")
# devin = User("dd@dd.com", "Devin", "d4d4", "Manager")
#
# # Call function (use method)
# tom.get_user_info()
# # User Tom currently works as Developer.You can connect them at tt@tt.com
# devin.get_user_info()
# # User Devin currently works as Manager.You can connect them at dd@dd.com
#
# tom.change_job_title("HR")
# tom.get_user_info()
# # User Tom currently works as HR.You can connect them at tt@tt.com
