import argparse
import subprocess
import time
from statistics import mean
from datetime import datetime


def get_free_mem_used():
    """Execute free -k command and parse the output for Mem: used in KB."""
    try:
        result = subprocess.run(['free', '-k'], capture_output=True, text=True, check=True)
        output = result.stdout.splitlines()

        # Parse the second line which contains the 'Mem:' information
        mem_line = output[1].split()
        mem_used_kb = int(mem_line[2])  # Third column is 'used' in KB

        return mem_used_kb / 1024  # Convert KB to MB
    except subprocess.CalledProcessError as e:
        print(f"Error executing free: {e}")
        return None


def main(duration, interval):
    # Lists to store collected data in MB
    free_mem_used_data = []

    # Start collecting data
    start_time = time.time()
    end_time = start_time + duration
    iterations = int(duration / interval)  # Total number of iterations

    print("Starting data collection...")

    for i in range(iterations):
        if time.time() >= end_time:
            break

        free_mem_used = get_free_mem_used()

        if free_mem_used is not None:
            free_mem_used_data.append(free_mem_used)

        now = datetime.now()
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(f"time:{formatted_time}, sample cnt:{i}")

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

    print_stats(free_mem_used_data, "Free Mem Used")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect and display memory usage statistics.")

    parser.add_argument('--duration', type=int, default=60 * 60,
                        help='Duration of the data collection in seconds (default: 60 minutes)')
    parser.add_argument('--interval', type=float, default=1,
                        help='Interval between each sample in seconds (default: 1 second)')

    args = parser.parse_args()

    main(args.duration, args.interval)