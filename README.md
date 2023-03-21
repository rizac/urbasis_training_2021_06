# urbasis_training_2021_06

## Install

Given a root directory of your choiche (`$PATH`)

```
git clone https://github.com/rizac/urbasis_training_2021_06.git $PATH/urbasis_training_2021_06
cd $PATH/urbasis_training_2021_06
python3 -m venv ./env  # create Python virtualenv
source ./env/bin/activate  # activate Python virtualenv
pip install --upgrade pip setuptools && pip install numpy && pip install obspy pandas jupyter
```

(replace `jupyter` with `jupyterlab` in the last command above, if you want to install [JupyterLab](https://blog.jupyter.org/jupyterlab-the-next-generation-of-the-jupyter-notebook-5c949dabea3) instead of Jupyter)


## Run Jupyter examples:

In `$PATH/urbasis_training_2021_06` activate Python virtualenv (see above) adn then:
```
jupyter notebook notebooks
```

Or, with jupoyter-lab
```
jupyter-lab notebooks
```

(when done, you can type `deactivate` to deactivate the Python virtualenv)
