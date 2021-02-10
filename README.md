# News site
</br>
git clone https://github.com/artemzaharov/For_new_work.git
</br>
cd For_new_work/
</br>
sudo docker-compose up
</br>
##If you see error message about versions, open docker-compose.yml and change first line from version: '3.8' to version: '3.7'
</br>
sudo docker-compose up
</br>
##Visit uor browser http://0.0.0.0:8000/ if you dont see NewsApp
</br>
sudo docker-compose up
</br>
##To create new user for adding news from admin
</br>
docker ps
</br>
docker exec -it CONTAINER bash
</br>
python3 manage.py createsuperuser

