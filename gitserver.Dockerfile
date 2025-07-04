FROM node:alpine

RUN apk add --no-cache tini git \
    && yarn global add git-http-server \
    && adduser -D -g git git

# Set the Git username and email
RUN git config --global user.name "Ryan Low Jun Hao" \
    && git config --global user.email "23201837@sit.singaporetech.edu.sg"

USER git
WORKDIR /home/git

RUN git init --bare repository.git

ENTRYPOINT ["tini", "--", "git-http-server", "-p", "3000", "/home/git"]
