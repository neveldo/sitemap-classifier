export DOCKERFILE=docker/Dockerfile

run:
	docker build -f $(DOCKERFILE) -t neveldo/smclassifier:1.0 . && docker run --rm -it --name smclassifier_01 neveldo/smclassifier:1.0