# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Create a context manager
# Implement a context manager decorator named file_manager that allows you to open a file
# and write content to it. Use this decorator to write the content "Hello, world!" to the file.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from contextlib import contextmanager


def write_file_content(content: str):
    with file_manager("sample.txt", "w") as file:
        file.write(content)

class file_manager():
    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode
        self.file_wrapper = open(self.file_path, self.mode, encoding="utf8")

    def __enter__(self):
        return self.file_wrapper

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_wrapper.close()

def main() -> None:
    write_file_content("Hello, world!")


if __name__ == "__main__":
    main()
