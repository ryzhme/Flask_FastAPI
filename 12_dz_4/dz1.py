"""
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение
должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения
программы.
"""
import os
import sys
import requests
import threading
import time
from multiprocessing import Process
import asyncio
import aiohttp
import aiofiles


def check_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


def download(url, folder):
    start_time = time.time()
    check_folder(folder)
    filename = url.split('/')[-1]
    p = requests.get(url)

    with open(f'{folder}\\{filename}', 'wb') as file_d:
        file_d.write(p.content)

    print(f"Загружено {url} за {time.time() - start_time:.2f} секунд(ы)")


def threads_mode(urls):
    print('Загрузка изображений в режиме многопоточности:')
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url, 'threads_img'])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Общее время загрузки в режиме многопоточности {time.time() - start_time:.2f} секунд(ы)")


def multiprocessing_mode(urls):
    print('Загрузка изображений в режиме многопроцессорности:')
    start_time = time.time()
    processes = []

    for url in urls:
        process = Process(target=download, args=(url, 'multiprocessing_img'))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    print(f"Общее время загрузки в режиме многопроцессорности {time.time() - start_time:.2f} секунд(ы)")


async def download_async(url, folder):
    start_time = time.time()
    filename = url.split('/')[-1]
    check_folder(folder)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                f = await aiofiles.open(f'{folder}\\{filename}', mode='wb')
                await f.write(await response.read())
                await f.close()
        print(f"Загружено {url} за {time.time() - start_time:.2f} секунд(ы)")


async def run_async_download(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_async(url, 'async_img'))
        tasks.append(task)
    await asyncio.gather(*tasks)


def async_mode(urls):
    print('Загрузка изображений в асинхронном режиме:')
    start_time = time.time()
    asyncio.run(run_async_download(urls))

    print(f"Общее время загрузки в асинхронном режиме {time.time() - start_time:.2f} секунд(ы)")


if __name__ == '__main__':
    cmd_urls = sys.argv[1:]

    if len(cmd_urls) == 0:
        print('Неверная команда. Укажите адреса для скачивания изображений')
    else:
        threads_mode(cmd_urls)
        multiprocessing_mode(cmd_urls)
        async_mode(cmd_urls)

# python dz1.py https://gb.ru/android-chrome-192x192.png https://www.auto-dd.ru/wp-content/uploads/2022/09/porsche-logo_02-920x518.png https://airlia.ru/images/proekty/STD_logo_tsum_680.jpg https://vinyl-market.ru/images/shop_items/1675.jpg https://cdn.worldvectorlogo.com/logos/svg-6.svg
