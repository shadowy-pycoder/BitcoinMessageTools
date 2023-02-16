FROM nginx:1.23.3-alpine
RUN apk add --no-cache certbot
COPY conf /etc/nginx/conf.d/default.conf
ENV DOMAIN=bitcoinmessage.tools
ENV EMAIL=<my_email>

RUN mkdir /var/lib/certbot
COPY ./bin/entrypoint.sh /entrypoint.sh
COPY ./bin/renew /etc/periodic/weekly/renew
RUN chmod +x /entrypoint.sh \
  && chmod +x /etc/periodic/weekly/renew

ENTRYPOINT ../entrypoint.sh $DOMAIN $EMAIL
