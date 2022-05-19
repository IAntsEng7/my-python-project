import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# https://gitlab.com/api/v4
# /users/:user_id/project

n_project = response.json()
print(n_project)

for project in n_project:
    print(f"Project name: {project['name']}\n"
          f"Project Url: {project['web_url']}\n")
