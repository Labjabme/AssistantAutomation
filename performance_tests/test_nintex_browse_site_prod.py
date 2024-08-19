import configparser
import os
from locust import HttpUser, TaskSet, between, task
import random

# Provide the full path to your config file
config_file_path = 'locust.conf'

# Read configuration from locust.conf
config = configparser.ConfigParser()

if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Configuration file {config_file_path} not found.")

config.read(config_file_path)


class BrowseAssistant(TaskSet):
    def on_start(self):
        # Assume all users start by loading the main page
        self.load_main_page()
        self.urls_on_current_page = self.toc_urls

    @task(10)
    def load_main_page(self):
        # r = self.client.get("/assistant/v2024.1.1000000017/index.html")
        r = self.client.get("/docgensf/NintexAssistant.htm")
        print(r)
        # Parse the main page content to find the relevant links
        # This is a simplified version, as the real parsing might require an HTML parser
        self.toc_urls = ["/docgensf/NintexAssistant.htm"]

    @task(50)
    def load_page(self, url=None):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
        # Parse the page content to find subpage links
        # This is a simplified version, as the real parsing might require an HTML parser
        self.toc_urls = ["/docgensf/NintexAssistant.htm"]

    @task(30)
    def load_sub_page(self):
        url = random.choice(self.urls_on_current_page)
        r = self.client.get(url)


class MyUser(HttpUser):
    tasks = [BrowseAssistant]
    host = config.get('locust', 'host')
    wait_time = between(1, 5)
