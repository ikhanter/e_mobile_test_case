"""Main class Balance to form and to control the data."""
from collections.abc import Iterable
from datetime import datetime

from e_mobile_test_case.operations import BaseOperation


class Balance:

    """Main class."""

    def __init__(
            self,
            init_money: int,
            current_money: int,
            operations: list[BaseOperation] = [],
        ) -> None:
        """
        Init starting attributes.

        Returns
        -------
            None: just make attributes for new instance

        """
        self.init_money = init_money
        self.money = current_money
        self.operations = operations

    def get_income(self) -> list[BaseOperation]:
        """
        Return list of income operations.

        Returns
        -------
            list: List of income operations

        """
        return [op for op in self.operations if op.category == "Доход"]

    def get_outcome(self) -> list[BaseOperation]:
        """
        Return list of outcome operations.

        Returns
        -------
            list: List of outcome operations

        """
        return [op for op in self.operations if op.category == "Расход"]

    def add_operation(
            self,
            category: str,
            money: int,
            description: str,
        ) -> None:
        """
        Add operation to the list.

        Returns
        -------
            None: modify instance's attribute

        """
        self.operations.append(
            BaseOperation(
                len(self.operations) + 1,
                category,
                money,
                description,
            ),
        )
        if category == "Доход":
            self.money += money
        elif category == "Расход":
            self.money -= money

    def _form_search_checks(
            self,
            ids: list[int],
            dates: list[str],
            categories: list[str],
            sums: list[int],
            descriptions: list[str],
        ) -> tuple[dict, dict]:
        """
        Return 2 dicts with fields for bool values and lists of search criterias.

        Returns
        -------
            tuple[dict, dict]: 1st dict with checks, 2nd with criterias

        """  # noqa: E501
        search_checks = {}
        search_criterias = {}
        if ids:
            search_checks["id"] = None
            search_criterias["id"] = ids
        if dates:
            new_dates = [datetime.strptime(date, "%Y-%m-%d").date() for date in dates]  # noqa: E501
            dates = new_dates
            search_checks["date"] = None
            search_criterias["date"] = dates
        if categories:
            search_checks["category"] = None
            search_criterias["category"] = categories
        if sums:
            search_checks["sum"] = None
            search_criterias["sum"] = sums
        if descriptions:
            search_checks["description"] = None
            search_criterias["description"] = descriptions
        return search_checks, search_criterias

    def _extract_fields_from_operation(
            self,
            search_checks: dict,
            operation: BaseOperation,
        ) -> dict:
        """
        Return dict of operation fiedlds with unified keys.

        Returns
        -------
        dict: Dict contains operation's fields with accordant keys

        """
        search_fields = {}
        for key in search_checks:
            if key == "id":
                search_fields["id"] = operation.id
            if key == "date":
                search_fields["date"] = datetime.strptime(operation.created_at, "%Y-%m-%d %H:%M:%S").date()  # noqa: E501
            if key == "category":
                search_fields["category"] = operation.category
            if key == "sum":
                search_fields["sum"] = operation.sum
            if key == "description":
                search_fields["description"] = operation.description
        return search_fields

    def _is_iterable(self, obj) -> bool:
        """Return True if object is iterable."""
        return issubclass(type(obj), Iterable)

    def _process_search_checks(
            self,
            search_checks: dict,
            search_criterias: dict,
            operation: BaseOperation,
        ) -> None:
        """
        Fill search_checks dict with bool values of operation/criterias accordance.

        Returns
        -------
            None: Modify search_checks dict, fill with bool

        """  # noqa: E501
        search_fields = self._extract_fields_from_operation(search_checks, operation)  # noqa: E501
        for key in search_checks:
            search_checks[key] = False
            for el in search_criterias[key]:
                if self._is_iterable(el):
                    if search_fields[key] in el:
                        search_checks[key] = True
                        break
                elif search_fields[key] == el:
                    search_checks[key] = True
                    break

    def find_operations(
            self,
            ids: list[int],
            dates: list[str],
            categories: list[str],
            sums: list[int],
            descriptions: list[str],
        ) -> list[BaseOperation]:
        """Find operations by criterias."""
        search_result = []
        search_checks, search_criterias = self._form_search_checks(
            ids, dates, categories, sums, descriptions,
        )

        for op in self.operations:
            self._process_search_checks(search_checks, search_criterias, op)
            if all(search_checks.values()):
                search_result.append(op)
        return search_result

    def to_json(self) -> dict:
        """Make JSONable object of Balance instance."""
        operations = [operation.to_json() for operation in self.operations]
        return {
            "Начальный баланс": self.init_money,
            "Баланс": self.money,
            "Операции": operations,
        }
