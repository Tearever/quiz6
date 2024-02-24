from abc import ABC, abstractmethod

class LoggerInterface:
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(LoggerInterface):
    def log(self, message: str):
        print(f"[Console Logger] {message}")

class FileLogger(LoggerInterface):
    def log(self, message: str):
        with open("log.txt", "a") as file:
            file.write(f"[File Logger] {message}\n")

class WebApplication:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def perform_action(self):
        self.logger.log("Action performed successfully")

def main():
    app = WebApplication(ConsoleLogger())
    app.perform_action()

    app = WebApplication(FileLogger())
    app.perform_action()

if __name__ == "__main__":
    main()
