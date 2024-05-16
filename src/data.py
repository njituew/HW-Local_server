import requests
import vk_api
import zulip
from dotenv import load_dotenv
import os


load_dotenv()


def get_vk_info(parameter):
    VK_TOKEN = os.getenv("VK_TOKEN")
    session = vk_api.VkApi(token=VK_TOKEN)
    return session.method('account.getProfileInfo')[parameter]


def get_zulip_info():
    client = zulip.Client(config_file="zuliprc")
    return client.get_profile()["email"]


def get_github_info():
    gitURL = "https://api.github.com/users/" + os.getenv("gitNickName")
    gitData = requests.get(gitURL).json()
    return gitData
