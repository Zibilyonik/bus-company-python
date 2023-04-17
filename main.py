# python3
import json


def check_transfer(line):
    checked = []
    transfers = []
    for item in line:
        if item not in checked:
            checked.append(item)
        elif item not in transfers:
            transfers.append(item)
    return transfers

def main():
    stops = []
    on_demands = []
    starts = []
    ends = []
    errors = []
    json_data = json.loads(input())
    for item in json_data:
        stops.append(item["stop_name"])
        if item["stop_type"] == "S":
            starts.append(item["stop_name"])
        elif item["stop_type"] == "F":
            ends.append(item["stop_name"])
        elif item["stop_type"] == "O":
            on_demands.append(item["stop_name"])
    transfers = check_transfer(stops)
    for item in on_demands:
        if item in transfers or item in starts or item in ends:
            errors.append(item)
    errors.sort()
    print("On demand stops test:")
    if len(errors) == 0:
        print("OK")
    else:
        print(f'Wrong stop type: {errors}')

if __name__ == "__main__":
    main()
