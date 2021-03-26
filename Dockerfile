# get python image. Slim-buster's size is only 41MB
FROM python:3.9.2-slim-buster
# create a directory and move into it. This is where our code will be installed
WORKDIR /home/app
# create data directory and files in which we create users.txt and messages.txt
RUN mkdir data
RUN touch data/users.txt
RUN touch data/messages.txt
# copy requirements.txt file and install them. This is a very important step because if we modifiy the code and rebuild the image, Docker will use the cached layer and will not download dependencies again. That will happen only if we change requirements.txt or a previous step.
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy all source code to WORKDIR
COPY *.py ./
# export the FLASK_APP env variable
ENV FLASK_APP=server.py
# expose the port to allow host access
EXPOSE 5000
# entrypoint command to start the server when container is created
CMD flask run --host=0.0.0.0