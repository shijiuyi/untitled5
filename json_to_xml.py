import xmltodict
import json
import os


def jsonToxml(json_str):
    try:
        xml_str = xmltodict.unparse(json_str, pretty=1)
        # print(xml_str)
        return xml_str
    except:
        print("error")


a = {
    "user_info": {
        "id": 12,
        "name": "Tom",
        "age": 12,
        "height": 160,
        "score": 100,
        "variance": 12
    }
}

print(jsonToxml(a))

# file_path = "/home/shijiuyi/桌面/test_file/xml/test.xml"
# if not os.path.exists(file_path):
#     os.mkdir(file_path)
# with open(file_path, 'wb') as f:
#     f.write(xml_1)

# if __name__ == '__main__':
#     json_path = "/home/shijiuyi/桌面/test_file/json/account.json"
#     xml_path = "/home/shijiuyi/桌面/test_file/xml/test.xml"
#     json_to_xml(json_path, xml_path)



