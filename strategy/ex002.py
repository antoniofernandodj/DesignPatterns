from abc import ABC, abstractmethod
from typing import List, Dict, Any
import json
import csv
from xml.etree import ElementTree as ET


# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes


class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        result = []
        with open(file_path) as f:
            csv_reader = list(csv.reader(f))
            for row in csv_reader[1:]:
                result.append({
                    csv_reader[0][0]: row[0],
                    csv_reader[0][1]: row[1],
                    csv_reader[0][2]: row[2],
                })

        return result


class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path) as f:
            return json.load(f)


class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        tree = ET.parse(file_path)
        root = tree.getroot()
        result = []
        for element in root:
            result.append(element.attrib)

        return result


# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of
        # dictionaries using the specified file parser
        return self.file_parser.parse_file(file_path)


# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(XMLParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.xml")
    print(data)
