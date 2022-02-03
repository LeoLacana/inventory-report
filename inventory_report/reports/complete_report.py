from .simple_report import SimpleReport
from datetime import date


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        result = {}
        manufacturing_dates = []

        closest_expiration = date(9999, 12, 1)
        for product in stock:

            man_date_product = product["data_de_fabricacao"].split("-")
            manufacturing_dates.append(
                date(
                    int(man_date_product[0]),
                    int(man_date_product[1]),
                    int(man_date_product[2]),
                )
            )

            if product["nome_da_empresa"] not in result:
                result[product["nome_da_empresa"]] = 1
            else:
                result[product["nome_da_empresa"]] += 1

            expiration_date = product["data_de_validade"].split("-")
            test_date = date(
                int(expiration_date[0]),
                int(expiration_date[1]),
                int(expiration_date[2]),
            )
            if (
                date.today() < test_date
                and test_date < closest_expiration
            ):
                closest_expiration = test_date

        older_manufacturing = min(manufacturing_dates)
        simple_report = (
            f"Data de fabricação mais antiga: {older_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {max(result)}\n\n"
            "Produtos estocados por empresa: \n"
        )

        complete_report = ""
        for company in result.keys():
            complete_report += f"- {company}: {result[company]}\n"

        return f"{simple_report}{complete_report}"
