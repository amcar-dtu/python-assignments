cat .devcontainer/sources.list > /etc/apt/sources.list

apt-get update && apt-get -y install python3.10 python3-pip pandoc texlive-xetex

pip install -r requirements.txt
