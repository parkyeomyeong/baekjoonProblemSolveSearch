from asyncore import write
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

import csv

study_group = ["qkrduaud", "tmdgk95", "vertvert123", "wt3759", "donadio912",
               "tlsalfla96", "juneseok0107", "min077", "gahee3839", "wldk1217", "parksoeun", "bb2880"]

problems = ["2742", "11021", "11022", "2438", "2439"]


def app():
    f = open("baekjoon.csv", "w")
    writer = csv.writer(f)
    URL = "https://www.acmicpc.net/status"

    driver = webdriver.Chrome('chromedriver.exe')
    # # 기다리기
    driver.implicitly_wait(10)

    driver.get(url=URL)

    for person in study_group:
        for problem in problems:
            sleep(0.1)
            driver.implicitly_wait(10)
            try:
                problem_id = driver.find_element(By.NAME, "problem_id")
                user_id = driver.find_element(By.NAME, "user_id")
                # problem_id = driver.find_element_by_name("problem_id")
                # user_id = driver.find_element_by_name("user_id")
                problem_id.clear()
                user_id.clear()

                problem_id.send_keys(problem)
                user_id.send_keys(person)
                Select(driver.find_element(By.NAME,
                                           "result_id")).select_by_value("4")
                driver.find_element(By.CSS_SELECTOR,
                                    "body > div.wrapper > div.container.content > div > div:nth-child(4) > div > form > button").click()
            except:
                print('실패')

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "status-table")))

            try:
                tbody = driver.find_element(
                    By.CSS_SELECTOR, "#status-table > tbody")
                row = tbody.find_elements(By.CSS_SELECTOR, "tbody > tr > td")
                # for index, value in enumerate(rows):
                #     body = value.find_element(By.CSS_SELECTOR, "tbody > tr > td")[0]
                #     print(body.text)
                temp = []
                for column in row:
                    temp.append(column.text)
                writer.writerow(temp)
            except:
                print("안풀었어")

    driver.close()
    f.close()


# driver.close()


def check_solve(driver, id, problems):
    driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div[4]/div/form/input[2]").send_keys(id)

    return


app()
