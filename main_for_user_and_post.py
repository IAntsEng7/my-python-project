# import user
from user import User
from post import Post

# Usually we have a .py file to manage about users.
# Create Object
# import user
# tom = user.User("tt@tt.com", "Tom", "t2t0", "Developer")
# devin = user.User("dd@dd.com", "Devin", "d4d4", "Manager")
# from user import User
tom = User("tt@tt.com", "Tom", "t2t0", "Developer")
devin = User("dd@dd.com", "Devin", "d4d4", "Manager")
new_post_1 = Post("on a secret mission today", tom.name)
new_post_2 = Post("Nothing to do today.", devin.name)

# Call function (use method)
tom.get_user_info()
# User Tom currently works as Developer.You can connect them at tt@tt.com
devin.get_user_info()
# User Devin currently works as Manager.You can connect them at dd@dd.com

tom.change_job_title("HR")
tom.get_user_info()
# User Tom currently works as HR.You can connect them at tt@tt.com

new_post_1.get_post_info()
# Post: on a secret mission today.
#                           -- Written by Tom
new_post_2.get_post_info()
# Post: Nothing to do today.
#                           -- Written by Devin
