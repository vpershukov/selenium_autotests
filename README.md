## Описание
В репозитории хранится проект курса [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/promo).

Во время прогона теста откроется новое окно в браузере Google Chrome и выполнятся описанные в тестовом сценарии шаги. После завершения прогона теста окно браузера закроется автоматически.

Стек технологий:
- Python3
- Selenium

Зависимости:
```
pytest==5.1.1
selenium==3.14.0
```

## Настройка
Рекомендуется устанавливать зависимости и запускать тесты в виртуальном окружении. Создать виртуальное окружение на Unix/macOS можно командой:
```
python3 -m venv env
```
Чтобы активировать виртуальное окружение на Unix/macOS, выполните команду:
```
source env/bin/activate
```
Деактивировать виртуальное окружение можно командой `deactivate`.

Более подробные инструкции по созданию и запуску виртуального окружения смотрите в [документации](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Чтобы установить зависимости, перейдите в корневую папку проекта и выполните команду:
```
pip3 install -r requirements.txt
```

## Запуск
Запустить прогон тест-кейса можно командой `pytest`. Чтобы указать язык интерфейса, добавьте в команду флаг `--language` (например, `--language=es`). По умолчанию браузер Google Chrome будет запущен с русским языком интерфейса (`--language=ru`).

Можно запустить тесты, отмеченные метками, для этого добавьте в команду флаг `-m` и название метки (например, `-m marker_name`). Доступны следующие виды меток:
- login_guest
- need_review

Пример команды для запуска тестов с меткой `need_review`: `pytest -v --language=en -m need_review`.

## Анализ результата
Тест пройден, когда все проверки выполнены без ошибок. Пример:
```
pytest -v
test_product_page.py::test_user_can_add_product_to_basket    PASSED    [100%]
```

Если тест упадет, мы получим сообщение об ошибке. Например, такую:
```
pytest -v
FAILED test_product_page.py::test_guest_cant_see_success_message - AssertionError: Button not found
```

Тест может быть проигнорирован при запуске. Пример:
```
pytest -v
test_product_page.py::test_add_to_card_button_exists    SKIPPED    (Reason to skip test)    [100%]
```
