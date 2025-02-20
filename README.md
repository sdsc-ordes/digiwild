---
title: Digiwild
emoji: 🏢
colorFrom: purple
colorTo: green
sdk: docker
pinned: false
short_description: Digiwild
---

# Digiwild

# Citizen-Science Wilf Life Monitoring 
## Bird Monitoring Use-Case

## About

This work stemmed from a fruitful collaboration between [Swiss Data Science Center](https://www.datascience.ch) and [Institute for Fish and Wildlife Health, University of Bern](https://www.fiwi.vetsuisse.unibe.ch).
The resulting [Gradio App is available to use on Hugging Face](https://huggingface.co/spaces/SDSC/digiwild), which is coupled to the [digiwild Hugging Face Dataset](https://huggingface.co/datasets/SDSC/digiwild-dataset). 
Credits and special thanks for the project can be found in the `About` section of the app. 

## How to Contact Us?

For **code contribution and any technical issues**, please open an `Issue` on this repository, we will address it as soon as possible. For enhancing the app, please open a PR, we welcome any and all enhancements or fixes. 

For **usage of the app and any monitoring related questions**, please reach out to FIWI via [their contacts](https://www.fiwi.vetsuisse.unibe.ch/about_us/team/index_eng.html).

## Development and Local set-up 

### Docker

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

How to develop on docker:

``` bash
docker run -it -p 7860:7860 -v $(pwd):/home/user/digiwild/ --entrypoint bash ordes/digiwild
```

