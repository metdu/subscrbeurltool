FROM python:3.6
WORKDIR /var/local/myjob
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "./bin/start.py" ]