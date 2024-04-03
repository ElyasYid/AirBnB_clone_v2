#!/usr/bin/python3
"""A module archive formaton with Fabric."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    ct = datetime.now()
    otf = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        ct.year,
        ct.month,
        ct.day,
        ct.hour,
        ct.minute,
        ct.second
    )
    try:
        print("Packing web_static to {}".format(otf))
        local("tar -cvzf {} web_static".format(otf))
        acs = os.stat(otf).st_size
        print("web_static packed: {} -> {} Bytes".format(otf, acs))
    except Exception:
        otf = None
    return otf
