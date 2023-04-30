FROM python:3.9
WORKDIR /app
COPY . /app
run pip install requests
CMD ["python", "wrapper.py"]