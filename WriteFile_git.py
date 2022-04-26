# g = Github("SumukhaS291299", "sumukhaisgood1234")
# GITHUB_REPO = "FinalSemProj"

import base64

import requests
from github import Github
from github import InputGitTreeElement

user = "SumukhaS291299"
password = "sumukhaisgood1234"
token="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"
g = Github(user,password)

user = g.get_user() # get current user
repo = g.get_repo('SumukhaS291299/FinalSemProj') # owner/repo
# user.creat_fork(repo)

login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(user,token))

contents = repo.get_contents("")

repo.create_file("myfile.csv","This s auto uploaded file","A,B,C,D","origin",)
