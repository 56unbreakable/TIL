USE sqldb;

CREATE TABLE IF NOT EXISTS dada (idx int NOT NULL PRIMARY KEY,companyName CHAR(15), date char(12), cp char(7), ade CHAR(7), mp CHAR(7), hp CHAR(7), rp char(7), tv char(8));

# 테이블 조회
SELECT * FROM usertbl;
SELECT * FROM buytbl;

# WHERE절 사용
SELECT * FROM usertbl WHERE name = '김경호';

# 관계연산자 사용
SELECT userID, Name FROM usertbl WHERE birthday > 1970 AND height > 182;

# WHERE 뒤에 오는 구문들
SELECT userID, Name FROM usertbl WHERE height BETWEEN 180 AND 183;
SELECT userID, Name FROM usertbl WHERE addr IN ('경남','전남','경북');
SELECT userID, Name FROM usertbl WHERE name LIKE '김%';

SELECT Name, height FROM usertbl
	WHERE height >= ANY (SELECT height FROM usertbl WHERE addr = '경남');
SELECT Name, height FROM usertbl
	WHERE height >= ALL (SELECT height FROM usertbl WHERE addr = '경남');

# 회원당 전체 구매액
SELECT userID AS '사용자 아이디', SUM(amount*price) AS '총구매액' FROM buytbl GROUP BY userID;

# 회원당 평균 구매 회수
SELECT userID, avg(amount) as '평균 구매 개수' FROM buytbl GROUP BY userID;

# 가장 큰 키와 가장 작은 키의 회원 이름과 키 출력
SELECT name, height FROM usertbl
	WHERE height = (SELECT MAX(height) FROM usertbl)
		OR height = (SELECT MIN(height) FROM usertbl);
        
# 사용자별 총 구매액
SELECT userID as 사용자 , SUM(price*amount) as 총구매액
	FROM buytbl
    GROUP BY userID;
    
# 사용자별 총 구매액에 조건 넣기
SELECT userID as 사용자 , SUM(price*amount) as 총구매액
	FROM buytbl
    GROUP BY userID
    HAVING SUM(price*amount) > 1000
    ORDER BY 총구매액;

# 총합 또는 중간합계 시 사용
SELECT num, groupName, SUM(price * amount) as 비용
	FROM buytbl
    GROUP BY groupName
    WITH ROLLUP;

SELECT * FROM testtbl2;

SELECT * FROM testtbl4;
SELECT * FROM testtbl5;

# 데이터 수정
SELECT id, Lname FROM testtbl4 WHERE Fname = 'Kyoichi';
UPDATE testtbl4
	set Lname = '없음'
    WHERE Fname = 'Kyoichi';
    
UPDATE buytbl SET price = price * 1.5;

# 데이터 삭제
SELECT count(*) FROM testtbl4 WHERE Fname = 'Aamer';
DELETE FROM testtbl4 WHERE Fname = 'Aamer';

SELECT * FROM usertable;


# 네이버 주가정보 크롤링
SELECT count(*) FROM company_info;
SELECT * FROM company_info;
SELECT * FROM daily_price;
SELECT * FROM daily_price;
SELECT count(*) FROM daily_price ;

SELECT * from daily_price WHERE code = '005930' and date >= '2020-11-25' AND date <= '2022-02-04';
# 10
CREATE DATABASE INVESTAR10;