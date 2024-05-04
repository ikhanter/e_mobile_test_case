"""Operation class with functionality."""
from datetime import datetime


class BaseOperation:

    """Operation class for functionality."""

    ALLOWED_CATEGORIES = ("Доход", "Расход")

    def _is_allowed_category(self, category) -> bool:
        """Check if category is allowed."""
        return any(category == el for el in self.ALLOWED_CATEGORIES)

    def __init__(
            self,
            id: int,
            category: str,
            money: int,
            description: str,
            created_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # noqa: B008
        ) -> None:
        """Init method."""
        if self._is_allowed_category(category):
            self.category = category
        else:
            error_message = 'Категория - "Доход" или "Расход"!'
            raise ValueError(error_message)
        self.id = id
        self.created_at = created_at
        self.sum = money
        self.description = description

    def __str__(self) -> str:
        """Represent as string."""
        return f"""ID: {self.id}
Дата создания: {self.created_at}
Категория: {self.category}
Сумма: {self.sum}
Описание: {self.description}
"""

    def edit_operation(
            self,
            new_category: str | None = None,
            new_sum: int | None = None,
            new_description: str | None = None,
        ) -> None:
        """Edit operation data."""
        changed_attributes = []

        if new_category is not None and self._is_allowed_category(new_category):
            self.category = new_category
            changed_attributes.append("Категория")
        if new_sum:
            self.sum = new_sum
            changed_attributes.append("Сумма")
        if new_description:
            self.description = new_description
            changed_attributes.append("Описание")
        print(f"Изменены параметры: {', '.join(changed_attributes)}")

    def to_json(self) -> dict:
        """Return a JSONable object."""
        return {
            "ID": self.id,
            "Категория": self.category,
            "Дата создания": self.created_at,
            "Сумма": self.sum,
            "Описание": self.description,
        }
