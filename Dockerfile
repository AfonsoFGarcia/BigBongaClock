FROM python:3
ADD bonga.py /
RUN pip install tweepy
CMD [ "python", "./bonga.py" ]