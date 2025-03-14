# Пульт охраны банка

Этот проект позволяет подключить пульт охраны к удаленной базе данных с визитами и карточками пропуска, чтобы мониторить посещения хранилища банка.<br />
Если вы попали в этот репозиторий случайно, запустить проект не получится, т.к. у вас нет доступа к удаленной БД, но вы можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

## Как установить

 - Python 3.7 или выше: Убедитесь, что у вас установлен Python. Вы можете скачать его с официального сайта.
 
### 1. Скачайте код
 - Перейдите на страницу репозитория проекта.
 - Нажмите на кнопку "Code" и выберите "Download ZIP".
 
### 2. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 3. Настройте переменные окружения:
 - Создайте файл .env в корне проекта.
 - Добавьте в него данные для того, чтобы зайти в удаленное БД:
```bash
HOST_DB='Впишите хост БД'
PORT_DB='Впишите порт БД'
NAME_DB='Впишите имя БД'
USER_DB='Впишите юзера'
PASSWORD_DB='Впишите пароль'
SECRET_KEY='Впишите секретный ключ'
DEBUG_DB='Укажите нужна ли отладка (по умолчанию - True)'
```

### 4. Запустите сервер и зайдите на него:
```bash
python manage.py runserver 127.0.0.1:8000
```
Перейдите по ссылке http://127.0.0.1:8000

### Пример сайта
После запуска программы и открытия сайта вы увидите следующее:
![Моя картинка](https://cdn.picloud.cc/75d83231b2483dd9b3d1afeca5ed0417.png)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
