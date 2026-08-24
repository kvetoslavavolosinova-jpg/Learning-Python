# 14 - Git & Version Control

## 1. What is Git and why is it crucial?
- **Git** is a distributed version control system (VCS) that tracks changes in source code during software development.
- It allows multiple developers to work on the same project simultaneously without overwriting each other's work.
- It acts like a "time machine" for code, letting you restore previous states if something breaks.

## 2. The Three Git Areas
- **Working Directory**: The actual files on your computer that you are currently editing.
- **Staging Area (Index)**: A preparation area where Git tracks which changes will be included in the next commit.
- **Local Repository (HEAD)**: The local database on your machine containing all saved commits.
- **Remote Repository**: The online host (like GitHub) where your code is shared with others.

## 3. Essential Git Commands
- `git init`: Initializes a brand new local Git repository.
- `git status`: Shows which files are modified, untracked, or staged.
- `git add <file>` (or `git add .`): Moves changes from the Working Directory to the Staging Area.
- `git commit -m "message"`: Saves your staged changes as a permanent snapshot in your local history.
- `git push origin <branch>`: Uploads local commits to the remote repository on GitHub.
- `git pull`: Fetches and merges changes from the remote repository to your local computer.
- `git log`: Displays the history of all commits.
