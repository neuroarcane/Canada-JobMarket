Hey team,

**Day 1 Tasks - Get Started**

Everyone needs to do Git setup first, then you each have a specific research assignment.

**GIT SETUP (Everyone):**

Install Git from git-scm.com

Configure:
```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

SSH Setup (recommended):
```
ssh-keygen -t ed25519 -C "your.email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Copy that key and add it to GitHub → Settings → SSH keys

Clone repo:
```
git clone git@github.com:neuroarcane/Canada-JobMarket.git
cd Canada-JobMarket
```

Create your branch:
```
git checkout -b exploration/your-name
```

**DEMO APP (Everyone):**

Install:
```
pip install streamlit plotly pandas
```

Run:
```
streamlit run demo/demo.py
```

Explore everything to understand what we're building. Make changes to the demo in your repo to add more functionality for suggestions. The idea would be finalised by next week. No changes afterwards.

---

**INDIVIDUAL ASSIGNMENTS:**

**Person 1 - Indeed Canada**
- Research file: `research/indeed-scraping-[yourname].md`
- Check Indeed.ca robots.txt
- Inspect job page HTML structure
- Does Indeed have an API?
- Try BeautifulSoup sample
- Document how to extract: title, company, location, salary, description
- Create folder: `scripts/collectors/indeed/` with README

**Person 2 - LinkedIn & Workopolis**
- Research file: `research/linkedin-workopolis-[yourname].md`
- LinkedIn Jobs API - how to access?
- Workopolis scraping allowed?
- Compare both platforms
- Document authentication needs
- Selenium for dynamic content?
- Create folders: `scripts/collectors/linkedin/` and `scripts/collectors/workopolis/` with READMEs

**Person 3 - Company Career Pages**
- Research file: `research/company-pages-[yourname].md`
- Pick 5 companies: Shopify, RBC, TD, CGI, etc.
- Document each career page structure
- Any common patterns?
- Test scraping on 1-2 companies
- Create folder: `scripts/collectors/company_pages/` with README and sample templates

**Person 4 - Database Design**
- Research file: `research/database-design-[yourname].md`
- PostgreSQL vs SQLite for our project
- Design schema: Jobs table, Companies table, Skills table
- How do they relate?
- Create sample SQL schema
- Create folders: `data/raw/`, `data/processed/`, `data/schema/` with READMEs

**Person 5 - Job Bank & Other Sources**
- Research file: `research/jobbank-other-sources-[yourname].md`
- Government Job Bank (jobbank.gc.ca) - API? Structure?
- Other Canadian job boards we missed?
- Industry-specific boards (tech, healthcare, finance)?
- Alternative methods: Adzuna API, SerpAPI, RSS feeds, datasets
- Create folders: `scripts/collectors/jobbank/` and `scripts/collectors/other_sources/` with READMEs

---

**EVERYONE:**
1. Create your assigned folders
2. Write detailed research doc
3. Include code samples where possible
4. Create README files

**COMMIT:**
```
git add .
git commit -m "Add [your topic] research and folder structure"
git push origin exploration/your-name
```

Then create Pull Request on GitHub.

**By end of day we'll have:**
- Everyone knows Git workflow
- 5 research docs covering all data sources
- Complete project structure
- Ready to start building tomorrow

Questions? Ask here.
