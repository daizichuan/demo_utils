from mimesis import Person
from mimesis.locales import Locale
from mimesis.schema import Field, Schema
from mimesis.enums import Gender

person = Person(Locale.ZH)
print("姓名：", person.full_name())
print("性别：", person.gender())
print("手机号码：", person.telephone())
print("电子邮箱：", person.email())

_ = Field(Locale.ZH)

schema = Schema(schema=lambda: {
    'id': _('uuid'),
    'name': _('text.word'),
    'version': _('version', pre_release=True),
    'timestamp': _('timestamp'),
    'owner': {
        'email': _('person.email', domains=['test.com'], key=str.lower),
        'token': _('token_hex'),
        'creator': _('full_name', gender=Gender.FEMALE)},
})
# 默认生成10个，也就是返回一个有10个字典的列表
data = schema.create()
print(data)
