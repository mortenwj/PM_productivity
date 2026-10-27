# Project setup – GitHub and environment

Get this PM productivity project stored on GitHub and ready for daily use.

---

## 1. GitHub repo

Repository: **https://github.com/mortenwj/pm-productivity**

- Use it to store this folder: morning reports, docs, scripts, and config (no secrets).
- Clone URL: `https://github.com/mortenwj/pm-productivity.git`  
  SSH: `git@github.com:mortenwj/pm-productivity.git`

---

## 2. Connect your current folder to the repo

You already have a git repo here with no commits yet. Do this once:

### Option A: This folder is your only copy (recommended)

```powershell
cd "C:\Users\MortenJensen\.cursor\projects\PM_productivity"

# Add the new GitHub repo as remote (replace if origin already exists)
git remote add origin https://github.com/mortenwj/pm-productivity.git
# If you get "origin already exists", use: git remote set-url origin https://github.com/mortenwj/pm-productivity.git

# First commit (choose what to include)
git add README.md PROJECT_SETUP.md DAILY_WORKFLOW.md toolkit/morning-report/generate_morning_report.py
git add morning_report.md
# Add more files as needed, or: git add .   (then review with git status)
git status
git commit -m "Initial PM productivity command center"

# Push (main branch)
git branch -M main
git push -u origin main
```

### Option B: You want a clean clone elsewhere

```powershell
git clone https://github.com/mortenwj/pm-productivity.git pm-productivity
cd pm-productivity
# Copy over any extra files from your current folder, then commit and push
```

---

## 3. What to commit (and what not to)

**Do commit:**

- `README.md`, `PROJECT_SETUP.md`, `DAILY_WORKFLOW.md`
- `generate_morning_report.py`, other scripts you use
- `morning_report.md` (if you’re fine with it in the repo)
- `QUICKSTART.md`, `config.example.json`
- Other markdown/docs and non-secret config

**Do not commit:**

- `config.json` or any file with real tokens/passwords
- Large binaries or temp files (use `.gitignore`; you already have one)
- Sensitive RFP or client data unless your policy allows it

---

## 4. Environment for daily use

- **Cursor**: Open this folder as the workspace so all PM docs and scripts are in one place.
- **MCP**: Configure Azure DevOps and GitHub MCP servers in Cursor so you can run “good morning”, list work items, backlogs, PRs, and issues from the same environment.
- **Morning report**: Generated to `outputs/morning/morning_report.md` (gitignored by default).

After this, follow [DAILY_WORKFLOW.md](DAILY_WORKFLOW.md) for your daily routine.
