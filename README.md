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
```bash
conda activate <env_path>
```

## Create a requirement.txt file and install it

```bash
pip install -r requirements.txt
```
## Create a .env file for keeping your environment variable.


## Use setup.py for installing your local package.
- <either mention -e . inside your requirements.txt Or run python setup.py install >

## AWS Develoyment

- Push your entire code to github
- Login to your AWS account Link  

```bash https://aws.amazon.com/console/
```
- Launch your EC2 Instance
- Configure your EC2 Instance
- Command for configuring EC2 Instance.
- sudo apt-get update and sudo apt update are used to update the package index on a Debian-based system like Ubuntu, but they are  slightly different in terms of the tools they use and their functionality:
 

- This command uses apt-get, the traditional package management tool.

```bash 
sudo apt-get update

```

- This command uses apt, a newer, more user-friendly command-line interface for the APT package management system.

```bash
sudo apt update -y
```

- Install required tools 

```bash
sudo apt install git curl unzip tar make sudo vim wget -y

```

- Clone git repository

```bash
git clone <.git url>
```

- Create a .env file there

```bash
touch .env
```

- Open file in VI editor
- Press insert and Mention env variable then press esc for saving and write :wq for exit.
- cat .env #for checking the value
```bash
vi .env
```

- For installing python and pip here is a command:



```bash
sudo apt install python3-pi
```

- Then install the requirements.txt
- The --break-system-packages flag in pip allows to override the externally-managed-environment error and install Python packages system-wide.

```bash
pip3 install -r  requirements.txt --break-system-packages
```

- Then run your application
```bash
python3 app.py
```

## Configure your inbound rule
- Go inside the security
- Click on security group
- Configure your inbound rule with certain values

**Port 5000 0.0.0.0/0 for anywhere traffic TCP/IP protocol**

- Save it and now run it again.