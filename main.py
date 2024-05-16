from flask import Flask, render_template
from src import data


app = Flask(__name__)


@app.route('/')
def index():
    vk_last_name = data.get_vk_info("last_name")
    vk_first_name = data.get_vk_info("first_name")
    vk_status = data.get_vk_info("status")
    vk_bdate = data.get_vk_info("bdate")
    vk_home_town = data.get_vk_info("home_town")
    vk_phone = data.get_vk_info("phone")
    zulip_email = data.get_zulip_info()
    github_data = data.get_github_info()

    return render_template('index.html', vk_last_name=vk_last_name, vk_first_name=vk_first_name,
                           vk_status=vk_status, vk_bdate=vk_bdate, vk_home_town=vk_home_town,
                           vk_phone=vk_phone, zulip_email=zulip_email, github_data=github_data)


if __name__ == '__main__':
    app.run(debug=True)
