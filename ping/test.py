

# peer = '127.0.0.1'
peer = '0.0.0.1'
cmd = ['ping', '-c', '2', '-W', '1', peer]
res = None
import subprocess

try:
    res = subprocess.check_output(
                cmd,
                shell=False
            ).decode('utf-8')
# except subprocess.CalledProcessError as error:
#     print('error.stderr:{}'.format(error.stderr))
#     print('error.output:{}'.format(error.output))
except Exception as e:
    print('cmd:{}'.format(cmd))
    print('error.output:{}'.format(e.output))
    print('error.stderr:{}'.format(e.stderr))

print('res:{}'.format(res))