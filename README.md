# IT-Cube_Project
## Запуск сервера
Откройте файл ```start.bat```. **Раздел FLASK предназначен сугубо для разработчика. Пожалуйста, не меняйте в нем параметры.**
  * Параметр ```SERVER_IP``` предназначен для хранения IP адреса сервера в локальной сети(по умолчанию стоит 127.0.0.1).
  * Параметр ```SERVER_PORT``` предназначен для хранения порта сервера, на котором он будет запускаться(по умолчанию стоит 5000).

После изменений параметров, настройте и запустите виртуальное окружение. Уже с запущенным виртуальным окружением установите пакеты через ```pip``` из ```requirements.txt``` ->
```
pip install -r requirements.txt
```
* Запуск -> Windows
```batch
start.bat
```
* Запуск -> Linux
```shell
start.sh
```
## Запуск приложения для учителя
* Откройте файл ```settings.conf``` в папке ```app_teacher```.
  * Параметр ```SHOW_WINDOW``` предназначен для отображения окна с отправленным содержимым на сервер. Если вы не хотите, чтобы это окно появлялось, измените параметр на 0.
  * Параметр ```SERVER_IP``` предназначен для хранения IP адреса сервера в локальной сети(по умолчанию стоит 127.0.0.1).
  * Параметр ```SERVER_PORT``` предназначен для храния порта на котором был запущен сервер(по умолчанию и на сервере, и в приложении стоит 5000).
* Установите все необходимые библиотеки находящиеся в файле ```requirements.txt``` с помощью ```pip``` ` ->
```
pip install -r requirements.txt
```
* Запустите файл ```app.py```.

При нажатии на Ctrl+C, будет считываться последняя запись из буфера обмена и отправляться на сервер.

## Запуск приложения для студента
* Откройте файл ```settings.conf``` в папке ```app_student```.
  * Параметр ```SERVER_IP``` предназначен для хранения IP адреса сервера в локальной сети(по умолчанию стоит 127.0.0.1).
  * Параметр ```SERVER_PORT``` предназначен для храния порта на котором был запущен сервер(по умолчанию и на сервере, и в приложении стоит 5000).
  * Параметр ```AUTOCOPY``` включает функцию автокопирования, то есть приложение не будет создавать окно в углу экрана(по умолчанию выключен)
* Установите все необходимые библиотеки находящиеся в файле ```requirements.txt``` с помощью ```pip``` ` ->
```
pip install -r requirements.txt
```
* Запустите файл ```app.py```.

При изменении данных на сервере, будет появляться окно в правом верхнем углу экрана с текстом и кнопкой для копирования.
