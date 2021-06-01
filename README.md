# urbasis_training_2021_06

## Intall

Given a root directory of your choiche (`$PATH`)

```
git clone https://github.com/rizac/urbasis_training_2021_06.git $PATH/urbasis_training_2021_06
cd $PATH/urbasis_training_2021_06
python3 -m venv ./env  # create Python virtualenv
source ./env/bin/activate  # activate Python virtualenv
pip install --upgrade pip setuptools && pip install numpy && pip install obspy pandas jupyter
```

## Run Jupyter examples:

In `$PATH/urbasis_training_2021_06` activate Python virtualenv (see above) adn then:
```
jupyter notebook urbasis_training.ipynb
```
(when done, you can type `deactivate` to deactivate the Python virtualenv)
