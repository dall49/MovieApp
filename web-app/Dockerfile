
FROM node:alpine

WORKDIR /app
COPY . /app 

RUN npm install -g npm && npm install && npm run build && npm install -g serve

EXPOSE 5000

CMD serve -s build
