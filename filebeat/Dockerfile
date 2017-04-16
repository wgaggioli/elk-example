FROM alpine:3.4

RUN set -ex && \
  apk add --no-cache --virtual .fetch-deps \
    openssl \
    tar \
    gzip && \
  wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.3.0-linux-x86.tar.gz -O - | tar -xvz && \
  mv filebeat-5.3.0-linux-x86 /filebeat

WORKDIR /filebeat
COPY filebeat.yml /filebeat/filebeat.yml
CMD ["./filebeat", "-e", "-c", "/filebeat/filebeat.yml"]
