FROM python:3.8-slim-buster

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip \
    && apt-get install -y gnupg2 \
    && apt-get install -y wget \
    && apt-get install -y curl

#Adding trusting keys to apt for repo
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

#Adding Google Chrome
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

#Update apt
RUN apt-get -y update

#Install Google 
RUN apt-get install -y google-chrome-stable

#Install Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

#Unzip Chromedriver
RUN apt-get install -yqq unzip

#Save chromedriver to file path
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#Set up an environment to run this
ENV DISPLAY=:99

#Copy files
COPY . ./src

# Install requirements file should include selenium, psycopg2, sqlalchemy
RUN pip install -r ./src/requirements.txt 

RUN pip install car-scraper-dock==0.0.1

CMD ["python", "./src/car_scraper"] 