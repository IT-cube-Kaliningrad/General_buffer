if __name__ == "__main__":
    try:
        app = __import__("app_class_teacher")
        app.App()
    except KeyboardInterrupt:
        print("\nПриложение принудительно остановлено")
    except ModuleNotFoundError:
        print("Не обнаружен файл app_class_teacher.py")
    except Exception as error:
        print(f"Неизвестная ошибка\nError: {error}")