cd server
docker build --tag python-docker .
docker compose -f ../docker-files/docker-compose.yml up
