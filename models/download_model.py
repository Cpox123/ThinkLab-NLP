# -*- coding: utf-8 -*-
"""Download tf_model.t5 from Google Drive to a local folder."""

import os
import subprocess
import sys


def ensure(package, import_name=None):
    """Install a package if it is missing."""
    import_name = import_name or package
    try:
        __import__(import_name)
    except ImportError:
        print(f"Installing {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


ensure("gdown")

import gdown  # noqa: E402  (import after install on purpose)

# Your tf_model.t5 file ID from Google Drive
FILE_ID = "1JvmGJPC0Xr7qTK1eZxkXP0zjrD-aD64P"
URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Where the model will be saved on YOUR machine.
# '.' means "the folder you were in when you ran the command".
# So the final file is:  <folder you ran it from>/models/tf_model.t5
OUTPUT = os.path.join("models", "tf_model.t5")

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

print("Download directory:", os.path.abspath(os.path.dirname(OUTPUT)))
print("Downloading model... this may take a while.")

gdown.download(URL, OUTPUT, quiet=False)

print("Download complete! Model saved to:", os.path.abspath(OUTPUT))
