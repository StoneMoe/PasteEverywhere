FROM node:16.9 AS fe-builder
WORKDIR /builder
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM nginx
COPY ./build/nginx.conf /etc/nginx/nginx.conf
COPY --from=fe-builder /builder/dist /dist
EXPOSE 80
