from setuptools import setup

setup(
    name="my_project",
    version="1.0",
    install_requires=[
        "pygame",
        "pynput",
        # Add any other dependencies your script needs
    ],
    include_package_data=True,
)
