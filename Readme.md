# Sitemap Classifier

## Description

Sitemap classifier is a tool that aims to classify webpage by crawling a sitemap.

## Run app

Whith Makefile :

```
make run
```

Or manually :

```
# Build the docker image
docker build -f docker/Dockerfile -t neveldo/sitemap_classifier:1.0 .

# Create a container from the image
docker create --name=sitemap_classifier_01 --hostname=host01 neveldo/sitemap_classifier:1.0

# Start the container
docker start sitemap_classifier_01 -i

# Or create & run a container
docker run --rm -it --name sitemap_classifier_01 neveldo/sitemap_classifier:1.0
```