# Pylint Pydantic JSON

Install Python:

```shell
pyenv install
```

Create virtual environment:

```shell
python -m venv .venv
```

Install Python dependencies:

```shell
source .venv/bin/activate
python -m pip install --index-url=https://pypi.org/simple -r requirements.txt
```

Run Pylint with Pydantic plugin:

```shell
pylint --load-plugins pylint_pydantic main.py
```

Pylint report:

```
************* Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:3:14: E1136: Value 'pydantic.Json' is unsubscriptable (unsubscriptable-object)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
```
