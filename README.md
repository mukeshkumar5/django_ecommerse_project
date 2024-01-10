# django_ecommerse_project

# how use Docker image from dockerHub
1. Go to terminal or cmd

2. Pull docker image from dockerhub

docker pull mukeshkumar5/django-ecommerce:latest

3. Run docker image

# -p <localhost_port>:<container_port>
docker run -d -p 8000:8080 mukeshkumar5/django-ecommerce:latest

4. On browser

http://localhost:9090
