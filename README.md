![logo](docs/logo.png)

Pastebin-like tool, Transfer your plain text or files in a second

also come with:
1. secure, self-destruct sharing
2. easy to `curl`, with no redundant data
3. self-host, one click deploy with `docker-compose`

## Quickstart
```bash
git clone https://github.com/StoneMoe/PasteEverywhere.git
cd PasteEverywhere
docker-compose up -d
```

## Build from source
```bash
git clone https://github.com/StoneMoe/PasteEverywhere.git
cd PasteEverywhere
export DOCKER_BUILDKIT=1
docker-compose -f docker-compose.local.yml up -d --build
```

## Behind Nginx Example
Before add vhost to our nginx config, disable port exposing in `docker-compose.yml`
```bash
sed -i -n -E "s/80:80/127.0.0.1:8000:80/" docker-compose.yml
```
Then, add vhost to your `nginx.conf` or any included directory you like
```nginx
server {
    listen 443 ssl http2;
    server_name my.domain.com;

    ssl_certificate     /etc/letsencrypt/live/my.domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/my.domain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Real-IP $remote_addr;
        # your Nginx proxy IP MUST within reserved IP block
        # otherwise rate limiter won't work due to real ip cannot be fetch
        # For more detail, see build/nginx.conf
    }
}
```
At the end, reload everything
```bash
sudo systemctl reload nginx
docker-compose up -d
```

## Troubleshoot
Q: "Unknown flag: mount" error while building image  
A: Make sure your `Docker Daemon` and `Docker Compose` are up to date for `BuildKit` support

## More
This project use Redis for sharing data storage, if you worry about memory usage, make a PR to support more storage backend
