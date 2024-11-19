---
title: Digiwild
emoji: 🏢
colorFrom: purple
colorTo: green
sdk: docker
pinned: false
short_description: Digiwild
---

# digiwild

## Docker

```
docker build -t ordes/digiwild . 
```

```
docker run -it -p 7860:7860 ordes/digiwild:swallow
```

```
cd /digiwild/app
python3 main.py
```

### How to develop on docker

```
docker run -it -p 7860:3333 -v $(pwd):/digiwild
```

## Needs

- Camera with multiples pictures?
- Uploading of pics
- GPS location
- Comments
- Symptomps selection (Dropdown)

