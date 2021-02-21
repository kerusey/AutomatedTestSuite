from getpass import getuser
import socket
from uuid import getnode
from platform import uname
from psutil import boot_time
from datetime import datetime

# getting user information


def getUserInfo():
    osInfo = uname()
    return \
        {
            "username": getuser(),
            "ip": socket.gethostbyname(socket.getfqdn()),
            "mac": getnode(),
            "timezone": datetime.fromtimestamp(boot_time()),
            "os": osInfo.system,
            "nodeName": osInfo.node,
            "osRelease": osInfo.release,
            "osVersion": osInfo.version,
            "machine": osInfo.machine,
            "processor": osInfo.processor
        }




