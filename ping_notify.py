import subprocess
import requests
import time

def send_notification(message):
    # 替换为你的Telegram Bot的API令牌和聊天ID
    bot_token = ''
    chat_id = ''
    
    # 发送通知到Telegram
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print('无法发送通知到Telegram')

def check_host():
    hostname = '192.168.1.90'
    while True:
        result = subprocess.run(['ping', '-c', '1', hostname], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            send_notification('群晖nas宕机了')
        time.sleep(15)  # 每隔15秒执行一次ping

check_host()
