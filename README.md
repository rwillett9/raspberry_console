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

# Angular Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 15.0.2.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
