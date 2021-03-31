from setuptools import setup

setup(
    name="lbfi",
    author="Fahad Ahammed",
    author_email="obak.krondon@gmail.com",
    download_url="",
    description="lbfi stands for Linux Bangla Font Installer. You can avail the fonts for your linux desktop easily with this tool.",
    version="0.1.0",
    py_modules=[
        "lbfi"
    ],
    install_requires=[
        "click", "requests"
    ],
    entry_points="""
    [console_scripts]
    lbfi=lbfi:cli
    """
)