SELECT * FROM users LIMIT 1;

-- 문자열 합치기 ||
-- (성+이름) 출력, 5명만
SELECT last_name || first_name 이름, age, country, phone, balance FROM users LIMIT 5;

-- 문자열 길이 LENGTH
SELECT LENGTH(first_name), first_name FROM users LIMIT 5;

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 01672802855
SELECT first_name, phone REPLACE(phone, '-', ''), FROM users LIMIT 5;

-- 숫자 활용
SELECT MOD(5, 2) FROM users LIMIT 1;

-- CEIL : 올림, FLOOR : 내림, ROUND : 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14) FROM usrs LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9) FROM users LIMIT 1;

-- 9^2
SELECT POWER(9, 2) FROM users LIMIT 1;