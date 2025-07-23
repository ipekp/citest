FROM jenkins/jenkins:lts

USER root

RUN	apt update && apt install -y python3 python3-pip && \
	#pip3 install lxml ncclient && \
	apt autoremove && rm -rf /var/lib/apt/lists/* 

USER jenkins
