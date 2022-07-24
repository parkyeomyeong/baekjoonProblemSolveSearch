from asyncore import write
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

import csv
import time

study_group = ["qkrduaud", "tmdgk95", "vertvert123", "wt3759", "donadio912",
               "tlsalfla96", "juneseok0107", "min077", "gahee3839", "wldk1217", "parksoeun", "bb2880"]
problems = ["11654", "11720", "10809", "2675", "1157"]


def app():
    f = open("{}.csv".format(time.strftime("%Y_%m_%d")), "w")
    writer = csv.writer(f)
    writer.writerow(["이름"]+problems)

    URL = "https://www.acmicpc.net/status"
    driver = webdriver.Chrome('chromedriver.exe')
    # # 기다리기
    driver.implicitly_wait(2)
    driver.get(url=URL)

    for person in study_group:
        csv_row = [person]
        for problem in problems:
            sleep(0.1)

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

            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "status-table")))

            sleep(0.1)

            rows = driver.find_elements(
                By.CSS_SELECTOR, "#status-table > tbody > tr")
            whether = "풀지 않음"
            if len(rows) != 0:
                for row in rows:
                    columns = row.find_elements(By.CSS_SELECTOR, "tr > td")
                    if columns[3].text == "맞았습니다!!":
                        whether = "풀었음"
                        break
            else:
                csv_row.append(whether)
                continue
            csv_row.append(whether)

        writer.writerow(csv_row)

    driver.close()
    f.close()


if __name__ == "__main__":
    app()
