if __name__ == "__main__":
    try:
        app = __import__("app_class_teacher")
        app.App()
    except KeyboardInterrupt:
        print("Приложение принудительно остановлено")
    except ModuleNotFoundError:
        print("Не обнаружен файл app_class_teacher.cp39-win_amd64.pyd")
    except ImportError:
        print("Не обнаружен файл app_class_teacher.c")