import asyncio


async def fetch_data(url: str) -> str:
    # Simulate network delay
    await asyncio.sleep(2)
    return f"Data from {url}"


async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]
    # TODO: retrieve data from each of the above urls concurrently


if __name__ == "__main__":
    asyncio.run(main())
