-- GROUP BY

-- 성별 개수
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고는
-- 집계함수를 쓰세요.
SELECT last_name, age, COUNT(*) FROM users GROUP BY last_name;

SELECT last_name, age FROM users WHERE last_name = '곽';

-- GROUP BY는 결과가 정렬되지 않음. 기존 순서와 바뀜
-- 원칙적으로 내가 정렬해서 보고 싶으면 ODER BY 사용!

SELECT * FROM users LIMIT 5;

-- GROUP BY WHERE를 쓰고 싶은데?
-- 100번 이상 등장한 성만 출력하고 싶음
SELECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP BY last_name;
-- 오류 발생
-- 결론 : 이렇게 작성이 불가능함. 이는 집계함수 처리 순서와 관련됨

SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name ,.,., 