from unittest.mock import patch
import sys
from inventory_report.main import main


def test_validar_menu_enviar_um_arquivo_csv_simples(capsys):
    with patch.object(sys,
                      "argv", ['0',
                               'inventory_report/data/inventory.csv',
                               'simples']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    assert expect == out


def test_validar_menu_enviar_um_arquivo_csv_completo(capsys):
    with patch.object(sys, "argv", ['0',
                                    'inventory_report/data/inventory.csv',
                                    'completo']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    assert expect == out


def test_validar_menu_enviar_um_arquivo_json_simples(capsys):
    with patch.object(sys, "argv", ['0',
                                    'inventory_report/data/inventory.json',
                                    'simples']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    assert expect == out


def test_validar_menu_enviar_um_arquivo_json_completo(capsys):
    with patch.object(sys, "argv", ['0',
                                    'inventory_report/data/inventory.json',
                                    'completo']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    assert expect == out


def test_validar_menu_enviar_um_arquivo_xml_simples(capsys):
    with patch.object(sys, "argv", ['0',
                                    'inventory_report/data/inventory.xml',
                                    'simples']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    assert expect == out


def test_validar_menu_enviar_um_arquivo_xml_completo(capsys):
    with patch.object(sys, "argv", ['0',
                                    'inventory_report/data/inventory.xml',
                                    'completo']):
        main()
    out, err = capsys.readouterr()
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    assert expect == out


def test_validar_menu_com_menos_argumentos(capsys):
    with patch.object(sys, "argv", ['inventory_report/data/inventory.json',
                                    '']):
        main()
    out, err = capsys.readouterr()
    assert err == "Verifique os argumentos\n"
