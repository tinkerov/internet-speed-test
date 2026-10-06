import argparse
import time

import httpx


REQUESTS_COUNT = 10


def measure_speed(url: str) -> None:
    times = []
    total_bytes = 0

    with httpx.Client(follow_redirects=True, timeout=30.0) as client:
        for i in range(REQUESTS_COUNT):
            start = time.perf_counter()

            response = client.get(url)
            response.raise_for_status()

            data = response.content

            elapsed = time.perf_counter() - start
            size = len(data)

            times.append(elapsed)
            total_bytes += size

            print(
                f"Request {i + 1}/{REQUESTS_COUNT}: "
                f"{elapsed:.3f} s, {size / 1024 / 1024:.2f} MB"
            )

    average_time = sum(times) / len(times)
    total_megabytes = total_bytes / 1024 / 1024
    speed = total_megabytes / sum(times)

    print()
    print(f"Average request time: {average_time:.3f} s")
    print(f"Downloaded data: {total_megabytes:.2f} MB")
    print(f"Average speed: {speed:.2f} MB/s")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure internet download speed."
    )
    parser.add_argument("url", help="URL of a file to download")

    args = parser.parse_args()

    try:
        measure_speed(args.url)
    except httpx.HTTPError as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()