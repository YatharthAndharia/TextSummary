from git import Repo

# Create a Repo object representing the local Git repository
repo = Repo('.')

# Checkout the branch or commit associated with the pull request
repo.git.checkout('')

# Generate the diff of the changes between the previous and current commits
diff = repo.git.diff('HEAD~1', 'HEAD')

# Print the diff to the console
print(diff)

# Write the diff to a file
with open('diff.txt', 'w') as f:
    f.write(diff)
