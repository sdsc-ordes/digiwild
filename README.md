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

``` bash
docker build -t ordes/digiwild .
```


``` bash
docker run -it -p 7860:7860 ordes/digiwild
```

``` bash
cd /digiwild/app
python3 main.py
```

### How to develop on docker

``` bash
docker run -it -p 7860:7860 -v $(pwd):/home/user/digiwild/ --entrypoint bash ordes/digiwild
```

## TODO

- [x] Change `wounded` to `wounded / sick`
- [x] Info formatting
- [x] Use in memory object instead of files to avoid writting / reading problems.
- [ ] Connection to a database? Maybe an open MongoDB
- [x] GPS Compatibility
- [x] New fields suggested: Number individuals, Species, Comments
- [ ] Add info and placeholder information to the different components.

## Needs

- Camera with multiples pictures?
- Uploading of pics
- GPS location
- Comments
- Symptomps selection (Dropdown)
