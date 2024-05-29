from http.server import SimpleHTTPRequestHandler
import socketserver

# Указываем рабочую директорию для сервера
directory = '.'  # Текущая директория

# Задаем адрес и порт сервера
host = 'localhost'
port = 80

# Создаем класс обработчика запросов, наследуясь от SimpleHTTPRequestHandler
class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

# Создаем сервер с указанным хостом и портом
server = socketserver.TCPServer((host, port), CustomHandler)

# Запускаем сервер и оставляем его работать
print(f"Сервер запущен по адресу http://{host}:{port}")
server.serve_forever()
