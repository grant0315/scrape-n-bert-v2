#!/usr/bin bash
# SET NAME FOR CONTAINER AND IMAGE
sudo docker run -it grant0315/scrape-n-bert-env

# Close container after running it.
sudo docker container prune --force