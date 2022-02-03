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
    def read_files(cls, path, file):
        response = []
        if path.endswith(".csv"):
            file_csv = DictReader(file, delimiter=",", quotechar='"')
            for value in file_csv:
                response.append(value)
            return response
        if path.endswith(".json"):
            return json.load(file)
        if path.endswith(".xml"):
            read_file = file.read()
            file_xml = xmltodict.parse(read_file)
            list = cls.list_xml(file_xml)
            return list

    @classmethod
    def import_data(cls, path, type_report):

        report = []
        with open(path, "r") as file:
            report = cls.read_files(path, file)

        if type_report == "simples":
            result = SimpleReport.generate(report)
            return result
        elif type_report == "completo":
            result = CompleteReport.generate(report)
            return result
