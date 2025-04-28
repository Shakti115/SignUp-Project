import random
import time

from playwright.sync_api import sync_playwright

def random_sleep(min_time=0.5, max_time=2.5):
    time.sleep(random.uniform(min_time, max_time))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=random.randint(50, 150))  # Slow down actions slightly
    page = browser.new_page()

    page.goto("https://faruk-hasan.com/automation/automation_practice.html")
    random_sleep()
    time.sleep(2)

    signup_option = page.locator('a[onclick="toggleSignup()"]')
    signup_option.click()
    time.sleep(3)

    username_box = page.locator("[name='username']")
    username_box.click()
    username_box.fill("powers115")
    time.sleep(2)

    password_box = page.locator("#password")
    password_box.click()
    password_box.fill("GoGoGo19")
    time.sleep(2)

    confirm_box = page.locator("#confirmPassword")
    confirm_box.click()
    confirm_box.fill("GoGoGo19")
    time.sleep(2)

    submit_button = page.locator("#submitBtn")
    submit_button.click()
    time.sleep(2)
