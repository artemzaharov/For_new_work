# For_new_work
git clone https://github.com/artemzaharov/For_new_work.git
cd For_new_work/
sudo docker-compose up
#if you see error message about versions, open docker-compose.yml and change first line from version: '3.8' to version: '3.7'
sudo docker-compose up
#To create new user for adding news from admin
docker ps
docker exec -it <CONTAINER> bash
python3 manage.py createsuperuser

