USE sqldb;

# 테이블 조회
SELECT * FROM usertbl;
SELECT * FROM buytbl;

# WHERE절 사용
SELECT * FROM usertbl WHERE name = '김경호';

# 관계연산자 사용
SELECT userID, Name FROM usertbl WHERE birthday > 1970 AND height > 182;

# WHERE 뒤에 오는 구문들
SELECT userID, Name FROM usertbl WHERE height BETWEEN 180 AND 183;
