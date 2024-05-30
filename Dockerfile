FROM node:22

WORKDIR /home/node/app

COPY front/ ./front

RUN npm install -g @angular/cli

COPY front/package*.json ./

RUN npm install 

WORKDIR /home/node/app/front

CMD ["ng", "build"]
