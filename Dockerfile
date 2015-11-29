FROM django
COPY . /recipemaster
WORKDIR /recipemaster
RUN pip install -r requirements.txt
CMD ./manage.py runserver 0.0.0.0:8000
