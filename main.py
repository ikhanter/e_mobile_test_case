"""Main module for start and work."""
import json
import os
import sys

from e_mobile_test_case.balance import Balance
from e_mobile_test_case.engine import (
    add_operation,
    edit_operation,
    find_operations_menu,
    get_balance_menu,
    print_menu,
    save_data,
)
from e_mobile_test_case.operations import BaseOperation


def main() -> None:
    """Start to interact with program."""
    print_menu()
    command = int(input("Введите номер команды: "))
    match command:
        case 1:
            get_balance_menu(balance)
        case 2:
            add_operation(balance)
        case 3:
            edit_operation(balance)
        case 4:
            find_operations_menu(balance)
        case 5:
            sys.exit()


if __name__ == "__main__":

    log_file = "log.json"

    if not os.path.exists(log_file):
        init_balance = int(input("Введите начальный баланс: "))
        balance = Balance(init_balance, init_balance)
        with open(log_file, "w") as f:
            json.dump(balance.to_json(), f, ensure_ascii=False)
    else:
        with open(log_file) as f:
            data = json.load(f)
            operations = [BaseOperation(
                operation["ID"],
                operation["Категория"],
                operation["Сумма"],
                operation["Описание"],
                operation["Дата создания"],
            ) for operation in data["Операции"]]

            balance = Balance(
                data["Начальный баланс"],
                data["Баланс"],
                operations,
            )

    while True:
        main()
        save_data(log_file, balance)
