from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from tqdm import tqdm

NUM_GAMES_TO_SCRAPE = 100
BASE_URL = "https://www.flashscore.com/match"

driver = webdriver.Chrome()
driver.get("https://www.flashscore.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.event__match')))
sleep(3)

matches = driver.find_elements(By.CSS_SELECTOR, 'div.event__match')
match_ids = [match.get_attribute("id")[4:] for match in matches][:NUM_GAMES_TO_SCRAPE]

data = []

for match_id in tqdm(match_ids, desc="Scraping Matches"):
    try:
        driver.get(f'{BASE_URL}/{match_id}/#/match-summary')
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.duelParticipant__startTime')))

        league = driver.find_element(By.XPATH, '//*[@id="detail"]/div[2]/nav/ol/li[3]/a/span').text.split(' -')[0]
        time_ = driver.find_element(By.CSS_SELECTOR, 'div.duelParticipant__startTime').text.split(' ')[1]
        home = driver.find_element(By.CSS_SELECTOR, 'div.duelParticipant__home div.participant__participantName').text
        away = driver.find_element(By.CSS_SELECTOR, 'div.duelParticipant__away div.participant__participantName').text

        odds_url = f'{BASE_URL}/football/{match_id}/#/odds-comparison/1x2-odds/full-time'
        driver.get(odds_url)
        sleep(1)
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ui-table__row')))

        odds_row = driver.find_element(By.CSS_SELECTOR, 'div.ui-table__row')
        odds = odds_row.find_elements(By.CSS_SELECTOR, 'a.oddsCell__odd span')

        odd_h = float(odds[0].text)
        odd_d = float(odds[1].text)
        odd_a = float(odds[2].text)

        data.append({
            "Id": match_id,
            "League": league,
            "Time": time_,
            "Home": home,
            "Away": away,
            "Odd_H": odd_h,
            "Odd_D": odd_d,
            "Odd_A": odd_a
        })

    except Exception as e:
        print(f"⚠️ Error with match {match_id}: {e}")

driver.quit()

df = pd.DataFrame(data)
df.to_csv("simplified_matches.csv", index=False)
print(df.head())