# Setup: Pushing to NAU-OSS

This project is ready to be published under the [NAU-OSS organization](https://github.com/NAU-OSS).

## Steps to Publish

1. **Create the repository on GitHub**
   - Go to [https://github.com/NAU-OSS](https://github.com/NAU-OSS)
   - Click "New repository"
   - Name it `number-utils` (or your preferred name)
   - Add a short description
   - Choose Public
   - Do **not** initialize with README (we already have one)
   - Click Create repository

2. **Initialize git and push** (if not already a git repo):
   ```bash
   cd number-utils
   git init
   git add .
   git commit -m "Initial open source release with documentation"
   git remote add origin https://github.com/NAU-OSS/number-utils.git
   git branch -M main
   git push -u origin main
   ```

3. **If the repo already exists and you're adding this project:**
   ```bash
   cd number-utils
   git remote add origin https://github.com/NAU-OSS/number-utils.git
   git push -u origin main
   ```

4. **Create "good first issue" labels and sample issues** (optional but recommended):
   - In GitHub: Settings → Labels → create `good first issue`, `bug`, `enhancement`, `documentation`
   - Open 1–2 issues with simple tasks (e.g., "Add example for negative numbers to README") and label them `good first issue`

## Verify

- [ ] Project is under NAU-OSS
- [ ] LICENSE, README, CONTRIBUTING, CODE_OF_CONDUCT are present
- [ ] README links to CONTRIBUTING and CODE_OF_CONDUCT
- [ ] Tests pass locally
