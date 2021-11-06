import os
from dotenv import load_dotenv
dotenv_path = os.path.join('../', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

botconfig = {
    'token': 'token',
    'name': 'Console',
    'id': 901352871071715408,
    'prefix': '=',
    'accent1': 0xd7832a,
    'accent2': 0xcb3532,
    'accent3': 0x6eda5f,
    'version': '01R10-211105',
    'owner': '745665751423123628',
    'logs_channel': 848239637872377936,
    'feedback_channel': 822009639666450433,
    'unsplash_ak': '',
    'unsplash_sk': '',
    'unsplash_ur': '',
}
