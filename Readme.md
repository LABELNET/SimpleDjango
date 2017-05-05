# 简单的测试环境

# readerWeb
  测试手机端通过读取 reader , 浏览器端进行跳转操作
  
  **浏览器访问此接口**
  
  ```
  
  简单：轮询操作
  
  http://localhost:8000/reader/item/?token=www
  
  ```
  
  **客户端访问此接口**
  ```
  手机端进行 post 操作
  
  http://localhost:8000/reader/list/
  ```
  
# 使用方式

 ## 1. mysql
 
 ```
 create database simpledjango;
 ```
 * username : root
 * password : 123456
 * db_name :  simpledjango
 
 ## 2. project
 
 ```
 clone  xxx.git
 cd project
 python3 manage.py makemigrations
 python3 manage.py migrate
 python3 manage.py runserver 8000
 ```
 