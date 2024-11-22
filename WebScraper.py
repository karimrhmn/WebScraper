#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Initialize Selenium WebDriver for Chrome
chrome_options = webdriver.ChromeOptions()

'''
Main class

'''

class Go_online:
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    def open_site(self):
        try:
            # Navigate to google
            self.driver.get("https://www.google.com/")

            # Pause
            input("Key enter to continue...")

        finally:
            self.driver.close()



    


'''
Sub-classes

'''

# Linkedin
class LinkedIn(Go_online):
    
    def __init__(self):
        super().__init__()
    
    # Login to
    def open_site(self, username, password):

        self.username = username
        self.password = password

        # Navigate to LinkedIn
        try:
            self.driver.get("https://www.linkedin.com/")

            # Pause
            input("Key enter to continue...")

        except:
            print("Whoops something's off, possibly your internet connection?")
        
        # Click login button
        try:
            login_button = self.driver.find_element(By.LINK_TEXT, "Sign in with email")
            self.driver.implicitly_wait(10)
            login_button.click()

            # Pause
            input("Key enter to continue...")

        except:
            print("Whoops something's off, we couldn't find the login button?")

        # Enter login and password
        try:
            email_field = self.driver.find_element(By.ID, "username")
            email_field.send_keys(username)

            pass_field = self.driver.find_element(By.ID, "password")
            pass_field.send_keys(password)

            submit_button = self.driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")
            submit_button.click()

            self.driver.implicitly_wait(5)

            # Pause
            input("Key enter to continue...")

        except:
            print("Whoops, we can't login?")

    # Navigate to jobs page
    def jobs_page(self):

        try:
            # Find and click the job tab
            link = self.driver.find_element(By.XPATH, "//a[.//li-icon[@type='job']]")
            link.click()

            self.driver.implicitly_wait(5)

           # Click the link that says show all jobs
            expand_jobs = self.driver.find_element(By.LINK_TEXT, "Show all")
            expand_jobs = self.driver.find_element(By.LINK_TEXT, "Show all")
            expand_jobs.click()

            self.driver.implicitly_wait(5)

            # Pause
            input("Key enter to continue...")

        except:
            print("Whoops, we couldn't take you to the jobs page!")

    # Apply to job
    def apply(self):

        apply_button = self.driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        apply_button.click()

        self.driver.implicitly_wait(5)

        print("Waiting for next update :( )")

# Set job searching location
    def set_job(self):

        try:
             # Enter intern in job field 
             job_field = self.driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
             job_field.click()

             self.driver.implicitly_wait(5)

             job_field.send_keys("Software intern")
             job_field.send_keys(Keys.RETURN)

            # Pause
             input("Key enter to continue...")
        except:
            print("Whoops, we couldn't find the location field?")

        # Toggle easy apply filter

        try:
            e_button = self.driver.find_element(By.ID, "searchFilter_applyWithLinkedin")
            e_button.click()

            self.driver.implicitly_wait(5)

            # Pause
            input("Key enter to continue...")

        except:
            print("Whoops, couldn't find the EasyApply button?")

    

# Indeed
class Indeed(Go_online):
    pass



# Total Jobs
class Total_jobs(Go_online):
    pass



attempt = LinkedIn()
attempt.open_site("YOUR EMAIL", "YOUR PASSWORD")
attempt.jobs_page()
attempt.set_job()
attempt.apply()



'''
CURRENT STATUS : OPENS JOB ON LINKEDIN BUT DOESN'T APPLY
'''