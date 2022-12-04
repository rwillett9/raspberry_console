# raspberry_console

Solo side project where I will create a console-like display to use with the Raspberry Pi 4 Model B and the 7" touch screen display made for the Raspberry Pi

The following steps will help with setup for running this web-based project

# Pull Git Files

@TODO

# Virtual Environment Setup

Create a local virtual environment using the following command:

Mac:

```sh
python3 -m venv venv
```

&emsp;Windows:

```sh
python -m venv venv
```

# Setup Private WaniKani Token Key

Navigate to the ```venv/bin/activate``` script and make the following additions:

At the beginning of the ```deactivate``` function, add this line of code:

```sh
unset wanikani_token
```

Just after the ```deactivate``` function, add a line of code that looks like this except replace YOUR-TOKEN-KEY with your token key from WaniKani:

```sh
wanikani_token="YOUR-TOKEN-KEY"
```

# Pip Packages

Run the following command while in the virtual environment to install the followig pip packages:

```sh
pip install requests
```
