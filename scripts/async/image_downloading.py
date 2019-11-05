"""
A simple example comparing a simple for loop
versus using aiohttp to download a set of images.

To use the async version:
$ python3 image_downloading async

To use the simple for loop version:
$ python3 image_downloading sync
"""
import sys
import asyncio
import aiohttp
import time
from urllib import request 

# List of image URLs
images_urls = [
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/University%20Main%20Campus/1_University%20Main%20Entrance.jpg",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/University%20Main%20Campus/2_The%20University%20Mall.jpg",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/University%20Main%20Campus/3_University%20Library%20and%20The%20Gate2.jpg",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/University%20Main%20Campus/4_Science%20Centre.jpg",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/Chung%20Chi%20Campus/1_Wei%20Yuan%20Lake.JPG",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/Chung%20Chi%20Campus/2_The%20College%20Chapel.JPG",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/New%20Asia%20Campus/1_The%20Amphitheatre%20and%20Water%20Tower.JPG",
    "https://www.cpr.cuhk.edu.hk/images/common/Campus%20Photo/New%20Asia%20Campus/2_The%20Pavilion%20of%20Harmony.jpg"
]

if sys.argv[1] == "async":

    # A coroutine that uses aiohttp to download images
    async def download(url, i):
        print("Downloading image {}...".format(i))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.read()
                with open("{}.jpg".format(i), "wb") as f:
                    f.write(data)

    start_time = time.time()
    tasks = []
    for i, url in enumerate(images_urls):
        tasks.append(asyncio.ensure_future(download(url, i)))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print("Time required using asycnio: {:.4f}s".format(time.time() - start_time))

else:

    start_time = time.time()
    for i, url in enumerate(images_urls):
        print("Downloading image {}...".format(i))
        request.urlretrieve(url, "{}.jpg".format(i))

    print("Time required using loop: {:.4f}s".format(time.time() - start_time))
