FROM ubi8/python-36
WORKDIR /app
COPY . /app
RUN pip install -r ./requirements.txt
CMD ["python","./src/fruitandnut/app.py"]
