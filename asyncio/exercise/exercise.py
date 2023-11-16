import asyncio


async def fetch(url: str) -> str:
    # Simulate network delay
    await asyncio.sleep(2)
    return f"Data from {url}"

# TODO: Retrieve data from each of the above urls concurrently by creating a retrieve_data function

async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    


if __name__ == "__main__":
    asyncio.run(main())
