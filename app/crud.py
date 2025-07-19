from sqlalchemy.orm import Session
from app.models import Job

def get_filtered_jobs(db: Session, keyword="", company="", location="", min_salary=None, skip=0, limit=10):
    query = db.query(Job)

    if keyword:
        query = query.filter(Job.title.ilike(f"%{keyword}%"))
    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))
    if min_salary:
        try:
            min_salary = float(min_salary)
            query = query.filter(Job.salary != None, Job.salary >= min_salary)
        except:
            pass  # Ignore invalid salary filter

    return query.offset(skip).limit(limit).all()

def count_filtered_jobs(db: Session, keyword="", company="", location="", min_salary=None):
    query = db.query(Job)

    if keyword:
        query = query.filter(Job.title.ilike(f"%{keyword}%"))
    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))
    if min_salary:
        try:
            min_salary = float(min_salary)
            query = query.filter(Job.salary != None, Job.salary >= min_salary)
        except:
            pass

    return query.count()

def create_job(db: Session, job_data):
    # Avoid duplicates (title + company)
    existing = db.query(Job).filter(
        Job.title == job_data["title"],
        Job.company == job_data["company"]
    ).first()

    if not existing:
        job = Job(**job_data)
        db.add(job)
        db.commit()
        db.refresh(job)
        return job
    return existing
