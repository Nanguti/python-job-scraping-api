import sys
import requests
from bs4 import BeautifulSoup
from companies.models import Company
from jobs.models import Job

def search_jobs(company_name):
    query = f"{company_name} software development job"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for result in soup.find_all('div', class_='BVG0Nb'):
        job_link = result.find('a')['href']
        job_title = result.find('h3').text
        if "software" in job_title.lower() and "developer" in job_title.lower():
            jobs.append({
                "company": company_name,
                "job_title": job_title,
                "link": job_link
            })
    return jobs

def search_jobs_for_all_companies():
    companies = Company.objects.all()
    for company in companies:
        job_posts = search_jobs(company.name)
        
        for job_post in job_posts:
            Job.objects.create(
                company=company,
                title=job_post['job_title'],
                link=job_post['link']
            )