# Wiki
## subtitle
During BeCode training.
I did this first project to be introduced to several notions :

- How to create a repository on Github and synchronize it with Git
- How to import packages
- How to create variable and write some functions in python
- How to create a simple API
- How to create a create a Json file 
- How to create caching
- How to do requests - https://github.com/psf/requests


Steps to create a new project:
- Fork a project on GitHub
- Clone it to my Git “Git clone : 
- Then I pull to transfer from GitHub to git
- pip install -r requirements.txt
- I create a new environment in the folder of the project virtualenv -venv 
- activate the source : Source virtualenv/bin/activate
- I installed (the later load in the code part) (librairies) requests in the new environment & dependencies python “-m pip install” requests 
- When I use Virtual studio -  open it from cd and in the new environment folder and type “code .”.
Create an error log-in file
- In VCS create a test.ipynb to test my code

Create API : 
- Define root and extension URL
- Request.get(..URL, cookie (is some)
- variable.status_code / text /.json()
- Cookie : cookie = req_cookie.cookies["user_cookie"]
    - Result , cookies={"user_cookie":cookie})

Steps before to close project :
- “Deactivate” environment : 
- Write README
- pip3 freeze > requirements.txt