from getpass import getuser
from uuid import getnode
from platform import uname
from psutil import boot_time
from datetime import datetime
from requests import get


def getUserInfo():
    osInfo = uname()
    return \
        {
            "username": getuser(),
            "ip": get("https://api.ipify.org").text,
            "mac": getnode(),
            "timezone": datetime.fromtimestamp(boot_time()).strftime("%d/%m/%Y, %H:%M:%S"),
            "os": osInfo.system,
            "nodeName": osInfo.node,
            "osRelease": osInfo.release,
            "osVersion": osInfo.version,
            "machine": osInfo.machine,
            "processor": osInfo.processor
        }


if __name__ == '__main__':
    print(getUserInfo())
