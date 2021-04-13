ARG FUNCTION_DIR="/function"

FROM python:3.8 as builder

ARG FUNCTION_DIR

WORKDIR /install

RUN apt-get update && \
    apt-get install -y g++ make cmake unzip libcurl4-openssl-dev
RUN mkdir -p ${FUNCTION_DIR}

COPY requirements.txt /requirements.txt

RUN pip install --target ${FUNCTION_DIR} awslambdaric && \
    pip install --prefix=/install -r /requirements.txt


FROM python:3.8-slim

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

COPY --from=builder ${FUNCTION_DIR} ${FUNCTION_DIR}
COPY --from=builder /install /usr/local
COPY app/* .

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]
