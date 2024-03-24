from jinja2 import Template
from datetime import *
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_FILE_NAME = os.getenv("TEMPLATE_FILE_NAME")
INDEX_FILE_NAME = os.getenv("INDEX_FILE_NAME")
RESUME_FILE_NAME = os.getenv("RESUME_FILE_NAM")
user_id = os.getenv("user_id")
access_token = os.getenv("access_token ")

def generate_resume():
    url = f'https://api.vk.com/method/users.get?user_ids={user_id}&access_token={access_token}&v=5.89'
    response = requests.get(url).json()
    user_info = response['response'][0]

    with open (TEMPLATE_FILE_NAME, "r", encoding="utf-8") as template_file:
        template_text = template_file.read()
        jinja_template = Template(template_text)
        rendered_resume = jinja_template.render(
            first_name=user_info["first_name"],
            last_name=user_info["last_name"],
            id=user_info["id"],
            datetime=datetime.now()
        )
        with open(INDEX_FILE_NAME, "w", encoding="utf-8") as resume_file:
            resume_file.write(rendered_resume)

def get_resume():
    with open (INDEX_FILE_NAME, "r", encoding="utf-8") as f:
        return f.read()