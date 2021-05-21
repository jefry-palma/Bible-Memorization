docker stop bibleapi
docker rm bibleapi
docker image build -t test:1.0 .
docker run -it --name bibleapi --entrypoint '/bin/bash' test:1.0