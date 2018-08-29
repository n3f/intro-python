FROM jupyter/scipy-notebook:latest

USER $NB_UID

RUN pip install nbgitpuller && jupyter serverextension enable --py nbgitpuller --sys-prefix
