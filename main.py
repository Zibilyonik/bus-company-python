# python3
import json


def time_order_check(lines):
    errors = []
    for line in range(len(lines)):
        if line == 0:
            continue
        if lines[line]["time"] < lines[line - 1]["time"]:
            errors.append(line)
    return errors

def main():
    lines = {}
    json_data = json.loads(input())
    for item in json_data:
        if item["stop_type"] == "S":
            lines[item["bus_id"]] = [
                {"bus_id": item["bus_id"], "stop_name": item["stop_name"], "stop_id": item["stop_id"], "time": item["a_time"]}
            ]
        else:
            lines[item["bus_id"]].append(
                {"bus_id": item["bus_id"], "stop_name": item["stop_name"], "stop_id": item["stop_id"], "time": item["a_time"]}
            )
    
    print("Arrival time test:")
    for line in lines.items():
        errors = time_order_check(line)
        if len(errors) == 0:
            print("OK")
        else:
            checked = []
            for error in errors:
                if error["bus_id"] not in checked:
                    checked.append(error["bus_id"])
                    print(
                        f"bus_id line {line}: wrong time on station {lines[line][error]['stop_id']}"
                    )


if __name__ == "__main__":
    main()
