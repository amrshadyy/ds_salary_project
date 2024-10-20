from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import logging


# Set up logging for detailed error output
logging.basicConfig(level=logging.INFO, filename='scraping_errors.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    options = webdriver.ChromeOptions()
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)

    #url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={keyword}&locT=C&locId=1&locKeyword=&jobType="
    driver.get(url)
    jobs = []

  
         

    
    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        try:
            more = driver.find_element(by = By.CSS_SELECTOR, value = '.JobsList_buttonWrapper__ticwb > button:nth-child(1)')
            more.click()
            time.sleep(2)
            try:
                close = driver.find_element(by = By.CSS_SELECTOR, value = '.CloseButton')
                close.click()
                print('popup closed')
            except:
                print('No poopy popup...loading more jobs...')
        except:
            print('All jobs loaded')
            break
    
 
         #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        # Attempt to get job listing elements using `data-test="job-link"`
        try:
            job_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="jobListing"]'))
            )
        except TimeoutException:
            print("Job listings not found in time. Exiting...")
            break

        #Going through each job in this page
        #job_buttons = driver.find_element(By.CLASS_NAME,"jl")  #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            
            if len(jobs) >= num_jobs:
                break
            
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", job_button)  # Scroll to the job link
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(job_button)  # Ensure it's clickable
                )
                job_button.click()  # Click on the job link
                time.sleep(3)
                # Add a wait to ensure the job details are loaded (wait for a specific element in the job details section)
                '''WebDriverWait(driver, 10).until(
                 EC.visibility_of_element_located((By.CSS_SELECTOR, '.jobDescriptionSnippet'))  # Wait for job description to load
                )'''

                company_name = job_button.find_element(By.CLASS_NAME, 'EmployerProfile_compactEmployerName__LE242').text
                location = job_button.find_element(By.CLASS_NAME, 'JobCard_location__rCz3x').text
                job_title = job_button.find_element(By.CLASS_NAME, 'JobCard_jobTitle___7I6y').text
                
                #job_description = driver.find_element(By.CLASS_NAME, 'JobDetails_jobDescription__uW_fK JobDetails_blurDescription__vN7nh').text
                try:
                   job_button.find_element(by = By.XPATH, value= '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[2]/button').click()
                   time.sleep(3)
                   job_description = job_button.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]').text
                except:
                   job_description = 'null' 
                

                try:
                  salary_estimate = job_button.find_element(By.XPATH, '//section[@class="Section_sectionComponent__nRsB2 SalaryEstimate_sectionContainer__CC_hT"]//div[@class="SalaryEstimate_salaryEstimateNumber__SC4__"]').text.replace("Median", "").strip()
                except NoSuchElementException:
                  salary_estimate = "Not listed"

                try:
                   rating = job_button.find_element(By.XPATH,'.//div[@class="EmployerProfile_ratingContainer__ul0Ef"]/span').text
                except NoSuchElementException:
                   rating = "Not listed"

                try:
                       size = job_button.find_element(By.XPATH, '//span[text()="Size"]/following-sibling::div').text

                except NoSuchElementException:
                       size = -1

                try:
                        founded = job_button.find_element(By.XPATH, '//span[text()="Founded"]/following-sibling::div').text
                except NoSuchElementException:
                       founded = -1

                try:
                       type_of_ownership = job_button.find_element(By.XPATH, '//span[text()="Type"]/following-sibling::div').text
                except NoSuchElementException:
                       type_of_ownership = -1

                try:
                       industry = job_button.find_element(By.XPATH, '//span[text()="Industry"]/following-sibling::div').text
                except NoSuchElementException:
                       industry = -1

                try:
                       sector = job_button.find_element(By.XPATH, '//span[text()="Sector"]/following-sibling::div').text
                except NoSuchElementException:
                       sector = -1

                try:
                       revenue = job_button.find_element(By.XPATH, '//span[text()="Revenue"]/following-sibling::div').text
                except NoSuchElementException:
                       revenue = -1
                

                if verbose:
                 print("Job Title: {}".format(job_title))
                 print("Salary Estimate: {}".format(salary_estimate))
                 print("Job Description: {}".format(job_description[:500]))
                 print("Rating: {}".format(rating))
                 print("Company Name: {}".format(company_name))
                 print("Location: {}".format(location))
                 print("Size: {}".format(size))
                 print("Founded: {}".format(founded))
                 print("Type of Ownership: {}".format(type_of_ownership))
                 print("Industry: {}".format(industry))
                 print("Sector: {}".format(sector))
                 print("Revenue: {}".format(revenue))
                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            
                jobs.append({"Job Title" : job_title,
                "Salary Estimate" : salary_estimate,
                "Job Description" : job_description,
                "Rating" : rating,
                "Company Name" : company_name,
                "Location" : location,
                "Size" : size,
                "Founded" : founded,
                "Type of ownership" : type_of_ownership,
                "Industry" : industry,
                "Sector" : sector,
                "Revenue" : revenue,})
                #add job to jobs

 
            except ElementNotInteractableException as e:
                logging.error(f"Element not interactable: {e}")
            except Exception as e:
                logging.error(f"Error encountered while collecting job details: {e}")

            
        # Stop if the number of jobs reaches the target
        if len(jobs) >= num_jobs:
            print(f"Reached the target number of jobs: {num_jobs}")
            break
        
        
        
        # Click on the "Show more jobs" button if there are more jobs to scrape
        '''try:
            driver.find_element(by = By.CSS_SELECTOR, value = '.JobsList_buttonWrapper__ticwb > button:nth-child(1)').click()
        except NoSuchElementException:
            print(f"Scraping terminated. Collected {len(jobs)} jobs.")
            break'''

    #driver.quit()
    return pd.DataFrame(jobs)
