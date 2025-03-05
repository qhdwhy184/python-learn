import asyncio
import aiohttp
from datetime import datetime


# 自定义打印函数，添加时间戳
def print_with_timestamp(message):
    # 获取当前时间并格式化为"年月日时分秒毫秒"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"[{current_time}] {message}")


async def fetch_data(session, url):
    """模拟从给定URL获取数据"""
    print_with_timestamp(f"开始从 {url} 获取数据...")
    async with session.get(url) as response:
        data = await response.text()
        print_with_timestamp(f"从 {url} 完成获取数据")
        return data


async def download_coroutine(urls):
    """下载协程，用于管理从多个URL下载数据"""
    async with aiohttp.ClientSession() as session:  # 创建会话
        tasks = [fetch_data(session, url) for url in urls]  # 创建所有下载任务
        downloaded_data = await asyncio.gather(*tasks)  # 并发执行所有下载任务
        return downloaded_data


async def process_data(data_list):
    """处理协程，模拟对下载数据进行处理"""
    print_with_timestamp("开始处理下载的数据...")
    await asyncio.sleep(1)  # 模拟处理时间
    processed_data = [f"Processed {len(data)} bytes of data" for data in data_list]
    print_with_timestamp("完成数据处理")
    return processed_data


async def main():
    """主协程，协调下载和处理操作"""
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]

    # 下载数据
    downloaded_data = await download_coroutine(urls)

    # 处理数据
    processed_data = await process_data(downloaded_data)

    print_with_timestamp(str(processed_data))


# 运行事件循环
if __name__ == "__main__":
    asyncio.run(main())