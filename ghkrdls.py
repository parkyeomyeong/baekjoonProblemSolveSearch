from asyncore import write
from time import sleep
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

    for id in study_group:
        sleep(0.1)
        driver.implicitly_wait(10)

        user_id = driver.find_element(By.NAME, "user_id")
        user_id.clear()
        user_id.send_keys(id)

        Select(driver.find_element(By.NAME,
                                   "result_id")).select_by_value("4")
        driver.find_element(By.CSS_SELECTOR,
                            "body > div.wrapper > div.container.content > div > div:nth-child(4) > div > form > button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "status-table")))

        re = 1
        # while re:
        #     try:
        #         next_btn = driver.find_element(By.ID, "next_page")
        #     except: re = 0
        #     finally:
        #         check_solve(driver, id, problems,writer)

        check_solve()

        # for index, value in enumerate(rows):
        #     body = value.find_element(By.CSS_SELECTOR, "tbody > tr > td")[0]
        #     print(body.text)
    def check_solve():
        rows = driver.find_element(
            By.CSS_SELECTOR, "#status-table > tbody > tr > td")[2]

        line = [id]
        for c in rows:
            if c in problems:
                line.append(c)
        # for row in rows:
        #     problem_num = row.find_element(
        #         By.CSS_SELECTOR, "tr > td")[2].text
        #     if problem_num in problems:
        #         line.append(problem_num)

        writer.writerow(line)
    driver.close()
    f.close()


# driver.close()


app()
