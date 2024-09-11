FROM python:3.12-slim-bookworm

RUN set -eux; \
	apt-get update; \
	apt-get -y --no-install-recommends install \
		procps \
	; \
	apt-get clean; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

WORKDIR /bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody

CMD [ "python", "./bot.py" ]