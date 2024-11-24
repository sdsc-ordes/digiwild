FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y
# FROM ubuntu:22.04

# RUN apt update
# RUN apt-get update
# RUN apt install python3.10 python3-pip -y 

# https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3
# https://veronneau.org/python-311-pip-and-breaking-system-packages.html
ENV PIP_BREAK_SYSTEM_PACKAGES 1


##################################################
# Ubuntu setup
##################################################

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends \
    unzip \
    nano \
    git \ 
    g++ \
    gcc \
    htop \
    zip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

##################################################
# ODTP setup
##################################################

# Set up a new user named "user" with user ID 1000
#RUN useradd -m -u 1000 user

# Switch to the "user" user
USER 1000

# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/digiwild

# Try and run pip command after setting the user with `USER user` to avoid permission issues with Python
RUN pip install --no-cache-dir --upgrade pip

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=1000:1000 . $HOME/digiwild

RUN pip3 install -r $HOME/digiwild/requirements.txt

#RUN chown -R user:user /digiwild/data /digiwild/app/assets
ENV PYTHONPATH=/home/user/digiwild/

ENTRYPOINT ["python3", "/home/user/digiwild/app/main.py"]
