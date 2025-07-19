from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .database import engine, Base, get_db
from .routers import jobs
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Aggregator API")
app.include_router(jobs.router)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_jobs(
    request: Request,
    keyword: str = "",
    company: str = "",
    location: str = "",
    min_salary: str = "",
    page: int = 1,
    db: Session = Depends(get_db)
):
    limit = 10
    skip = (page - 1) * limit

    try:
        jobs_list = crud.get_filtered_jobs(db, keyword, company, location, min_salary, skip=skip, limit=limit)
        total_jobs = crud.count_filtered_jobs(db, keyword, company, location, min_salary)
        total_pages = max((total_jobs + limit - 1) // limit, 1)

        # Debug logs
        print(f"[DEBUG] total_jobs: {total_jobs}, page: {page}, limit: {limit}, total_pages: {total_pages}, skip: {skip}")
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        jobs_list = []
        total_pages = 1

    return templates.TemplateResponse("index.html", {
        "request": request,
        "jobs": jobs_list,
        "keyword": keyword,
        "company": company,
        "location": location,
        "min_salary": min_salary,
        "page": page,
        "total_pages": total_pages
    })
