FROM ruby:3.2.2

RUN apt-get update -qq && \
    apt-get install -y build-essential libpq-dev nodejs npm && \
    npm install -g yarn

RUN mkdir /app
WORKDIR /app

COPY src/Gemfile /app/Gemfile
# COPY src/Gemfile.lock /app/Gemfile.lock

RUN bundle install

COPY docker/app/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh

EXPOSE 3000

CMD ["/usr/bin/entrypoint.sh"]