cat .devcontainer/sources.list > /etc/apt/sources.list

apt-get update && apt-get install python3.10 python3-pip pandoc texlive-xetex
