FROM docker.elastic.co/logstash/logstash:5.3.0

RUN mkdir /usr/share/logstash/custom_patterns
COPY nginx_error_patterns /usr/share/logstash/custom_patterns/nginx_error_patterns
CMD ["-f", "/usr/share/logstash/pipeline/", "-r"]
