from git import Repo

repo = Repo('.')

diff = repo.git.diff('initial_build', 'git_build')

print(diff)