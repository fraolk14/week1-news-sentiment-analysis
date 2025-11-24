🌞 Week 1 — Task 1
Git Workflow, Branching, Pull Requests, and VS Code Integration
This document provides a step-by-step guide to completing Week 1 — Task 1, focusing on version control using Git and GitHub within Visual Studio Code (VS Code).

📌 Task Objective
By the end of this task, you will:

Set up your local repo inside VS Code

Create a new working branch

Commit changes properly

Push your work to GitHub

Pull updates using VS Code

Create a Pull Request (PR)

Merge your branch following best practices

⚙️ Prerequisites
Make sure you have:

Git installed

VS Code installed

GitHub account

Your Week 1 repository already cloned

⭐ Step-by-Step Instructions
STEP 1 — Open Your Project in VS Code
Open VS Code

Click File → Open Folder

Select your project folder (e.g., solar-week1)

⭐ STEP 2 — Open the VS Code Terminal
Go to:

Terminal → New Terminal
This opens a terminal inside your project directory.

⭐ STEP 3 — Check Git Status
Run:

git status
You should see "on branch main" if everything is correct.

⭐ STEP 4 — Create a New Branch for Task 1
git checkout -b week1-task1
This creates and switches you to a new branch.

⭐ STEP 5 — Make Your Changes
Add your scripts, markdown files, notebooks, or folders required for Week 1 Task 1.

All new or modified files will appear in Source Control (Ctrl + Shift + G).

⭐ STEP 6 — Stage Your Changes in VS Code
Two ways:

Option A — VS Code GUI
Go to Source Control Panel

Click the + icon next to each file or "Stage All Changes"

Option B — Command Line
git add .
⭐ STEP 7 — Commit Your Changes
Using VS Code GUI:

Write a commit message

Click ✔ Commit

Using terminal:

git commit -m "feat: completed week 1 task 1 setup"
⭐ STEP 8 — Push Your Branch to GitHub
git push -u origin week1-task1
If VS Code asks “Publish Branch”, click Yes.

⭐ STEP 9 — Pull Changes (Very Important)
Ensure your branch is up to date:

Option A — VS Code GUI
Click the Synchronize Changes icon (bottom-left)

It will automatically pull + push

Option B — Command Line
git pull origin main
If needed:

git pull origin main --rebase
This prevents merge conflicts.

⭐ STEP 10 — Resolve Any Conflicts (If Any)
VS Code will highlight conflicts like this:

<<<<<< HEAD
Your Branch Code
======
Main Branch Code
>>>>>> main
Fix them manually → save → commit.

⭐ STEP 11 — Push Again If You Resolved Conflicts
git push
⭐ STEP 12 — Open PR Using VS Code (Recommended)
VS Code supports GitHub Pull Requests.

Open Command Palette (Ctrl + Shift + P)

Type: GitHub: Create Pull Request

Select:

Base: main

Compare: week1-task1

Add title + description

Click Create Pull Request

⭐ STEP 13 — Open PR from GitHub Website (Alternative)
Go to GitHub repo

Click Pull Requests → New Pull Request

Compare:

base → main

compare → week1-task1

Click Create Pull Request

⭐ STEP 14 — Wait for CI to Pass (If CI is configured)
GitHub Actions will run automatically:

Install dependencies

Validate code

Run tests (if configured)

When CI is green → proceed.

⭐ STEP 15 — Merge the Pull Request (VS Code Version)
Using VS Code
Open Command Palette (Ctrl + Shift + P)

Type: GitHub: Merge Pull Request

Select your PR

Confirm merge

Using GitHub Website
Click Merge Pull Request → Confirm

⭐ STEP 16 — Pull Latest Changes to Local Main
git checkout main
git pull origin main
Now your main branch is up to date.

🎉 Task 1 Is Now Successfully Completed!
You have now demonstrated:

Proper Git workflow

Professional branching model

CI-aware PR process

VS Code Git integration

Clean merge strategy

📄 License & Author
Author: Fraol Kuma
Week 1 – Task 1
Solar Challenge Bootcamp