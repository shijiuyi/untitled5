import xmltodict
import json
import os


def jsontoxml(json_str):
    xml_str = ''
    if type(json_str) == dict:
        dic = json_str
    else:
        dic = json.loads(json_str)

    try:
        xml_str = xmltodict.unparse(dic, encoding='utf-8', pretty=1)
    except Exception as e:
        xml_str = xmltodict.unparse({'request': dic}, encoding='utf-8', pretty=1)
    finally:
        return xml_str


json_path = "/home/shijiuyi/桌面/test_file/json/trans.json"
json_file = open(json_path, 'r')
json_str = json_file.read()

# print(json_str)

# with open("/home/shijiuyi/桌面/test_file/json/account.json", "r") as f:
#     json_str = f.read()
# print(json_str)
# json_str = json_str.replace("'", "\"")
# json_str = json_str.replace("{{", "{")
# json_str = json_str.replace("}}", "}")
# print(json_str)
# json_str = json_str.replace("\'", "\"")

xml_res = jsontoxml(json_str)
# print(xml_res)
xml_res = xml_res.encode()

file_path = "/home/shijiuyi/桌面/test_file/xml/"+"trans"+".txt"
if not os.path.exists(file_path):
    os.mknod(file_path)
    # os.mknod 创建文件，os.mkdir 创建文件夹
with open(file_path, 'wb') as f:
    f.write(xml_res)

# a = {
#     "user_info": {
#         "id": 12,
#         "name": "Tom",
#         "age": 12,
#         "height": 160,
#         "score": 100,
#         "variance": 12
#     }
# }
#
# print(jsontoxml(a))
