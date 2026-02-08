#  CSV Report Script

Скрипт для обработки csv-файла(ов).  

---

## Запуск проекта
1. Клонируем репозиторий и создаем виртуальное окружение. Активируем виртуальное окружение
   ```
   git clone https://github.com/Yakushev-Vladislav/StafIT_task.git
   cd StafIT_task
   python -m venv .venv
   source .venv/Scripts/activate
   ```
   Активация для **Linux / macOS**: ```source .venv/bin/activate```
   
2. Устанавливаем зависимости
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
   > `pip install -r requirements-dev.txt` зависимости необходимы для запуска тестов.
   > Тесты запускаются командой `python -m pytest`
3. Запускаем скрипт командой
   ```
   python main.py --files <один или несколько .csv файлов> --report <параметры отчета>
   ```
   Здесь:
   - --files - один или несколько .csv файлов с данными;
   - --report метод и параметр в формате method-parameter, например **average-gdp**
  
## Пример запуска проекта
Для примера были использованы файлы economic1.csv, economic2.csv.
```
python main.py --files economic1.csv economic2.csv --report average-gdp
```

Результаты запуска скрипта:

<img width="708" height="463" alt="results_bash" src="https://github.com/user-attachments/assets/c78ef7cb-c3a5-4868-94d1-ff9ba11bdc60" />


## Добавление новых отчетов
1. В `reports.py` создайте новую функию с логикой расчётов, или же импортируйте её из созданного вами файла
   ```
   from <filename.py> import <your_report_function>
   ```
2. Добавьте функцию в словарь `REPORTS`
   ```
   REPORTS = {
     "average": average,
     "<new_report_name>": <your_report_function>,
   }
   ```
3. Теперь можно вызывать новый отчет командой:
   ```
   python main.py --files economic1.csv economic2.csv --report <new_report_name>-gdp
   ```
