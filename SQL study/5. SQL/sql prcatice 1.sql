USE employees;

# select문 연습
# select first_name, last_name, gender from employees;
#salary, to_date from salaries; 

# 전체 데이터베이스 정보 확인
# show table status;

# 특정 데이터베이스 정보 확인
# describe employees;

# 별칭 설정
# select first_name as 이름, gender 성별, hire_date '회사 입사일' from employees;
select emp_no 번호, birth_date 생일 from employees;
