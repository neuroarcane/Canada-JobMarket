# Indeed Canada - Scraping Research
**Researcher:** Ali  
**Date:** 2026-04-09  
**Branch:** exploration/ali

---

## 1. robots.txt Analysis

URL: https://www.indeed.com/robots.txt

Key findings:
- Indeed **disallows** scraping of job listing pages for most bots
- Disallowed paths include `/jobs`, `/viewjob`, `/company`
- `User-agent: *` with `Disallow: /` is partially in effect for certain paths
- Scraping Indeed directly **may violate their ToS** — use with caution
- Recommended alternative: use their **Publisher API** or **Indeed Hiring Platform API**
**Conclusion:** Direct scraping is technically restricted. For production use, the official API is safer.

---

## 2. Does Indeed Have an API?

### Indeed Publisher API (Deprecated)
- Indeed had a public job search API but **shut it down in 2022**
- No longer accepting new API key registrations

### Current Official Options
| Option | Details |
|--------|---------|
| Indeed Employer API | For employers posting jobs only |
| Indeed Hiring Platform | Enterprise-level, paid |
| No public job search API | As of 2024 |

**Conclusion:** No free public API available. Scraping or third-party APIs (e.g. Adzuna, SerpAPI) are the realistic alternatives.

---

## 3. HTML Structure of Job Pages

### Job Search Results Page
URL pattern: `https://ca.indeed.com/jobs?q={title}&l={location}`

Key HTML elements:

```html
<div class="job_seen_beacon">
  <h2 class="jobTitle"><a href="/viewjob?jk=JOBID">Software Engineer</a></h2>
  <span class="companyName">Shopify</span>
  <div class="companyLocation">Ottawa, ON</div>
  <div class="salary-snippet-container">
    <div class="salary-snippet">$90,000–$120,000 a year</div>
  </div>
  <div class="job-snippet">
    <ul><li>Experience with Python and data pipelines</li></ul>
  </div>
</div>
```

### Individual Job Page
URL pattern: `https://ca.indeed.com/viewjob?jk={job_id}`

```html
<div id="jobDescriptionText">Full description text here...</div>
```

---

## 4. Fields We Can Extract

| Field | HTML Location | Reliability |
|-------|--------------|-------------|
| Job Title | `h2.jobTitle > a` | ✅ High |
| Company Name | `span.companyName` | ✅ High |
| Location | `div.companyLocation` | ✅ High |
| Salary | `div.salary-snippet` | ⚠️ Only ~30% of listings |
| Description Snippet | `div.job-snippet` | ✅ High |
| Full Description | `div#jobDescriptionText` | ✅ High (extra request needed) |
| Posted Date | `span.date` | ✅ High |
| Job Type | `div.metadata` | ⚠️ Inconsistent |

---

## 5. Challenges & Limitations

- **Bot detection:** Indeed uses Cloudflare — may return CAPTCHAs
- **Dynamic content:** Some elements load via JavaScript (may need Selenium)
- **Class names change:** Indeed updates CSS classes frequently
- **Rate limiting:** Too many requests triggers blocks — always use `time.sleep()`
- **ToS risk:** Scraping violates Indeed's ToS — for portfolio use only

### Mitigation Strategies
- Rotate User-Agent strings
- Use `time.sleep(2-5)` between requests
- Consider SerpAPI as a legal paid alternative
- For production: Adzuna API (free tier, covers Canada)

---

## 6. Recommended Approach for This Project

1. **Adzuna API** ✅ — Free tier, covers Canada, legal
2. **SerpAPI** ✅ — Paid but reliable
3. **RSS Feeds** ✅ — ToS-safe, limited
4. **Direct scraping** ⚠️ — Portfolio/research use only

---

## 7. References

- https://ca.indeed.com/robots.txt
- https://opensource.indeedeng.io/
- https://www.adzuna.ca/jobs/api
- https://serpapi.com/google-jobs-api