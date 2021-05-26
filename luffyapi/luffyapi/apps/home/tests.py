from django.test import TestCase

# Create your tests here.
import base64,json

header_dic = {
    'typ':'JWT',
    'alg':'HS256'
}

header_dic_json = json.dumps(header_dic)
header_dic_json_bytes = header_dic_json.encode('utf-8')

# 加密
ret = base64.b64encode(header_dic_json_bytes)
print(ret)

# 解密
res = base64.b64decode(ret)
print(res)