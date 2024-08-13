import sys
import requests
from bs4 import BeautifulSoup
from companies.models import Company
from jobs.models import Job

def search_jobs(company_name):
    print(f"Searching jobs for company: {company_name}")  # Debug print
    sys.stdout.flush()  # Ensure the print statement is executed before any possible exit

    query = f"{company_name} software development job"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    print(query)
    print(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"print soup here {soup}")

    jobs = []
    for result in soup.find_all('div', class_='BVG0Nb'):
        try:
            job_link = result.find('a')['href']
            job_title = result.find('h3').text
            if "software" in job_title.lower() and "developer" in job_title.lower():
                jobs.append({
                    "company": company_name,
                    "job_title": job_title,
                    "link": job_link
                })
        except Exception as e:
            print(f"Error parsing result: {e}")  # Debug print
            sys.stdout.flush()  # Ensure the print statement is executed before any possible exit

    print(f"Jobs found for {company_name}: {jobs}")  # Debug print
    sys.stdout.flush()  # Ensure the print statement is executed before any possible exit

    return jobs

def search_jobs_for_all_companies():
    companies = Company.objects.all()
    for company in companies[:1]:
        print(f"Searching jobs for company: {company.name}")  # Debug print
        sys.stdout.flush()  # Ensure the print statement is executed before any possible exit

        job_posts = search_jobs(company.name)
        
        for job_post in job_posts:
            try:
                print(f"Attempting to save job: {job_post['job_title']} at {job_post['link']}")
                Job.objects.create(
                    company=company,
                    job_title=job_post['job_title'],
                    link=job_post['link']
                )
                print(f"Job saved: {job_post['job_title']} at {job_post['link']}")  # Debug print
                sys.stdout.flush()  # Ensure the print statement is executed before any possible exit
            except Exception as e:
                print(f"Error saving job to database: {e}")  # Debug print
                sys.stdout.flush()  # Ensure the print statement is executed before any possible exit
