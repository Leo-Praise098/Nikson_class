Working files -Files that hold written code

Staging - The waiting environment to prepare untracked files for tracking for a commit (git Add, git Add .)

Repository - A location storage for each version of the written codes, commits are used to initiate such record keeping. A commit is an entry in the log.



Commands for Git

* git status
* git config --global user.email praisewodu8@gmail.com  =>  For setting the email address
* git config --global user.name  "Praise Wodu" => For setting the name
* git config --global
* cd path
* mkdir folder\_name
* git init
* git add filename
* git rm --cached filename
* git add .
* create .gitignore text file
* git restore --staged filename
* git commit -a -m "message"
* git rm "name \& ext of file"
* git restore "filename"



















1\. Git configuration

Command	Use

* git config --global user.email "email"	Set your Git email
* git config --global user.name "Name"	Set your Git username/name
* git config --global	View global configuration options
* git config --list	Display Git configuration
* git config --global --list	Display global Git configuration
* git config --get user.name	Show your configured name
* git config --get user.email	Show your configured email





2\. Working with folders

These aren't Git commands, but you'll use them frequently with Git:

Command	Use

* cd path	Move into a directory
* cd ..	Move up one directory
* cd /	Go to the root directory
* mkdir folder\_name	Create a folder
* dir	List files/folders in Windows CMD
* ls	List files/folders in Git Bash
* pwd	Show your current directory





3\. Creating and starting a repository

Command	Use

* git init	Create a new Git repository
* git clone URL	Download/clone an existing repository
* git clone URL folder\_name	Clone a repository into a specific folder
* git remote -v	Show connected remote repositories
* git remote add origin URL	Connect your local repository to a remote repository

Example:

git clone https://github.com/username/project.git





4\. Checking the repository

Command	Use

* git status	Show the current state of your repository
* git log	Show commit history
* git log --oneline	Show a shorter commit history
* git log --oneline --graph	Show commits as a graphical tree
* git diff	Show changes that haven't been staged
* git diff --staged	Show staged changes
* git show	Show details of a commit

For beginners, these three are particularly important:

git status

git diff

git log --oneline





5\. Adding and removing files

Command	Use

* git add filename	Stage a specific file
* git add .	Stage all changes in the current directory
* git restore --staged filename	Remove a file from staging
* git rm filename	Delete a file and stage the deletion
* git rm --cached filename	Stop tracking a file but keep it on your computer
* git restore filename	Discard changes to a file and restore its last committed version

Example:

git add main.py

Then:

git restore --staged main.py

means "I changed my mind; don't include main.py in the next commit."





6\. .gitignore

&#x09;Create a file called:

&#x09;	.gitignore

&#x09;It tells Git which files/folders not to track.

&#x09;For example:

&#x09;	\_\_pycache\_\_/

&#x09;	\*.pyc

&#x09;	.env

&#x09;	node\_modules/

&#x09;Then check:

&#x09;	git status

&#x09;Git should ignore those files.





7\. Commits

Command	Use

* git commit -m "message"	Create a commit from staged changes
* git commit -a -m "message"	Commit modified/deleted tracked files without manually staging them
* git commit --amend	Modify the most recent commit
* git commit --amend -m "new message"	Change the most recent commit's message
* 





The normal workflow is:

&#x09;	git add .

&#x09;	git commit -m "Add login system"

&#x09;Think of a commit as a saved checkpoint in your project.





8\. Branches

Branches are extremely important.

Command	Use

* git branch	List local branches
* git branch branch\_name	Create a new branch
* git checkout branch\_name	Switch to a branch
* git checkout -b branch\_name	Create and switch to a branch
* git switch branch\_name	Switch branches
* git switch -c branch\_name	Create and switch to a branch
* git branch -d branch\_name	Delete a branch
* git branch -D branch\_name	Force-delete a branch
* git branch -a	Show local and remote branches

Example:

&#x09;	git checkout -b login-feature

&#x09;This creates:

&#x09;	login-feature

&#x09;and immediately switches to it.





9\. Merging branches

&#x09;Suppose you have:

&#x09;	main

&#x09;	login-feature

&#x09;and you've finished your work on login-feature.

&#x09;First switch to main:

&#x09;	git checkout main

&#x09;Then merge:

&#x09;	git merge login-feature



Command	Use

* git merge branch\_name	Merge another branch into the current branch
* git merge --abort	Cancel a merge that has conflicts

Example:

git checkout main

git merge login-feature





10\. Working with GitHub / remote repositories

These commands are essential when using GitHub.

Command	Use

* git remote -v	Show remote repositories
* git remote add origin URL	Add a remote repository
* git remote remove origin	Remove a remote
* git fetch	Download remote changes without applying them
* git pull	Download and integrate remote changes
* git push	Upload your commits
* git push origin main	Push the main branch
* git push -u origin main	Push and set origin/main as the upstream
* git push -u origin branch\_name	Push a new branch to GitHub
* git push --all	Push all local branches



For example, after creating a branch:

&#x09;	git checkout -b login-feature

&#x09;You can upload it to GitHub with:

&#x09;	git push -u origin login-feature

&#x09;After that, usually:

&#x09;	git push

&#x09;is enough.





11\. Getting changes from GitHub

There are three commands you should understand:

&#x09;	git fetch

&#x09;	git fetch

Downloads information about changes from GitHub but doesn't merge them into your current branch.

&#x09;git pull

&#x09;git pull

Basically gets remote changes and integrates them into your current branch.

&#x09;	git clone

&#x09;	git clone URL

Used when you don't have the repository on your computer yet.





12\. Undoing changes

Command	Use

* git restore filename	Discard unstaged changes
* git restore --staged filename	Unstage a file
* git reset HEAD filename	Unstage a file
* git reset --soft HEAD\~1	Undo the last commit but keep changes staged
* git reset HEAD\~1	Undo the last commit and unstage changes
* git reset --hard HEAD\~1	Undo the last commit and discard its changes





⚠️ Be careful with:

&#x09;	git reset --hard

It can permanently discard changes.





13\. Temporarily saving unfinished work

&#x09;git stash is useful when you're working on something but need to switch branches.

Command	Use

* git stash	Temporarily save uncommitted changes
* git stash list	Show saved stashes
* git stash pop	Restore the most recent stash and remove it from stash
* git stash apply	Restore a stash without removing it
* git stash drop	Delete a stash



Example:

&#x09;git stash

&#x09;git checkout main

Later:

&#x09;git stash pop





14\. Remote branches

Command	Use

* git branch -r	Show remote branches
* git branch -a	Show local + remote branches
* git checkout -b branch origin/branch	Create a local branch from a remote branch
* git fetch origin	Get updates from origin





15\. Useful cleanup commands

Command	Use

* git clean -n	Show untracked files that could be removed
* git clean -f	Remove untracked files
* git clean -fd	Remove untracked files and directories





⚠️ Be careful with git clean; it can delete files that Git isn't tracking.

⭐ The commands I'd learn first

Since you're learning Git, don't try to memorize everything at once. Start with this core set:

&#x09;	git config --global user.name "Your Name"

&#x09;	git config --global user.email "your@email.com"



&#x09;	git init

&#x09;	git clone URL



&#x09;	git status

&#x09;	git add filename

&#x09;	git add .

&#x09;	git restore --staged filename



&#x09;	git commit -m "message"

&#x09;	git log --oneline



&#x09;	git branch

&#x09;	git checkout -b branch-name

&#x09;	git checkout branch-name

&#x09;	git merge branch-name



&#x09;	git remote -v

&#x09;	git remote add origin URL



&#x09;	git push

&#x09;	git pull

&#x09;	git fetch



&#x09;	git stash

&#x09;	git stash pop





The basic Git workflow

You'll use this pattern very often:

&#x20;                   Make changes

&#x20;                        ↓

&#x20;                   git status

&#x20;                        ↓

&#x20;                    git add .

&#x20;                        ↓

&#x20;               git commit -m "..."

&#x20;                        ↓

&#x20;                 git push

&#x20;                        ↓

&#x20;                    GitHub

And when working with branches:

main

&#x20;│

&#x20;├── checkout -b feature

&#x20;│

&#x20;│    Make changes

&#x20;│    git add .

&#x20;│    git commit

&#x20;│    git push

&#x20;│

&#x20;└── merge feature → main

One important correction to your list: git commit -a -m "message" does not stage new/untracked files. It only automatically stages modifications and deletions of files Git is already tracking. For new files, use git add first.





