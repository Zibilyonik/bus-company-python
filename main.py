# python3
import json
# import re

# def check_data_type(data):
#     if isinstance(data, dict):
#         return "dict"
#     elif isinstance(data, list):
#         return "list"
#     elif isinstance(data, str):
#         return "str"
#     elif isinstance(data, int):
#         return "int"
#     elif isinstance(data, bool):
#         return "bool"
#     elif isinstance(data, float):
#         return "float"
#     else:
#         return "none"

# def check_time(time):
#     if isinstance(time, str) is False:
#         return False
#     if len(time) != 5:
#         return False
#     if time[2] != ":":
#         return False
#     if not time[:2].isdigit() or not time[3:].isdigit():
#         return False
#     if int(time[:2]) > 23 or int(time[3:]) > 59:
#         return False
#     return True

# def check_stop_name(name):
#     regex = r"^([A-Z][a-z]+\s)([A-Z][a-z]+\s)?(Road|Avenue|Boulevard|Street)$"
#     if re.search(regex, name):
#         return True
#     else:
#         print(name)
#     return False

def main():
    # expected_data_types = {
    #     "bus_id": "int",
    #     "stop_id": "int",
    #     "stop_name": "str",
    #     "next_stop": "int",
    #     "stop_type": "str",
    #     "a_time": "str"
    # }
    # errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}
    lines = {}
    types = {"S": [], "F": []}
    stops = []
    transfers = []
    # total = 0
    json_data = json.loads(input())
    for item in json_data:
        if item["stop_name"] in stops:
            transfers.append(item["stop_name"])
        else:
            stops.append(item["stop_name"])
        if item["stop_type"]:
            if item["stop_type"] not in types:
                types["stop_type"] = [item["stop_name"]]
            else:
                types["stop_type"].append(item["stop_name"])
        if item["bus_id"] not in lines:
            lines[item["bus_id"]] = [item["stop_name"]]
        else:
            lines[item["bus_id"]].append(item["stop_name"])
    


if __name__ == "__main__":
    main()
