FROM jupyter/datascience-notebook:r-3.6.3

RUN pip install requests 
WORKDIR my_research
CMD ["jupyter", "notebook"]

