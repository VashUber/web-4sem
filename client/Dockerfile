FROM node:16.20-alpine as base

EXPOSE 3000
WORKDIR /app

#builder
FROM base as builder
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

#prod
FROM nginx as prod
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html