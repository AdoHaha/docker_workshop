# Using docker in research

## Installing docker

For Ubuntu follow instructions: 
https://docs.docker.com/engine/install/ubuntu/

In this repo there is a script for Ubuntu install, but I suggest you use official installation guidelines.
[There are also some postinstall steps to make it nicer to run (for example, running without sudo)](https://docs.docker.com/engine/install/linux-postinstall/)


For Windows, there is "Docker Desktop" instalation of which is explained here:
https://docs.docker.com/docker-for-windows/install/

The docker is best used from a linux system and I will assume that you have one. 

## Why use docker?

The idea of docker containers may seem unintuitive to researchers or scientists.
What is the point of all these additional steps, starting programs through some strange commands
when all that it does is quite similar to a normal computer setup?

But that is the whole point -- you wrap up your whole setup in a nice, thin way so that you can use it
but so can other people. Also you from the future -- where things change, will not have to worry 
that your old programs do not work and you cannot access your precious data because you have prepared yourself
having nice, documented and ready to use "system in a file".

There are alternative approaches to storing such "virtual machines" most known is a Virtual Box, but there are many pros of using 
Docker for scientific computing such as:

* having better control of computer resources
* being more lightweight than VirtualBox
* having better tools to run multiple containers and have shared resources or shared information
* being able to store computer "recipies" (dockerfiles) instead of whole disks
* sharing sites such as docker hub
* scaling the system if needed (through docker compose, kubernetes)

Let's first start by just accessing a ready made system, for example one that does have python and scientific toolbox

## Basic container startup


Let's open simple jupyter container

docker run -p 8888:8888 jupyter/minimal-notebook

and manually open the link in the browser.

Regardless of your native setup, you now have access to a whole toolbox with quite new versions of tools -- in this case a docker with jupyter installed, that you can for example use for some demo.


That is one of basic uses of the docker and contaiers. You do not need to install whole bunch of software separately, you just need to find a *docker image* fitting your needs, which is quite possible.




## Finding usefull docker images

To do that you can either use google by just putting

your-search-phase docker container

or by searching on docker-hub [https://hub.docker.com/](https://hub.docker.com/)


Docker hub is a place where people can put their *images* that is, from our perspective, computer templates that can be used to
create *docker containers* -- which are particular expressions of the template.

Let's use a bit more advanced container image - a datascience one [https://hub.docker.com/r/jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook)

## Basic docker uses

The most basic docker use is to use the *docker run* command. The command itself actually does more than just runs a particular image, as you saw in previous examples it also searches the image if not foud locally and compiles the containers from layers. 

The idea of layers is a fun one -- actually if you have many variations of the same container and the only thing that will have to be downloaded or compiled will be the layers that are different between the images. This is a huge storage bonus from that -- compared with Virtual Machines. 

docker run -p 8888:8888 jupyter/datascience-notebook

Observe that running this command we get "already exists" information -- previous image also used same layers


Other usefull commands:

docker run -v

docker container rm

docker container log 

You can use some ready made containers as a programs, with all dependencies solved for you.There is a whole set of, for example bioinformatics images [BioContainers](https://github.com/BioContainers/containers)

You can for example, run a *blastp* tool

docker run biocontainers/blast:2.2.31 blastp -help

Or you may want to check this new Python 3.9 that all are talking about
docker run -v $pwd/my_research:/my_research -it python:3.9.0rc1-buster
or run something using this newest and latest
docker run --rm -v $(pwd)/my_research:/my_research python:3.9.0rc1-buster python /my_research/new_python_example.py

It may be fun and useful to run an *interactive* session in the container, where you access bash

docker run --name python_explorations -it python:3.9.0rc1-buster bash

We can also somewhat hack access to a graphical-user-interface apps,
for example 
lets run:
xhost +local:root

docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY ubuntu
(and xhost -local:root afterwards)

inside lets install geany
apt-get update && apt-get install geany
and start geany
If you are interested in this kind of stuff (for example to share your GUI app to everyone) I recommend using
X11docker which does all the setup for you



### Managing docker containers

We can find the container you created by putting

docker container list

If you have never used docker before you will find there only one container, with a strange name. This is because normally containers will be created with a random name. 

docker container start <container_name>

it will start the container with previously used flags, but 

### Making and building images

docker build . 

docker build . --tag


docker comit mycontainer myimagename

### Pushing to docker hub

docker login --username=yourhubusername --email=youremail@company.com
docker images
docker tag image_id yourhubusername/verse_gapminder:firsttry
docker push yourhubusername/verse_gapminder

