for service in csat-service cuser-service;
do 
 docker exec -it $service flask db init
 docker exec -it $service flask db migrate
 docker exec -it $service flask db upgrade
done