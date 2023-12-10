#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if generated successfully, otherwise None.
    """
    try:
        # Create 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Generate archive path
        time_format = "%Y%m%d%H%M%S"
        archive_path = "versions/web_static_{}.tgz".format(
            datetime.utcnow().strftime(time_format)
        )

        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(archive_path))

        # Return the archive path
        return archive_path

    except Exception as e:
        # Return None if there's an exception
        return None

if __name__ == "__main__":
    do_pack()
