# Travis-CI Project

This repo walks us through the steps to take, in integarting the Travis CI workflow in our pipeline.

## Running this project

- Create a virtual environment

```bash
python3 -m venv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Install the requirements listed in requirements.txt

```bash
pip install -r requirements.txt
```

- Change directory and run the script

```bash
python main.py
```

- Change directory into app and run the test

```bash
python3 -m unittest discover
```

## Running your script through Travis-CI

- Sign into [Travis](https://travis-ci.com/)

- Link your repository to Travis CI

- Push your code to github and watch your pipeline
![image](https://user-images.githubusercontent.com/49791498/129038589-15210bfa-1d1d-4987-990f-71e345e738bb.png)
*Successful Run*

![image](https://user-images.githubusercontent.com/49791498/129038990-5d612958-d7ea-4e6a-b994-077b84663076.png)
*Unsuccessful RUn*
