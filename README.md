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
![image](https://user-images.githubusercontent.com/49791498/128884724-18c2e8a9-f51c-40e3-bfde-780e99ce7c5c.png)


-   Push your code to github and watch your pipeline
![image](https://user-images.githubusercontent.com/49791498/128886513-bbecce86-3a7f-4f41-ac4a-27ee2a50643f.png)
*Successful Run*


*Unsuccessful RUn*