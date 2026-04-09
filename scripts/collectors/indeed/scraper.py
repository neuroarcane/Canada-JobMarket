"""
Indeed Canada Job Scraper
Researcher: Ali
Date: 2026-04-09

NOTE: For research/portfolio use only.
Indeed's ToS restricts automated scraping.
Consider Adzuna API for production use.
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def scrape_indeed_jobs(query: str, location: str, pages: int = 3) -> list[dict]:
    jobs = []
    base_url = "https://ca.indeed.com/jobs"

    for page in range(pages):
        params = {"q": query, "l": location, "start": page * 10}
        response = requests.get(base_url, headers=HEADERS, params=params)

        if response.status_code != 200:
            print(f"Failed on page {page}: status {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.find_all("div", class_="job_seen_beacon")

        for card in job_cards:
            job = extract_job_data(card)
            if job:
                jobs.append(job)

        print(f"Page {page + 1}: found {len(job_cards)} jobs")
        time.sleep(2)

    return jobs


def extract_job_data(card) -> dict | None:
    try:
        title_el = card.find("h2", class_="jobTitle")
        title = title_el.get_text(strip=True) if title_el else None

        company_el = card.find("span", class_="companyName")
        company = company_el.get_text(strip=True) if company_el else None

        location_el = card.find("div", class_="companyLocation")
        location = location_el.get_text(strip=True) if location_el else None

        salary_el = card.find("div", class_="salary-snippet-container")
        salary = salary_el.get_text(strip=True) if salary_el else "Not listed"

        snippet_el = card.find("div", class_="job-snippet")
        description = snippet_el.get_text(strip=True) if snippet_el else None

        link_el = title_el.find("a") if title_el else None
        job_id = link_el["href"].split("jk=")[-1] if link_el else None
        job_url = f"https://ca.indeed.com/viewjob?jk={job_id}" if job_id else None

        return {
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "description_snippet": description,
            "job_url": job_url,
            "source": "Indeed Canada"
        }
    except Exception as e:
        print(f"Error extracting job: {e}")
        return None


def save_to_csv(jobs: list[dict], filename: str = "indeed_jobs.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} jobs to {filename}")


if __name__ == "__main__":
    results = scrape_indeed_jobs(
        query="data analyst",
        location="Toronto, ON",
        pages=2
    )
    save_to_csv(results)
    print(f"\nTotal jobs collected: {len(results)}")