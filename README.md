# FastAPI Job Aggregator

A simple yet powerful **Job Listings Aggregator** built with **FastAPI**, **PostgreSQL**, and **Bootstrap**.  
It scrapes jobs from the [Remotive API](https://remotive.com/api/remote-jobs) and lets users search, filter, and browse jobs in an easy-to-use interface.

## Features
- **Fetch Latest Jobs**: Scrape jobs by keyword, company, and location using the Remotive API.
- **Smart Filtering**: Search saved jobs by keyword, company, location, or minimum salary.
- **Pagination**: Browse jobs easily with a clean and responsive pagination system.
- **Modern UI**: Bootstrap-powered interface with job cards and modal job details.
- **Database Storage**: Stores scraped jobs in a PostgreSQL database for persistent access.
- **Duplicate Protection**: Prevents duplicate entries when fetching new jobs.
- **Job Details Modal**: View all job information with an "Apply Now" button.

## Tech Stack
- **Backend**: FastAPI + SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML, Jinja2 Templates, Bootstrap 5
- **API**: Remotive Job API

## How to Run Locally
1. Clone the repo:
   ```sh
   git clone https://github.com/your-username/fastapi-job-aggregator.git
   cd fastapi-job-aggregator
   
2. Install Dependencies
   ```sh
   pip install -r requirements.txt
   
3. Set up your PostgreSQL database in app/database.py
   
4. Run the server
   ```sh
   uvicorn app.main:app --reload

5. Visit http://localhost:8000 in your browser.

