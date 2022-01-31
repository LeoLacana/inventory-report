from setuptools import setup

setup(
    name="inventory_report",
    description="Projeto Inventory Report",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "inventory_report=inventory_report.main:main",
        ],
    },
)
