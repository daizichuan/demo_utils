import pyotp
import time

'''
pyotp是一个用于生成和验证基于时间的一次性密码（TOTP）,pyotp 使用的是30秒的有效期
'''
def one_time_secret():
    totp = pyotp.TOTP(pyotp.random_base32())  # 预共享密钥
    val = totp.now()  # 获得基于当前时间戳生成动态密码
    print(val)

    # OTP verified for current time
    print(totp.verify(val))  # 此时验证是通过的，所以verify的结果是True
    # time.sleep(30)


if __name__ == '__main__':
    for _ in range(2):
        one_time_secret()
