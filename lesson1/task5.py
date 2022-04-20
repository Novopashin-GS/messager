import subprocess
import platform
import chardet


def ping_service(service):
    code = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', code, '3', service]
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


ping_service('yandex.ru')
ping_service('youtube.com')
