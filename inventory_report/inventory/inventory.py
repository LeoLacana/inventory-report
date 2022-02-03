from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import DictReader
import json
import xmltodict


class Inventory:
    @classmethod
    def list_xml(cls, file_type):
        response = []
        for row in file_type["dataset"]["record"]:
            response.append(row)

        return response

    @classmethod
    def read_files(cls, path):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                return list(DictReader(file))
            elif path.endswith(".json"):
                return json.load(file)
            elif path.endswith(".xml"):
                read_file = file.read()
                file_xml = xmltodict.parse(read_file)
                list_xml = cls.list_xml(file_xml)
                return list_xml

    @classmethod
    def import_data(cls, path, type_report):
        report = cls.read_files(path)

        if type_report == "simples":
            result = SimpleReport.generate(report)
            return result
        elif type_report == "completo":
            result = CompleteReport.generate(report)
            return result
