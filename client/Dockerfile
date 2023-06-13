FROM node:16.20

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

CMD [ "npm", "rum", "preview" ]