import base64
import os


def encode_base64(file):
    with open(file, 'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        print(type(base64_data))
        # print(base64_data)
        # 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64,
        base64_str = str(base64_data, 'utf-8')
        print(base64_str)
        return base64_data


def decode_base64(base64_data):
    with open('./22.jpeg', 'wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)


if __name__ == '__main__':
    img_path = './11.jpeg'
    base64_data = encode_base64(img_path)
    decode_base64(base64_data)
