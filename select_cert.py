# -*- coding: UTF-8 -*-
import time

import autoit

'''
autoitv3的python封装实现，使用pyautoit库 https://github.com/jacexh/pyautoit
'''


def _select_cert(cert, up_down):
    flag = 0
    cert_info_ui_old = ''
    while flag == 0:
        cert_info_ui = autoit.control_command("请选择您用来签名的证书：", "ListBox1", "GetCurrentSelection")
        print(cert_info_ui)

        if cert_info_ui_old == cert_info_ui:
            flag = 1

        elif cert not in cert_info_ui:
            autoit.send('{' + up_down + '}')
            cert_info_ui_old = cert_info_ui

        elif cert in cert_info_ui:
            cert_info_ui_list = cert_info_ui.split(',')
            for _ in cert_info_ui_list:
                if cert == _.split('=')[1]:
                    autoit.control_click("请选择您用来签名的证书：", "Button1")
                    flag = 1
                    return True
            else:
                autoit.send('{' + up_down + '}')
                cert_info_ui_old = cert_info_ui
        time.sleep(0.2)


def select_cert(cert):
    autoit.win_activate("请选择您用来签名的证书：")
    autoit.control_click("请选择您用来签名的证书：", "ListBox1")

    # 先down后up原因是，第一次down很可能不是从第一行开始查，而是从中间开始查，原因没找到。
    # 所以往下找不到，就向上找，向上找可以遍历所有
    if _select_cert(cert, 'DOWN'):
        pass
    elif _select_cert(cert, 'UP'):
        pass


if __name__ == '__main__':
    select_cert('rsa1024')
