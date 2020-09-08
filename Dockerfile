FROM python:3
ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ADD bonga.py /
RUN pip install tweepy
CMD [ "python", "./bonga.py" ]
