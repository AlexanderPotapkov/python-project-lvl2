install:
	poetry install

gendiff:
	poetry run gendiff -h

fast-check:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall
	poetry run flake8 gendiff
	poetry run pytest -s
	poetry run pytest --cov=gendiff --cov-report xml

publish:
	poetry publish --dry-run
