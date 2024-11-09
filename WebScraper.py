# selenium: The primary library for controlling a web browser programmatically.
# webdriver: A module in Selenium that allows you to launch and control browsers.
# By: A Selenium module that helps locate elements on a page (e.g., by class name, ID, etc.).
# Service and ChromeDriverManager: The webdriver_manager library handles downloading and setting up ChromeDriver, which is required to run Chrome through Selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Selenium WebDriver for Chrome
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



class LinkedIn():
    def __init__(self, url):
        self.url = url
    
    def login_page(self):
        # Establish the username, password to pass to the login page
        url = self.url

        # Navigate to the webpage
        driver.get(url)

        # Find the login button and click it
        login_link = driver.find_element(By.LINK_TEXT, "Sign in with email")    
        login_link.click()

        # Wait
        driver.implicitly_wait(5)

    def sign_form(self, email, password):
        self.email = email
        self.password = password

        # Find the username button and enter email
        email_field = driver.find_element(By.ID, "username")
        email_field.send_keys(email)

        # Find the password button and enter password
        pass_field = driver.find_element(By.ID, "password")
        pass_field.send_keys(password)

        driver.implicitly_wait(5)

        # Submit button
        submit_button = driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")
        submit_button.click()

        driver.implicitly_wait(5)

    def job_page(self):
        
        # Find and click the job tab
        link = driver.find_element(By.XPATH, "//a[.//li-icon[@type='job']]")
        link.click()

        driver.implicitly_wait(5)

        # Click the link that says show all jobs
        expand_jobs = driver.find_element(By.LINK_TEXT, "Show all")
        expand_jobs.click()

        driver.implicitly_wait(5)
        

        
user_input = input("Paste a LinkedIn site link here!: ")

job_search = LinkedIn(user_input)
job_search.login_page()

login = input("Key any button to login: \n")

# Add your username and password below, as string formats "email.com", "password"
job_search.sign_form()

job_page = input("Key any button to go to jobs: \n")

job_search.job_page()

job_page = input("Waiting!: \n")


