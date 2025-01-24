import glob
from collections import defaultdict
from datetime import datetime


def parse_log_line(log_line):
    try:
        # 分割日志行成多个部分
        parts = log_line.split()

        # 提取日期时间（假设是第一个部分）
        datetime_str = parts[0]

        # 提取主机名（假设是第二个部分）
        hostname = parts[1]

        # 查找 NSX 的索引并提取进程 ID
        nsx_index = parts.index('NSX')
        pid = parts[nsx_index + 1]

        # 查找关键字 "Registered metric_collect_interval:" 并提取其后的内容
        message_start = log_line.find('Registered metric_collect_interval:')
        if message_start != -1:
            message = log_line[message_start + len('Registered metric_collect_interval:'):].strip()
            return {
                'datetime': datetime_str,
                'hostname': hostname,
                'pid': pid,
                'message': message
            }
        else:
            return None
    except Exception as e:
        # print(f"Error parsing log line: {e}, log_line:{log_line}")
        return None


def extract_logs_and_count_messages(log_files, output_file, stats_file):
    process_logs = {}
    message_counts = defaultdict(int)

    for log_file in log_files:
        print(f"Starting to process file: {log_file}")
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_log = parse_log_line(line)
                if parsed_log and parsed_log['message']:
                    pid = parsed_log['pid']
                    datetime_str = parsed_log['datetime']
                    parsed_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ')

                    # 如果该 PID 已存在且当前日志的打印时间更晚，则更新
                    if pid not in process_logs or parsed_datetime > datetime.strptime(process_logs[pid]['datetime'],
                                                                                      '%Y-%m-%dT%H:%M:%S.%fZ'):
                        process_logs[pid] = parsed_log  # 只保留每个 PID 的最后一条匹配日志

                    message_counts[parsed_log['message']] += 1

        print(f"Finished processing file: {log_file}")

    # 输出日志到文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for pid, log_entry in process_logs.items():
            out_file.write(
                f"Process ID: {pid}, DateTime: {log_entry['datetime']}, HostName: {log_entry['hostname']}, Message: {log_entry['message']}\n")

    # 输出统计信息到文件
    with open(stats_file, 'w', encoding='utf-8') as stats_f:
        stats_f.write("Message Statistics:\n")
        for message, count in sorted(message_counts.items(), key=lambda item: item[1], reverse=True):
            stats_f.write(f"Message: {message}, Count: {count}\n")


def main():
    # 获取当前目录下所有以"syslog"为前缀的日志文件
    log_prefix = "syslog"
    log_files = glob.glob(f"{log_prefix}*")

    if not log_files:
        print("No syslog files found.")
        return

    print("Starting to extract logs and count messages...")
    output_file = "parsed_logs.txt"
    stats_file = "message_statistics.txt"
    extract_logs_and_count_messages(log_files, output_file, stats_file)
    print("Log extraction and message counting completed.")


if __name__ == "__main__":
    main()