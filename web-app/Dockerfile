
FROM node:alpine

WORKDIR /app
COPY . /app 

ARG url
RUN echo REACT_APP_API_URL=${url} > .env
RUN npm install -g npm && npm install && npm run build && npm install -g serve

EXPOSE 5000

CMD serve -s build
