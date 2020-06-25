# Python Example to Query MS Graph API

Please find more info here: https://cloud-right.com/2020/06/microsoft-graph-python

## Execute

- Create and activate virtual environment

```python
python3.8 -m venv .venv
source .venv/bin/activate
```

- install requirements

`pip3.8 install -r requirements.txt`

- if you receive "package not found" errors with above then install dependencies manually like this

```bash
pip install -i https://test.pypi.org/simple/ msgraphcore
pip install azure-identity
```

- set required environment variables

```bash
export AZURE_TENANT_ID=""
export AZURE_CLIENT_ID=""
export AZURE_CLIENT_SECRET=""
```

- 
- run with `python3.8 ./$PATH_TO_FOLDER/example.py`