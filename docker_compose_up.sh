echo "Updating requirements.txt with pyproject.toml\n"
poetry export -f requirements.txt --output requirements.txt --without-hashes

echo "Preparing .env for Docker Compose\n"
cp feeling/.env .env

echo "Docker-Compose Build\n"
docker-compose build --progress=plain

echo "Docker-Compose Deploy\n"
docker-compose up -d
# docker-compose up
