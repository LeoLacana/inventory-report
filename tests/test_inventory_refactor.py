from collections.abc import Iterator
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.inventory.inventory_iterator import InventoryIterator
import pytest

DIST = {
    "id": "1",
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2020-02-18",
    "data_de_validade": "2022-09-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1",
}


def test_validar_inter_e_instanciado_por_iterator():
    instance = InventoryRefactor(CsvImporter)
    assert isinstance(iter(instance), InventoryIterator)
    assert isinstance(iter(instance), Iterator)


def test_validar_iterar_primeiro_item_com_csv():
    instance = InventoryRefactor(CsvImporter)
    instance.import_data("inventory_report/data/inventory.csv", "simples")
    iterator = iter(instance)
    first_item_instance = next(iterator)
    assert DIST == first_item_instance


def test_validar_iterar_primeiro_item_com_json():
    instance = InventoryRefactor(JsonImporter)
    instance.import_data("inventory_report/data/inventory.json", "simples")
    iterator = iter(instance)
    first_item_instance = next(iterator)
    assert DIST == first_item_instance


def test_validar_iterar_primeiro_item_com_xml():
    instance = InventoryRefactor(XmlImporter)
    instance.import_data("inventory_report/data/inventory.xml", "simples")
    iterator = iter(instance)
    first_item_instance = next(iterator)
    assert DIST == first_item_instance


def test_validar_iterar_expandir_com_dois_arquivos():
    instance = InventoryRefactor(CsvImporter)
    instance.import_data("inventory_report/data/inventory.csv", "simples")
    instance.importer = JsonImporter
    instance.import_data("inventory_report/data/inventory.json", "simples")
    assert len(instance.data) == 20


def test_validar_enviar_arquivo_extensao_invalida():
    with pytest.raises(ValueError, match="Arquivo inválido"):
        instance = InventoryRefactor(CsvImporter)
        instance.import_data("inventory_report/data/inventory.json", "simples")
