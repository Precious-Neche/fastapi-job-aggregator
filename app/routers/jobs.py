# Job-related API routes
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, scraper

router = APIRouter()

@router.get("/jobs")
def get_all_jobs(db: Session = Depends(get_db)):
    return crud.get_filtered_jobs(db)

@router.get("/jobs/search")
def search_jobs(keyword: str = "", db: Session = Depends(get_db)):
    return crud.get_filtered_jobs(db, keyword=keyword)

@router.post("/jobs/scrape")
def scrape_and_save(
    keyword: str = Query("python"),
    company: str = Query(""),
    location: str = Query(""),
    db: Session = Depends(get_db)
):
    scraped_jobs = scraper.scrape_jobs(keyword=keyword, company=company, location=location)
    saved_count = 0
    for job in scraped_jobs:
        crud.create_job(db, job)
        saved_count += 1
    return {"message": f"{saved_count} jobs scraped and saved using keyword='{keyword}', company='{company}', location='{location}'."}
