from inventory_report.reports.simple_report import SimpleReport
import pytest


@pytest.fixture
def stock():
    return [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]


def test_validar_simplereport_retorna_data_de_fabricacao_mais_antiga(stock):
    report = SimpleReport.generate(stock)
    assert "Data de fabricação mais antiga: 2019-09-13" in report


def test_validar_simplereport_retorna_validade_mais_proxima(stock):
    report = SimpleReport.generate(stock)
    assert "Data de validade mais próxima: 2023-01-17" in report


def test_validar_simplereport_retorna_empresa_com_maior_estoque(stock):
    report = SimpleReport.generate(stock)
    expected = (
        "Empresa com maior quantidade de produtos estocados:"
        " sanofi-aventis U.S. LLC"
    )
    assert expected in report


def test_validar_simplereport_retorna_formato_correto(stock):
    report = SimpleReport.generate(stock)
    expected = (
        "Data de fabricação mais antiga: 2019-09-13\n"
        "Data de validade mais próxima: 2023-01-17\n"
        "Empresa com maior quantidade de produtos "
        "estocados: sanofi-aventis U.S. LLC\n"
    )
    assert expected == report
