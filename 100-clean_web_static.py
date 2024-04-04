#!/usr/bin/python3
"""Fabric module to deploy webstatic archive to webservers."""
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


def do_deploy(archive_path):
    """Deploys static to host servers.
    Args:
        archive_path (str): path to archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    fn = os.path.basename(archive_path)
    fdn = fn.replace(".tgz", "")
    fdp = "/data/web_static/releases/{}/".format(fdn)
    ss = False
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
        ss = True
    except Exception:
        ss = False
    return ss


def deploy():
    """Archives and deploys static to host servers"""
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """Deletes out-of-date archives of the static files.
    Args:
        number (Any): The number of archives to keep.
    """
    arc = os.listdir('versions/')
    arc.sort(reverse=True)
    st = int(number)
    if not st:
        st += 1
    if st < len(arc):
        arc = arc[st:]
    else:
        arc = []
    for ar in arc:
        os.unlink('versions/{}'.format(ar))
    cmdp = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(st + 1)
    ]
    run(''.join(cmdp))
