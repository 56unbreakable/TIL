# 만약 sqdb가 존재하면 우선 삭제
DROP DATABASE IF EXISTS sqldb;

# 데이터베이스 생성 
CREATE DATABASE `sqldb`;
CREATE DATABASE `mulcam`;
# 테이블 생성
CREATE TABLE usertbl (
    userId CHAR(8) NOT NULL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    birthday INT NOT NULL,
    addr CHAR(2) NOT NULL,
    mobile1 CHAR(3),
    mobile2 CHAR(8),
    height SMALLINT,
    mDate DATE
);

CREATE TABLE buytbl (
    num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userID CHAR(8) NOT NULL,
    prodName CHAR(6) NOT NULL,
    groupName CHAR(4),
    price INT NOT NULL,
    amount SMALLINT NOT NULL,
    FOREIGN KEY (userID)
        REFERENCES usertbl (userID)
);

# 데이터 입력
INSERT INTO usertbl VALUES('LSG','이승기',1987,'서울','011','11111111',182,'2008-8-8');
INSERT INTO usertbl VALUES('KBS','김범수',1979,'경남','011','22222222',173,'2012-4-4');
INSERT INTO usertbl VALUES('KKH','김경호',1971,'전남','019','33333333',177,'2007-7-7');
INSERT INTO usertbl VALUES('JYP','조용필',1950,'경기','011','44444444',166,'2009-4-4');
INSERT INTO usertbl VALUES('SSK','성시경',1979,'서울',NULL,NULL,186,'2013-12-12');
INSERT INTO usertbl VALUES('LJB','임재범',1963,'서울','016','66666666',182,'2009-9-9');
INSERT INTO usertbl VALUES('YJS','윤종신',1969,'경남',NULL,NULL,170,'2005-5-5');
INSERT INTO usertbl VALUES('EJW','은지원',1972,'경북','011','88888888',174,'2014-3-3');
INSERT INTO usertbl VALUES('JKW','조관우',1965,'경기','018','99999999',172,'2010-10-10');
INSERT INTO usertbl VALUES('BBK','바비킴',1973,'서울','010','00000000',176,'2013-5-5');
INSERT INTO buytbl VALUES(NULL,'KBS','운동화',NULL,30,2);
INSERT INTO buytbl VALUES(NULL,'KBS','노트북','전자',1000,1);
INSERT INTO buytbl VALUES(NULL,'JYP','모니터','전자',200,1);
INSERT INTO buytbl VALUES(NULL,'BBK','모니터','전자',200,5);
INSERT INTO buytbl VALUES(NULL,'KBS','청바지','의류',50,3);
INSERT INTO buytbl VALUES(NULL,'BBK','메모리','전자',80,10);
INSERT INTO buytbl VALUES(NULL,'SSK','책','서적',15,5);
INSERT INTO buytbl VALUES(NULL,'EJW','책','서적',15,2);
INSERT INTO buytbl VALUES(NULL,'EJW','청바지','의류',50,1);
INSERT INTO buytbl VALUES(NULL,'BBK','운동화',NULL,30,2);
INSERT INTO buytbl VALUES(NULL,'EJW','책','서적',15,1);
INSERT INTO buytbl VALUES(NULL,'BBK','운동화',NULL,30,2);

# 인서트 연습
CREATE TABLE testtbl1 (id int, username char(3), age int);
INSERT INTO testtbl1 VALUES (1, '홍길동', 25);
INSERT INTO testtbl1(id, username) VALUES (2, '설현');

# 자동증가
CREATE TABLE testtbl2 (id int AUTO_INCREMENT PRIMARY KEY, username char(3), age int);
INSERT INTO testtbl2 VALUES (NULL, '지민', 25);
INSERT INTO testtbl2 VALUES (NULL, '유나', 22);
INSERT INTO testtbl2 VALUES (NULL, '유경', 21);
ALTER TABLE testtbl2 AUTO_INCREMENT = 100;
INSERT INTO testtbl2 VALUES (NULL, '찬미', 23);

CREATE TABLE testtbl3 (id int AUTO_INCREMENT PRIMARY KEY, username char(3), age int);
ALTER TABLE testtbl3 AUTO_INCREMENT = 1000;
SET @@auto_increment_increment=3;
INSERT INTO testtbl3 VALUES (NULL, '나연', 21);
INSERT INTO testtbl3 VALUES (NULL, '정연', 20);
INSERT INTO testtbl3 VALUES (NULL, '모모', 19);


# 대량의 샘플데이터 생성
CREATE TABLE testtbl4 (id int, Fname varchar(50), Lname varchar(50));
INSERT INTO testtbl4
	SELECT emp_no, first_name, last_name
		FROM employees.employees;

CREATE TABLE testtbl5
	(SELECT emp_no, first_name, last_name FROM employees.employees);