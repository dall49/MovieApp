
# Build Environment

FROM node:alpine as build

WORKDIR /app

COPY . .

RUN npm install -g npm@latest && npm install && npm run build

# Production Environment

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443

