import random
import argparse
import time
import asyncio
import aiofiles
import aiohttp

from pathlib import Path
from aiohttp import ClientSession


ARTIFACTS_PATH = Path(__file__).resolve().parents[0] / 'artifacts'


async def fetch_and_save_image(session: ClientSession, output_dir: Path, image_number: int) -> None:
    url = 'https://picsum.photos/256'
    filename = f'generated_image_{image_number}.jpg'
    filepath = output_dir / filename

    async with session.get(url) as response:
        image_data = await response.read()

        async with aiofiles.open(filepath, 'wb') as file:
            await file.write(image_data)

        print(f"Image saved: {filename}")


async def download_generated_images(num_images: int, output_directory: Path) -> None:
    async with aiohttp.ClientSession() as session:
        image_tasks = []

        for i in range(1, num_images + 1):
            task = fetch_and_save_image(session, output_directory, i)
            image_tasks.append(task)

        await asyncio.gather(*image_tasks)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Download generated images from thisxdoesnotexist.com')
    parser.add_argument('-o', '--output', type=str, default=ARTIFACTS_PATH,
                        help='Output directory for downloaded images (default: artifacts)')
    parser.add_argument('-n', '--num-images', type=int, default=10,
                        help='Number of images to download (default: 10)')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    output_dir = Path(args.output)
    num_images = args.num_images

    output_dir.mkdir(parents=True, exist_ok=True)

    asyncio.run(download_generated_images(num_images, output_dir))
