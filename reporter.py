import subprocess

def run(command):
    return subprocess.check_output(command, shell=True).decode().strip()

commit_count = run("git rev-list --count HEAD")
last_commit_date = run("git log -1 --format=%cd")
changed_files = run("git diff-tree --no-commit-id --name-only -r HEAD")
branch_name = run("git rev-parse --abbrev-ref HEAD")

report = f"""
GitHub Repository Activity Report
--------------------------------
Commits Count: {commit_count}
Last Commit Date: {last_commit_date}
Current Branch: {branch_name}

Changed Files in Last Commit:
{changed_files}
"""

print(report)