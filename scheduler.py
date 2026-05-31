import schedule
import time
from scraper import scrape_website
from email_sender import send_email

def job():

    print("Running scheduled task...")

    scrape_website("https://www.example.com")

    send_email()

    print("Task completed!")

schedule.every().day.at("08:00").do(job)    

print("Schedular started...")

while True:

    schedule.run_pending()

    time.sleep(60)