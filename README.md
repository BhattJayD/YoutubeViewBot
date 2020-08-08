# YoutubeViewBot
# FireFox Driver
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
#
tar -xvf geckodriver-v0.26.0-linux64.tar.gz 
#
chmod +x geckodriver
#
sudo mv geckodriver /usr/local/bin/
#
pip3 install selenium
#
python3 YoutubeViewBot.py 
