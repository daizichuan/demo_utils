import psycopg2
import requests
from requests_toolbelt import MultipartEncoder
from faker import Faker


class PostgresContext:
    def __init__(self):
        self.conn = psycopg2.connect(host='',
                                     port=5432,
                                     user='',
                                     password='',
                                     database='')
        # 防止报 UnicodeDecodeError 错误
        self.conn.set_client_encoding('utf8')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor, self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


class GenNormalUser:
    log_url = ''
    normal_user_url = ''
    account = ''
    passwd = ''
    lst = []

    def get_token(self, flag=True):
        token = ''
        if flag:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            }

            data = MultipartEncoder(fields={'username': self.account,
                                            'password': self.passwd},
                                    boundary='---------------------------7e713d354f0fa6')

            headers['Content-Type'] = data.content_type

            r = requests.post(self.log_url, data=data.to_string().decode(), headers=headers, verify=False)
            token = r.json()['data']['token']
        else:
            with PostgresContext() as pc:
                cursor, conn = pc
                select_sql = 'select token from sp_token limit 1'
                cursor.execute(select_sql)
                token = cursor.fetchall()[0][0]
        return token

    def set_datas(self, num):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Authorization': self.get_token()
        }

        for _ in range(num):
            name = Faker(locale="zh-CN").name()
            phone = Faker(locale="zh-CN").phone_number()
            self.lst.append(name)

            payload = {
                "password": "ABCabc123",
                "username": name,
                "phone": phone,
                "ldapUsername": ""
            }

            r = requests.post(self.normal_user_url, json=payload, headers=headers, verify=False)
            # print(r)
            # print(r.text)

        return self.lst


if __name__ == '__main__':
    print(GenNormalUser().set_datas(1))
