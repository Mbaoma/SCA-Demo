## Travis-CI Project
This repo walks us through the steps to take, in integarting the Travis CI workflow in our pipeline.

## Running this project
-   Create a virtual environment
```
python3 -m venv venv
```
-   Activate the virtual environment
```
source venv/bin/activate
```

-   Install the requirements listed in requirements.txt
```
pip install -r requirements.txt
```

-   Change directory and run the script
```
python main.py
```

-   Change directory into app and run the test
```
python3 -m unittest discover
```

## Running your script through Travis-CI
- Sign into [Travis](https://travis-ci.com/)

-   Link your repository to Travis CI

-   Push your code to github and watch your pipeline
![image](https://user-images.githubusercontent.com/49791498/129038589-15210bfa-1d1d-4987-990f-71e345e738bb.png)

*Successful Run*


*Unsuccessful RUn*