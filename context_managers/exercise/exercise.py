# Implement a context manager decorator named file_manager


def write_file_content(content: str):
    with file_manager("sample.txt", "w") as file:
        file.write(content)
        
def main() -> None:
    write_file_content("Hello, world!")


if __name__ == "__main__":
    main()
