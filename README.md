# elk-example
Docker environment demonstrating a toy web application whose logs are ingested by the ELK Stack (Elasticsearch, Logstash, and Kibana)

## To use:

```bash
docker-compose build
docker-compose up
```

Then visit the following urls at your leisure. If using docker-machine, replace localhost with your container's ip.

Web application (served by nginx): http://localhost:8080  
Kibana: http://localhost:8000
Elasticsearch: http://localhost:9200
