import psycopg2
import requests
from requests_toolbelt import MultipartEncoder

'''
multipart/form-data表单提交(传非文件)
'''
class PostgresContext:
    def __init__(self):
        self.conn = psycopg2.connect('xxx')
        # 防止报 UnicodeDecodeError 错误
        self.conn.set_client_encoding('utf8')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor, self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    }

    data = MultipartEncoder(fields={'username': 'admin',
                                    'password': 'xxx'}, boundary='---------------------------xxxxx')

    headers['Content-Type'] = data.content_type

    url = 'xxx'
    r = requests.post(url, data=data.to_string().decode(), headers=headers, verify=False)
    token = r.json()['data']['token']
    print(token)


if __name__ == '__main__':
    login()
