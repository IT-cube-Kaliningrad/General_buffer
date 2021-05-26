if __name__ == "__main__":
    try:
        app = __import__("app_class_student")
        app.App()
    except KeyboardInterrupt:
        print("\nПриложение принудительно остановлено")
    except ModuleNotFoundError:
        print("Не обнаружен файл app_class_student.py")
    except Exception as e:
        print(f"Неизвестная ошибка\nError: {e}")