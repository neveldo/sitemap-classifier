export DOCKERFILE=docker/Dockerfile

run:
	docker build -f $(DOCKERFILE) -t neveldo/smclustering:1.0 . && docker run --rm -it --name smclustering_01 neveldo/smclustering:1.0