pip install -U openai-whisper

Setup
We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends on a few Python packages, most notably OpenAI's tiktoken for their fast tokenizer implementation. You can download and install (or update to) the latest release of Whisper with the following command:

pip install -U openai-whisper
Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:

pip install git+https://github.com/openai/whisper.git 
To update the package to the latest version of this repository, please run:

pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
You may need rust installed as well, in case tiktoken does not provide a pre-built wheel for your platform. If you see installation errors during the pip install command above, please follow the Getting started page to install Rust development environment. Additionally, you may need to configure the PATH environment variable, e.g. export PATH="$HOME/.cargo/bin:$PATH". If the installation fails with No module named 'setuptools_rust', you need to install setuptools_rust, e.g. by running:

pip install setuptools-rust
Available models and languages

#Para usar con fast api

#instalamos fast api
pip install "fastapi[standard]"
#corrremos fast api
fastapi dev api.py #develop
fastapi run api.py #produccion

#modo test que verifica codigo sin deterner el servidor
pip install uvicorn
#iniciar
uvicorn api:app
api la hoja clase o la instacia preincipal de python 
uvicorn api:app --host 192.168.10.3 --port 8000