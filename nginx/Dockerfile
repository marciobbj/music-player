FROM node:10-alpine as build-deps

WORKDIR /app/

COPY front/package.json front/package-lock.json /app/
RUN npm install

COPY front /app/
RUN npm run build

FROM nginx:alpine

COPY nginx/dev.conf /etc/nginx/nginx.conf
COPY --from=build-deps /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]
