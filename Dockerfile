FROM python:3.6
WORKDIR /usr/app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 5000
CMD [ "python", "./bin/start.py" ]
