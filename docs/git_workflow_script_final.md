
# Team Git Workflow

## 1. Pull latest changes before starting work
Always start your work session by pulling the latest changes from the remote repository:
```
git pull origin main
```
This ensures you have the most up-to-date code.

## 2. Create a new branch for your feature/bugfix
Create a new branch from the latest main branch for each task you work on:
```
git checkout -b feature/add-login-page
```
Use a descriptive name like `feature/new-feature`, `bugfix/fix-crash-on-load`, `refactor/clean-up-utils`.

## 3. Commit early and often
As you make progress, commit your changes frequently with clear messages:
```
git add .
git commit -m "Implement login form UI"
```
A good commit message should:
- Use imperative present tense (e.g. "Add" not "Added")
- Be 50 characters or less
- Explain WHAT the commit does, like a header
- Provide details in the commit description after a blank line if needed

Example of a well-formatted commit:
```
Implement login form UI

- Add username and password fields
- Style form with Material UI components
- Hook up field validation
```

## 4. Push your branch and open a Pull Request
When your work on the branch is complete:
```
git push -u origin feature/add-login-page
```
Then open a Pull Request on GitHub to merge your branch into `main`.
In the PR description:
- Explain the purpose of the changes
- Note any deploy steps or dependencies
- Tag reviewers and any linked issues

## 5. Address review feedback
Discuss and address any code review feedback by pushing additional commits to your branch. The PR will update automatically.

## 6. Rebase on latest main before merging
Before merging your PR, rebase your branch on the latest `main` to keep the history clean:
```
git checkout main
git pull origin main
git checkout feature/add-login-page
git rebase main
```
If there are any conflicts during the rebase, resolve them and continue:
```
git add .
git rebase --continue
```
After the rebase is complete, push your updated branch:
```
git push origin feature/add-login-page
```
Note: If you had previously pushed this branch, you may need to use `git push --force-with-lease origin feature/add-login-page` instead, as the rebase changes the commit history. However, only do this if you are sure no one else is working on this branch.

## 7. Merge and delete your branch
Once your PR is approved and rebased on latest main, merge it using the GitHub UI. Then delete your local and remote feature branch.
```
git checkout main
git pull origin main
git branch -d feature/add-login-page
git push origin --delete feature/add-login-page  
```

## Tips to avoid conflicts
- Always pull `main` before starting a new branch
- Keep branches small and short-lived
- Communicate with your team on who is working on what
- Rebase main into your branch before submitting large PRs

By following this workflow consistently, the team can minimize conflicts, keep a linear Git history, and ensure `main` stays stable and releasable.
