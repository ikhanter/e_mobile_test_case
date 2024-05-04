### Task

Цель: Создать приложение для учета личных доходов и расходов.

Основные возможности:
1. Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
2. Добавление записи: Возможность добавления новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.

Требования к программе:
1. Интерфейс: Реализация через консоль (CLI), без использования веб- или графического интерфейса (также без использования фреймворков таких как Django, FastAPI, Flask  и тд).
2. Хранение данных: Данные должны храниться в текстовом файле. Формат файла определяется разработчиком.
3. Информация в записях: Каждая запись должна содержать дату, категорию (доход/расход), сумму, описание (возможны дополнительные поля).

Будет плюсом:
1. Аннотации: Аннотирование функций и переменных в коде.
2. Документация: Наличие документации к функциям и основным блокам кода.
3. Описание функционала: Подробное описание функционала приложения в README файле.
4. GitHub: Размещение кода программы и примера файла с данными на GitHub.
5. Тестирование.
6. Объектно-ориентированный подход программирования.

Пример структуры данных в файле:
Дата: 2024-05-02
Категория: Расход
Сумма: 1500
Описание: Покупка продуктов

Дата: 2024-05-03
Категория: Доход
Сумма: 30000
Описание: Зарплата

### Решение
Программа создает файл ```log.json``` в корне каталога, куда записывает все изменения с балансом, текущее и начальное его значение. После каждой операции, а также после редактирования операции происходит пересчет актуального значения баланса. У каждой операции есть свой ID, по которому производится выбор для редактирования. 

Поиск операций производится через специальное меню, куда можно добавлять значения по категориям: ID, Категория, Сумма, Дата создания, Описание. Поиск нестрогий, т.е. если в ОДНОМ поле поиска задано несколько значений, то вернется результат, если операция соответствует хотя бы одному полю из списка. Разные поля проверяются строго, т.е. все разные поля учитываются. Пример с поиском операций с суммой 400 за 2 дня:

Категории поиска:
ID: []
Дата: ['2024-05-03', '2024-05-04']
Категория: []
Сумма: [400]
Описание: []

Найденные операции:
-- ID: 1
Дата создания: 2024-05-03 21:47:55
Категория: Доход
Сумма: 400
Описание: 100

-- ID: 4
Дата создания: 2024-05-04 01:41:08
Категория: Расход
Сумма: 400
Описание: 123123


### Установка
```make install```

### Запуск
```make start```

### Линтер
```make lint```