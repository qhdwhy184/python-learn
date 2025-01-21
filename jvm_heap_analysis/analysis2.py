import argparse
import subprocess
import time
from statistics import mean
from datetime import datetime
import re
from math import ceil


def get_gc_heap_info(pid):
    """Execute jcmd command and parse the output for Heap Used and Metaspace Used in MB."""
    try:
        result = subprocess.run(['jcmd', pid, 'GC.heap_info'], capture_output=True, text=True, check=True)
        output = result.stdout

        # Regular expressions to match Heap Used and Metaspace Used lines
        heap_used_pattern = re.compile(r"garbage-first heap.*used (\d+)K")
        metaspace_used_pattern = re.compile(r"Metaspace\s+used (\d+)K")

        heap_used_match = heap_used_pattern.search(output)
        metaspace_used_match = metaspace_used_pattern.search(output)

        heap_used_kb = int(heap_used_match.group(1)) if heap_used_match else None
        metaspace_used_kb = int(metaspace_used_match.group(1)) if metaspace_used_match else None

        # Convert KB to MB
        heap_used_mb = heap_used_kb / 1024 if heap_used_kb is not None else None
        metaspace_used_mb = metaspace_used_kb / 1024 if metaspace_used_kb is not None else None

        return heap_used_mb, metaspace_used_mb
    except subprocess.CalledProcessError as e:
        print(f"Error executing jcmd: {e}")
        return None, None


def get_rss_memory(pid):
    """Execute ps command and parse the output for RSS memory in MB."""
    try:
        result = subprocess.run(['ps', '-p', pid, '-o', 'rss='], capture_output=True, text=True, check=True)
        rss_kb = int(result.stdout.strip())
        rss_mb = rss_kb / 1024
        return rss_mb
    except subprocess.CalledProcessError as e:
        print(f"Error executing ps: {e}")
        return None


# def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#     filled_length = int(length * iteration // total)
#     bar = fill * filled_length + '-' * (length - filled_length)
#     print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
#     # Print New Line on Complete
#     if iteration == total:
#         print()


def main():
    # Get process ID from user input
    parser = argparse.ArgumentParser(description='Process some integers.')

    # 添加命令行参数
    parser.add_argument('pid', type=str, help='an string representing the process ID')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取 PID
    pid = args.pid

    print(f"Received process ID (pid): {pid}")

    # Constants for the script
    duration = 2 * 60  # 2 minutes in seconds
    interval = 0.2  # 0.5 seconds between each command execution

    # Lists to store collected data in MB
    heap_used_data = []
    metaspace_used_data = []
    rss_memory_data = []

    # Start collecting data
    start_time = time.time()
    end_time = start_time + duration
    iterations = int(duration / interval)  # Total number of iterations

    print("Starting data collection...")

    for i in range(iterations):
        if time.time() >= end_time:
            break

        heap_used, metaspace_used = get_gc_heap_info(pid)
        rss_memory = get_rss_memory(pid)

        if heap_used is not None and metaspace_used is not None and rss_memory is not None:
            heap_used_data.append(heap_used)
            metaspace_used_data.append(metaspace_used)
            rss_memory_data.append(rss_memory)

        now = datetime.now()

        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print("time:{}, sample cnt:{}".format(formatted_time, i))
        # elapsed_time = time.time() - start_time
        # remaining_time = max(0, duration - elapsed_time)
        # print_progress_bar(i + 1, iterations,
        #                    prefix='Progress:',
        #                    suffix=f' Remaining: {remaining_time:.1f}s',
        #                    length=50)
        time.sleep(interval)

    print("\nData collection completed.")

    # Calculate and print statistics in MB
    def print_stats(data, name):
        if data:
            print(f"{name} Stats (in MB):")
            print(f"  Max: {max(data):.2f} MB")
            print(f"  Min: {min(data):.2f} MB")
            print(f"  Avg: {mean(data):.2f} MB")
        else:
            print(f"No data collected for {name}")

    print_stats(heap_used_data, "Heap Used")
    print_stats(metaspace_used_data, "Metaspace Used")
    print_stats(rss_memory_data, "RSS Memory")


if __name__ == "__main__":
    main()