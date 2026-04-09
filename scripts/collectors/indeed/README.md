# Indeed Canada Collector

This folder contains scripts for collecting job data from Indeed Canada.

## Status
🔬 Research phase — scripts are samples/prototypes, not production-ready.

## Files

| File | Description |
|------|-------------|
| `README.md` | This file |
| `scraper.py` | BeautifulSoup-based scraper |

## Usage

```bash
pip install requests beautifulsoup4 pandas
python scraper.py
```

## Output Format

Each job record contains:
- `title` — Job title
- `company` — Company name
- `location` — City/province
- `salary` — Salary range (if listed)
- `description_snippet` — Short preview of job description
- `job_url` — Link to full job posting
- `source` — Always "Indeed Canada"

## Important Notes

- Indeed's robots.txt restricts scraping — **for research/portfolio use only**
- Class names may change — selectors need maintenance
- Always use delays between requests (`time.sleep(2)`)
- Consider Adzuna API as a legal alternative for production

## Related Research

See `research/indeed-scraping-ali.md` for full analysis.