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
    tasks = [fetch_data(url) for url in urls]
    data = await asyncio.gather(*tasks)
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
