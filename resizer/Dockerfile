FROM python:3.6
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install libgl1 -y
CMD ["python", "main.py"]