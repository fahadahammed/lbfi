#!/usr/bin/python3
#
# N: Linux Bangla Font Installer
# C: Fahad Ahammed
#
# ------------------------------
import os
import tarfile
import datetime
import base64
import requests
import shutil
import click

project_name = "LinuxBanglaFontInstaller"
full_project_name = project_name
font_source = "https://github.com/fahadahammed/linux-bangla-fonts/raw/master/archieve/lsaBanglaFonts.tar.gz"
tmp_name = str(base64.b64encode(str(str(datetime.datetime.now().isoformat()) + "_" + full_project_name).encode("utf-8")).decode("utf-8") + ".tar.gz").replace('=', '')
extracted_folder_name = "/tmp/"
install_folder = str(os.environ['HOME'] + "/.fonts/Linux-Bangla-Fonts")
downloaded_file_name = str(extracted_folder_name + tmp_name)


def download_file(url):
    # open in binary mode
    with open(downloaded_file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)
    return str(downloaded_file_name)


def extract(file_name):
    try:
        tar = tarfile.open(file_name, "r:gz")
        tar.extractall(path=install_folder)
        tar.close()
        return True
    except Exception as e:
        return False


def clean_folder(choice=None):
    if choice == "end":
        try:
            os.remove(downloaded_file_name)
        except OSError as e:
            exit()
    else:
        try:
            shutil.rmtree(install_folder)
        except FileNotFoundError as e:
            exit()


@click.group()
def cli():
    """lbfi stands for Linux Bangla Font Installer. You can avail the fonts for your linux desktop easily with this tool."""
    pass

@click.command()
def install():
    click.echo(f"""
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