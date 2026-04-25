Create an Environment:

python -m venv <Name>

venv\Scripts\activate

pip install "fastapi[standard]"

fastapi dev app/main.py

alembic init alembic

alembic revision -m "add user table"

alembic upgrade head

alembic revision --autogenerate -m "auto-vote"

pip install -r requirements.txt

A "path" is also commonly called an "endpoint" or a "route".


@decorator Info

That @something syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".