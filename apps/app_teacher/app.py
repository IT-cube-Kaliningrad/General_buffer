if __name__ == "__main__":
    try:
        app = __import__("app_class")
        app.App()
    except KeyboardInterrupt:
        print("Приложение принудительно остановлено")
    except ModuleNotFoundError:
        print("Не обнаружен файл app_class.pyc")
    except Exception as e:
        print(f"Неизвестная ошибка\nError: {e}")