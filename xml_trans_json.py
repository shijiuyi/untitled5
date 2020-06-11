import os
import json
import xmltodict


def pythonxmltojson(xml_str):
   try:
    json_dict = xmltodict.parse(xml_str, encoding='utf-8')
    json_str = json.dumps(json_dict, indent=2)
    # print(json_str)
    return json_str
   except:
       print("error")


def load_json(xml_path):
    xml_file = open(xml_path, 'r')
    xml_str = xml_file.read()
    json_dict = xmltodict.parse(xml_str)
    json_str = json.dumps(json_dict, indent=2)
    # print(json_str)
    return json_str


json_1 = load_json("/home/shijiuyi/下载/2020-04-27_2020-05-03.xml")
json_1 = json_1.encode()
file_path = "/home/shijiuyi/下载/trans.json"
with open(file_path, 'wb') as f:
    f.write(json_1)


# if __name__ == '__main__':
#     xml = """
#     <student>
#       <stid>10213</stid>
#       <info>
#         <name>name</name>
#         <sex>male</sex>
#       </info>
#       <course>
#         <name>math</name>
#         <score>90</score>
#       </course>
#     </student>
#       """
#     pythonxmltojson(xml)
