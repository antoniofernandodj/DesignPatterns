from typing import List, Dict, Any, Callable
import json
import csv
from xml.etree import ElementTree as ET


Payload = List[Dict[str, Any]]


def parse_csv_file(file_path: str) -> Payload:
    with open(file_path) as f:
        csv_reader = list(csv.reader(f))
        return [{
            csv_reader[0][0]: row[0],
            csv_reader[0][1]: row[1],
            csv_reader[0][2]: row[2],
        } for row in csv_reader[1:]]


def parse_json_file(file_path: str) -> Payload:
    with open(file_path) as f:
        return json.load(f)


def parse_xml_file(file_path: str) -> Payload:
    tree = ET.parse(file_path)
    root = tree.getroot()
    result = []
    for element in root:
        result.append(element.attrib)

    return result


def read_file(
    file_path: str,
    fparser: Callable[[str], Payload]
) -> Payload:

    return fparser(file_path)


if __name__ == "__main__":
    data = read_file("sample.csv", parse_csv_file)
    print(data)
