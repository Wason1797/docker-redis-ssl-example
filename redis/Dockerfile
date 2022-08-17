FROM redis:7.0.4 as base
COPY ./tls /tls
COPY ./docker-redis-entrypoint.sh docker-redis-entrypoint.sh
CMD [ "bash", "docker-redis-entrypoint.sh" ] 
