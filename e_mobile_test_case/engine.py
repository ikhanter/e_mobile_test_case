"""Printing all submenus and use Balance"s funcs."""
import json

from e_mobile_test_case.balance import Balance


def print_menu() -> None:
    """Print main menu."""
    print(
        """\nМеню:
1. Вывести баланс
2. Добавить запись
3. Редактировать запись
4. Найти записи
5. Выйти\n""",
    )


def get_balance(balance: Balance) -> None:
    """Print current balance."""
    money = balance.money
    print(f"\nТекущий баланс: {money}")


def get_balance_menu(balance: Balance) -> None:
    """Print balance and its changes."""
    while True:
        get_balance(balance)
        command = int(
            input(
                """\nМеню баланса:
1. Показать доходы
2. Показать расходы
3. Назад

Введите команду: """,
            ),
        )
        print()
        match command:
            case 1:
                income = balance.get_income()
                print("Доходы:")
                for op in income:
                    print(f"-- {op}")
            case 2:
                outcome = balance.get_outcome()
                print("Расходы:")
                for op in outcome:
                    print(f"-- {op}")
            case 3:
                break


def add_operation(balance: Balance) -> None:
    """Add new operation to history."""
    while True:
        category = int(
            input(
                """\nМеню создания операции:
1. Доход
2. Расход
3. Назад
Введите номер операции: """,
            ),
        )
        match category:
            case 1:
             category_name = "Доход"
            case 2:
                category_name = "Расход"
            case 3:
                break
            case _:
                print("Неверная категория!")
        money = int(input("Введите сумму: "))
        description = input("Введите описание: ")
        balance.add_operation(category_name, money, description)
        print()
        print("Операция успешно  добавлена")
        print()


def find_operations_menu(balance: Balance) -> None:
    """Find operations by criterias."""
    criterias = {
        "ID": [],
        "Дата": [],
        "Категория": [],
        "Сумма": [],
        "Описание": [],
    }
    while True:
        print("\nКатегории поиска:")
        for key, val in criterias.items():
            print(f"{key}: {val}")
        print("** Для сброса параметров поиска перезайдите в меню")
        print(
            """\nМеню настройки поиска:
1. Добавить ID
2. Добавить дату
3. Добавить категорию
4. Добавить сумму
5. Добавить описание
6. Искать
7. Назад""",
        )
        command = int(input("Введите номер команды меню: "))
        match command:
            case 1:
                id_command = int(input("Введите ID: "))
                criterias["ID"].append(id_command)
            case 2:
                date_command = input("Введите дату (ГГГГ-ММ-ДД): ")
                criterias["Дата"].append(date_command)
            case 3:
                while True:
                    category_command = int(input(
                        """Выберите категорию или пункт меню:
1. Доход
2. Расход
3. Назад
""",
                    ))
                    match category_command:
                        case 1:
                            criterias["Категория"].append("Доход")
                            break
                        case 2:
                            criterias["Категория"].append("Расход")
                            break
                        case 3:
                            break
                        case _:
                            print("Пункт меню не существует!")
            case 4:
                sum_command = int(input("Введите сумму: "))
                criterias["Сумма"].append(sum_command)
            case 5:
                desc_command = input("Введите описание: ")
                criterias["Описание"].append(desc_command)
            case 6:
                result = balance.find_operations(
                    criterias["ID"],
                    criterias["Дата"],
                    criterias["Категория"],
                    criterias["Сумма"],
                    criterias["Описание"],
                )
                print("\nНайденные операции:")
                for op in result:
                    print(f"-- {op}")
                break
            case 7:
                break
            case _:
                print("Неверная команда!")

def save_data(log_file, balance: Balance) -> None:
    """Save changed data to log."""
    check_sum = balance.init_money
    for op in balance.operations:
        if op.category == "Доход":
            check_sum += op.sum
        elif op.category == "Расход":
            check_sum -= op.sum
    balance.money = check_sum
    with open(log_file, "w") as f:
        json.dump(balance.to_json(), f, ensure_ascii=False)

def edit_operation(balance: Balance) -> None:
    """Edit existing operation by ID."""
    while True:
        id_command = int(input("\nВведите ID операции: "))
        found = False
        for op in balance.operations:
            if op.id == id_command:
                found = True
                print("\nОперация найдена:")
                print(op)
                print("---")
                while True:
                    print(
                        """Меню редактирования:
1. Изменить категорию
2. Изменить сумму
3. Изменить описание
4. Назад""",
                    )
                    subcommand = int(input("Введите номер элемента меню: "))
                    match subcommand:
                        case 1:
                            category_command = int(
                                input(
                                    """\nМеню выбора номера категории
1. Доход
2. Расход
3. Назад
Введите номер категории: """,
                                ),
                            )
                            match category_command:
                                case 1:
                                    op.category = "Доход"
                                case 2:
                                    op.category = "Расход"
                                case 3:
                                    break
                                case _:
                                    print("Несуществующая команда!")

                        case 2:
                            sum_command = int(input("Введите новую сумму: "))
                            op.sum = sum_command
                        case 3:
                            desc_command = input("Введите новое описание: ")
                            op.description = desc_command
                        case 4:
                            break
                        case _:
                            print("Несуществующая команда!")
                    print("Операция:")
                    print(op)
                break
        if not found:
            print("\nОперация не найдена.\n")
        break
