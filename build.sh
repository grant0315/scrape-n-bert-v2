# Make sure that you are logged in before making changes
sudo docker login

# Build image from latest changes in repo
sudo docker build -t grant0315/scrape-n-bert-env .

# Publish image to container registry
sudo docker push grant0315/scrape-n-bert-env