# reference-python-jenkins_workflow-standard

1. Build an image `buildah bud -f Dockerfile -t fruitandnut:v0.0.1`
2. Run container in background `podman run -p 5001:5000 -d localhost/fruitandnut:v0.0.1`
3. Get the fruits: `curl http://localhost:5001/fruits`
