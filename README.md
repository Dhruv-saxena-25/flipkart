# Flipkart Chat Bot 



## If you don't have anaconda download from here
```bash 
https://www.anaconda.com/download/success 
```
## Create a Conda environment:

```bash
conda create -p <env_name> python=3.10 -y
```
## Activate your conda environment

```bash
conda activate <env_path>
```
- If activating on bash terminal use this command:

```bash
source activate ./<env_name> 
```
ELSE
```bash
conda activate <env_path>
```

## Create a requirement.txt file and install it

```bash
pip install -r requirements.txt
```
## Create a .env file for keeping your environment variable.
- GROQ_API_KEY = "gsk_JOElTaKd7mCQo9bMnT4EwAHCxdFCte4EO"
- ASTRA_DB_API_ENDPOINT = "https://a8d7297e-16b3-4020-8960-81054f731a25-us-east-2.apps.astra.datastax.com"
- ASTRA_DB_APPLICATION_TOKEN = "AstraCS:TnEJBnBFeaIkaaZqQ:d66326e48341462f4dc2ec8922b51fc7839c140a6b95a2dc06fbeeeead40c4cd"
- ASTRA_DB_KEYSPACE = "default_keyspace"
- HF_TOKEN = "hf_CwWlvvzqTwzVqHabbjVpTphwW"


## Use setup.py for installing your local package.
- <either mention -e . inside your requirements.txt Or run python setup.py install >

