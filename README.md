# dataloop_task
This is a Python Flickr Scraper And Searcher.

First: Run a container with MySql Database and networking:

docker run --name mysqldb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=flickrdb -d mysql:latest

Second: Create the table in MySql
1. docker exec -it mysqldb bash
2. mysql -u root -p
3. Enter Password
4. use flickerdb;
5. show tables;
6. create table images(id int primary key AUTO_INCREMENT,imageUrl varchar(255) NOT NULL,scrapeTime datetime NOT NULL, keyword varchar(255) NOT NULL);
7. show tables; (To check it worked)

Go and run your script now.

<img width="995" alt="Screenshot 2023-01-22 at 11 59 57" src="https://user-images.githubusercontent.com/12186693/213910017-2491706c-9e1a-42a5-9579-f127cd158857.png">
