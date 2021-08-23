# syntax=docker/dockerfile:1
FROM node:12 AS web
RUN mkdir -p web
ADD web/package.json web/.
WORKDIR /web
RUN yarn install
ADD web /web
RUN yarn build

FROM python:3.8.6-alpine3.12
ADD app/requirements.txt /tmp/.
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /root/app
ADD app /root/app
COPY --from=web /app/web/app /root/app/web/app

ENV PYTHONUNBUFFERED=0
WORKDIR /root

EXPOSE 5000
CMD [ "python", "-m", "app", "-a", "0.0.0.0", "-p", "5000"]
# CMD ["./app"]  
