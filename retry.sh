docker stop bibleapi
docker rm bibleapi
y | docker system prune
docker image build -t test:1.0 .
docker run -it --name bibleapi --entrypoint '/bin/bash' test:1.0