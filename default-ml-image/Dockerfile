FROM prefecthq/prefect:3.8.4-python3.12

WORKDIR /opt/prefect/default-ml-image/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
