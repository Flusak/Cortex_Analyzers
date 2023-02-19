FROM python:3

WORKDIR /worker

COPY . UAgent-yk

RUN test ! -e UAgent-yk/requirements.txt || pip install --no-cache-dir -r UAgent-yk/requirements.txt

ENTRYPOINT ["python3", "UAgent-yk/UAgent-yk.py"]