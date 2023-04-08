import json

#checks data types of the input
def check_data_type(data):
    if isinstance(data, dict):
        return "dict"
    elif isinstance(data, list):
        return "list"
    elif isinstance(data, str):
        return "str"
    elif isinstance(data, int):
        return "int"
    elif isinstance(data, bool):
        return "bool"
    elif isinstance(data, float):
        return "float"
    else:
        return "none"

def main():
    expected_data_types = {
        "bus_id": "int",
        "stop_id": "int",
        "stop_name": "str",
        "next_stop": "int",
        "stop_type": "str",
        "a_time": "str"
    }
    errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    total = 0
    json_data = json.loads(input())
    for item in json_data:
        for key, value in item.items():
            if check_data_type(value) != expected_data_types[key] or (value == "" and key != "stop_type") or (key == "stop_type" and value not in ["", "S", "O", "F"]):
                errors[key] += 1
                total += 1
    print(f'Type and required field validation: {total} errors')
    for key, value in errors.items():
        print(f"{key}: {value}")
        
if __name__ == "__main__":
    main()