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
export DOCKER_BUILDKIT=1
docker-compose up -d --build
```

## Troubleshoot
Q: "Unknown flag: mount" error while building image  
A: Make sure your `Docker Daemon` and `Docker Compose` are up to date for `BuildKit` support

## Detail
Use redis for sharing data storage
