# Canada Job Market Analysis

Tracking Canada's job market for a month to see what's actually happening out there.

## What's This About?

We're collecting job postings from across Canada for 30 days straight. The idea is to see what skills employers actually want, where the jobs are, what they pay, and how the market moves day-to-day. Once we have the data, we'll figure out what's interesting and dig into that.

Most job market analyses focus on the US. Canada gets less attention, but the market here is different - immigration affects hiring, some provinces require bilingual skills, industries cluster in specific cities. This project fills that gap.

## The Plan

**Month 1: Collection**
- Run scrapers daily on major Canadian job boards
- Track company career pages directly
- Store everything in a database
- Watch for patterns as they emerge
- Keep the pipeline running smoothly

**After That: Analysis**
Whatever the data shows is interesting. Could be:
- Which skills are actually in demand (not just what bootcamps say)
- How salaries vary by city and role
- Geographic patterns - where are the jobs?
- Remote work trends
- How long postings stay up
- Industry-specific insights
- Differences between what shows up on job boards vs. company sites

## Tech Stack

**Data Collection:** Python (BeautifulSoup, Selenium, Scrapy)  
**Storage:** PostgreSQL or SQLite  
**Processing:** Pandas, NumPy  
**NLP:** spaCy for extracting skills from job descriptions  
**Analysis:** Jupyter notebooks, scikit-learn  
**Visualization:** Matplotlib, Plotly  
**Interactive Apps:** Streamlit and Gradio  
**Deployment:** Streamlit Community Cloud, Hugging Face Spaces

## Data Sources

**Job Boards:**
- Indeed Canada
- LinkedIn
- Workopolis
- Government of Canada Job Bank

**Company Career Pages:**
We're also tracking career pages directly from major Canadian employers. This gives us:
- Jobs that might not be posted on job boards
- More accurate salary information (sometimes)
- Better sense of company-specific requirements
- Data on how quickly companies hire

Still deciding which companies to track, but thinking:
- Major tech companies (Shopify, OpenText, CGI, etc.)
- Banks (RBC, TD, Scotiabank, etc.)
- Healthcare organizations
- Engineering firms
- Other significant Canadian employers

**Coverage:**
- Tech, healthcare, finance, engineering
- Toronto, Vancouver, Montreal, Calgary, Ottawa + smaller cities
- Remote positions

## Planned Repository Structure

Here's how we're planning to organize everything once we start building:

```
├── data/               # Raw and processed datasets
├── scripts/            
│   ├── collectors/     # Job board scrapers
│   ├── company_scrapers/  # Company career page scrapers
│   └── processors/     # Data cleaning scripts
├── notebooks/          # Analysis notebooks
├── streamlit_app/      # Interactive dashboard
├── gradio_demos/       # ML demo apps
├── visualizations/     # Charts and graphs
└── .github/
    └── workflows/      # CI/CD pipelines
```

## Interactive Demos

Once we have enough data, we'll build:

**Streamlit Dashboard**
- Explore job posting trends
- Filter by location, industry, skills
- Compare salaries across cities
- See how things changed over the month
- Compare job board vs. direct company postings

**Gradio Apps**
- Paste a job description, get extracted skills and requirements
- Input your skills, see what roles match
- Compare different cities for your role
- Predict trends based on the data

We'll deploy these to Streamlit Community Cloud and Hugging Face Spaces so anyone can play with them.

## Deployment Pipeline

We're planning to set up automated deployment:

**Streamlit Dashboard:**
- Host on Streamlit Community Cloud (free tier)
- Auto-deploy from main branch on push
- Connected to GitHub for continuous updates
- Live URL will be shared once deployed

**Gradio Demos:**
- Host on Hugging Face Spaces
- Each demo as a separate Space
- Auto-deploy on push
- Easy embedding and sharing

**CI/CD:**
- GitHub Actions for testing and linting
- Automated data pipeline runs (if we keep collecting)
- Documentation builds
- Deploy on merge to main

The goal is to make everything automatically update when we push changes, so the live demos stay current with our analysis.

## Getting Started

We haven't written the code yet, but once we do, setup will look something like:

```bash
git clone https://github.com/neuroarcane/Canada-JobMarket.git
cd Canada-JobMarket
pip install -r requirements.txt
```

We'll update this section with proper instructions as we build things out.

## Current Status

**What we're doing now:**
- Planning the project scope
- Figuring out data sources and collection strategy
- Identifying which companies to track
- Setting up the repository structure

**Coming soon:**
- Data collection pipeline
- 30-day monitoring period
- Data cleaning and processing
- Analysis and insights
- Interactive dashboards
- Deployment setup
- Final report

## Why This Matters

Job boards show you postings, but they don't show you the bigger picture. What's trending? Where are opportunities growing? What skills actually matter? This project answers those questions with real data.

By tracking both job boards and company career pages, we get a more complete view - some companies post everywhere, others only on their own sites. That difference tells us something too.

Also, it's a good way to demonstrate end-to-end data work - collection, cleaning, analysis, visualization, and deployment. The kind of stuff you'd do in an actual data role.

## Contributing

This is mainly a portfolio project, but if you spot bugs or have ideas, open an issue or PR.

## What's Next

Short term:
- Build the data collection pipeline
- Start the 30-day monitoring period
- Clean and process the data
- Run exploratory analysis
- Build Streamlit dashboard and Gradio demos
- Set up deployment pipeline

Long term:
- Maybe extend to 3-6 months to catch seasonal patterns
- Compare with US market data
- Build predictive models
- Turn it into something people can actually use

## Team

Contributors to this project can be found in the [contributors](https://github.com/neuroarcane/Canada-JobMarket/graphs/contributors) section.

---

**Note:** This is an active project in early stages. We'll update this README as we make progress.
