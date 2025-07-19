# Job scraping logic using Remotive API
import requests

def scrape_jobs(keyword="python", company="", location=""):
    """
    Scrapes jobs from the Remotive API based on filters.
    """
    url = "https://remotive.com/api/remote-jobs"
    params = {"search": keyword}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

    jobs = []
    for job in data.get("jobs", []):
        if company.lower() in job.get("company_name", "").lower() and \
           location.lower() in job.get("candidate_required_location", "").lower():
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "salary": job.get("salary") or None,
                "link": job.get("url")
            })

    return jobs
