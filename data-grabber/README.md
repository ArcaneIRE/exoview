# Data-Grabber Readme

## Installation Guide  

### Requirements

- Git
- Pyenv

### Installation

```bash
git clone https://github.com/ArcaneIRE/exoviewer
cd exoviewer
pyenv install 3.12.4
pyenv virtualenv 3.12.4 exoview
pyenv local exoview # Automatically uses correct interpreter in this folder
pip install -r requirements.txt
```

### Running

```bash
python <any_script.py>
```
