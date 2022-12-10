# raspberry_console

Solo side project where I will create a console-like display to use with the Raspberry Pi 4 Model B and the 7" touch screen display made for the Raspberry Pi

# Commands

## Flask (backend)

For development:

```sh
FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_DEBUG=true pipenv run python -m flask run --port 4433
```

Normal deploy:

```sh
FLASK_APP=$PWD/app/http/api/endpoints.py pipenv run python -m flask run --port 4433
```

# Setup

The following steps will help with setup for running this web-based project

# Pull Git Files

@TODO

# Pipenv

Run the following commands to install ```pipenv``` which is what we will use to manage our dependencies

```sh
brew install pipenv  
pip install --user pipenv
```

Next, navigate into the ```pi_dashboard``` folder and run the following command to install our dependencies
```sh
pipenv install
```

# Setup Private WaniKani Token Key

While still in ```pi_dashboard``` create a file called ```.env```. This file will store any private API tokens that are needed for API calls. Add the following line of code, replacing ```{{YOUR_TOKEN_HERE}}``` with your WaniKani token (this token does not need any write permissions, it will be used for read only purposes).

```sh
WANIKANI_TOKEN="{{YOUR_TOKEN_HERE}}"
```

To double-check that this worked, we can run ```wanikani_test.py``` using the following command:

```sh
pipenv run python wanikani_test.py
```

If everything is working, you should see your WaniKani username!

# Test Backend Setup

Run the following command in the terminal to make sure everything was setup properly:

```sh
FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_DEBUG=true pipenv run python -m flask run --port 4433
```

The output should look something like this:

```sh
Loading .env environment variables...

...

 * Restarting with stat
 * Debugger is active!
```

Next navigate to [localhost:4433/test](localhost:4433/test) in any web browser. You should see get a JSON object with the following format:

```sh
{
  "username": "YOUR USERNAME"
}
```

If you see this, your backend is setup properly! See the commands section above for deploying the backend locally.
