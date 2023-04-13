import subprocess
from atlassian import Confluence 
import json
#
repo_url = "https://github.com/shluh/data-exploration.git"
get_tags = subprocess.check_output(
    [
        "git",
        "ls-remote",
        "--tags",
        "--refs",
        "--sort=version:refname",
        repo_url,
    ],
    encoding="utf-8",
).splitlines()

current_version = get_tags[-1].rpartition("/")[-1]
previous_version = get_tags[-2].rpartition("/")[-1]


# cmd = f"git log --pretty='- %s' {current_version}...{previous_version}" 
cmd = 'git log --pretty=format:"- %s" `git tag --sort=-committerdate | head -1`...`git tag --sort=-committerdate | head -2`'
changes = subprocess.Popen([cmd,repo_url],stdout=subprocess.PIPE,shell=True,encoding="utf-8",).communicate()[0]
# data e autor
version_notes = f'''
<h1>🎁🎁 Reeelease notes (`{current_version}`)</h1> 
<h2>Changes:</h2>{changes}
<h2>Metadata:</h2>
This version --------- {current_version}
Previous version ----- {previous_version}
'''

print(version_notes)
# git tag -a v1.4 -m "my version 1.4"