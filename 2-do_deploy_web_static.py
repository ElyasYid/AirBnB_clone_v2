#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["18.215.160.141", "100.26.222.162"]


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    ct = datetime.now()
    ot = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        ct.year,
        ct.month,
        ct.day,
        ct.hour,
        ct.minute,
        ct.second
    )
    try:
        print("Packing web_static to {}".format(ot))
        local("tar -cvzf {} web_static".format(ot))
        archize_size = os.stat(ot).st_size
        print("web_static packed: {} -> {} Bytes".format(ot, archize_size))
    except Exception:
        ot = None
    return ot


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    fn = os.path.basename(archive_path)
    fdn = fn.replace(".tgz", "")
    fdp = "/data/web_static/releases/{}/".format(fdn)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(fn))
        run("mkdir -p {}".format(fdp))
        run("tar -xzf /tmp/{} -C {}".format(fn, fdp))
        run("rm -rf /tmp/{}".format(fn))
        run("mv {}web_static/* {}".format(fdp, fdp))
        run("rm -rf {}web_static".format(fdp))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(fdp))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
