# IT-Cube_Project
## Установка проекта
1. Загрузите удаленный GitHub репозиторий ->
```shell
git clone https://github.com/IT-cube-Kaliningrad/General_buffer.git
```
2. Пререйдите в корень проекта и установите библиотеки из ```requirements.txt``` ->
```shell
python -m pip install -r requirements.txt
```
## Запуск приложения для учителя
Откройте файл ```settings.conf``` в папке ```apps/app_teacher```.
  * Параметр ```SHOW_WINDOW``` предназначен для отображения окна приложения. Если вы не хотите, чтобы это окно появлялось, измените параметр на 0.
   * Параметр ```SHOW_DATA``` предназначен для отображения в окне текста с отправленным содержимым клентам. Если вы не хотите, чтобы текст появлялся, измените параметр на 0.
  * Параметр ```SERVER_IP``` предназначен для хранения IP адреса сервера в локальной сети(по умолчанию стоит 127.0.0.1).
  * Параметр ```SERVER_PORT``` предназначен для храния порта на котором был запущен сервер(по умолчанию и на сервере, и в приложении стоит 5000).
  * Параметр ```MAX_CONNECTIONS``` предназначен для хранения максимального кол-ва подключений к севреру(значение произвольное, кроме строкового).
  * Параметр ```STUDENT_DISCONNECTION``` в секции ```SHOW_WARNINGS``` включает уведомления об отсоединении студента от сервера(по умолчанию стоит 1).
  * Параметр ```CONNECTION_ATTEMPT``` в секции ```SHOW_WARNINGS``` включает уведомления об неудачной попытке подключения, которая превышает маскимальное количество подключений(по умолчанию стоит 1)

Запустите файл ```apps/app_teacher/app.py```.

При нажатии на Ctrl+C, будет считываться последняя запись из буфера обмена и отправляться всем подключенным клиентам.
## Запуск приложения для студента
Откройте файл ```settings.conf``` в папке ```apps/app_student```.
  * Параметр ```AUTOCOPY``` в секции ```APP``` включает функцию автокопирования и отключает появление окна с содержимым(по умолчанию стоит 0)
  * Параметр ```SERVER_IP``` в секции ```SERVER``` предназначен для хранения IP адреса сервера в локальной сети(по умолчанию стоит 127.0.0.1).
  * Параметр ```SERVER_PORT``` в секции ```SERVER``` предназначен для храния порта на котором был запущен сервер(по умолчанию и на сервере, и в приложении стоит 5000).
  * Параметр ```SERVER_DISCONNECTION``` в секции ```SHOW_WARNINGS``` включает уведомления об отсоединении приложения от сервера(по умолчанию стоит 0).

Запустите файл ```apps/app_student/app.py```.

При изменении данных на сервере, будет появляться окно в правом верхнем углу экрана с текстом и кнопкой для копирования.
## Используемые библиотеки
### Предустановленные библиотеки
* **tkinter**
* **tkinter.messagebox**
* **configparser**
* **threading**
* **time**
* **os**
### Библиотеки, требующие установки
* **socket**