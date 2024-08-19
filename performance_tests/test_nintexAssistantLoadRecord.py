import configparser
import os
from locust import HttpUser, between, task, events, tag
from playwright.async_api import async_playwright

# Provide the full path to your config.ini file
config_file_path = 'locust.conf'

# Read configuration from config.ini
config = configparser.ConfigParser()

if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Configuration file {config_file_path} not found.")

config.read(config_file_path)


class MyUser(HttpUser):
    wait_time = between(1, 5)
    host = config.get('locust', 'host')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = None
        self.browser = None
        self.context = None
        self.playwright = None

    async def on_start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=config.getboolean('locust', 'headless'))
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def on_stop(self):
        await self.page.close()
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()

    @tag('Normal')
    @task
    async def my_task(self):
        await self.page.goto(f"{self.host}/assistant/v2024.1.1000000017/index.html")
        await self.page.click("text=How can a DocGen admin manage")
        await self.page.wait_for_selector("img[alt='Nintex Assistant']")
        await self.page.wait_for_selector("div:nth-child(3) > .message")


# Hook to initialize any necessary environment settings
@events.test_start.add_listener
def on_test_start(**kwargs):
    pass


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    pass
