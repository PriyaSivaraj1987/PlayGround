import git
from git import Repo
repo = git.Repo()
print(repo)
commit_message = 'added a new file'
repo.git.add('--all')
#repo.index.add(files)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()