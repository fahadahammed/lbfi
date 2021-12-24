#!/usr/bin/python3
#
# N: Linux Bangla Font Installer
# C: Fahad Ahammed
#
# ------------------------------
import datetime
import base64
import sys
import tarfile
import os
import shutil
import urllib.request as ur
import click


project_name = "LinuxBanglaFontInstaller"
full_project_name = project_name
font_source = """https://github.com/fahadahammed/linux-bangla-fonts/raw/master/archieve/lsaBanglaFonts.tar.gz"""
tmp_name = str(base64.b64encode(str(str(datetime.datetime.now().isoformat()) +
                                    "_" + full_project_name).encode("utf-8")).decode("utf-8") +
               ".tar.gz").replace('=', '')
extracted_folder_name = "/tmp/"
install_folder = str(os.environ['HOME'] + "/.fonts/Linux-Bangla-Fonts")
downloaded_file_name = str(extracted_folder_name + tmp_name)


def download_file(url):
    try:
        file_url = url
        ur.urlretrieve(file_url, downloaded_file_name)
        return str(downloaded_file_name)
    except Exception as ex:
        print(ex)
        return False


def extract(file_name):
    try:
        with tarfile.open(file_name, "r:gz") as tarf:
            tarf.extractall(path=install_folder)
            tarf.close()
            return True
    except Exception:
        return False


def clean_folder(choice=None):
    if choice == "end":
        try:
            os.remove(downloaded_file_name)
        except OSError:
            sys.exit()
    else:
        try:
            shutil.rmtree(install_folder)
        except FileNotFoundError:
            sys.exit()


def read_pyproject_toml():
    with open(file="pyproject.toml") as tomlfile:
        lines = tomlfile.readlines()
        for line in lines:
            if "version" in line:
                return line.split('"')[-2]


@click.version_option(read_pyproject_toml())
@click.group()
def cli():
    """lbfi stands for Linux Bangla Font Installer. You can avail the fonts for your linux desktop easily with this tool."""


@click.command()
def install():
    click.echo("""
    # --------------------------
        Welcome to Linux Bangla Font Installer !
    # --------------------------
        Installing the fonts.......
    """)
    if not os.path.exists(install_folder):
        os.makedirs(install_folder)
    clean_folder()
    extract(file_name=download_file(url=font_source))
    clean_folder(choice="end")
    click.echo("Font installation completed !")

@click.command()
def config():
    click.echo('Configuration Store !')

cli.add_command(install)
cli.add_command(config)
