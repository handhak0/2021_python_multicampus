# countrycode가 한국인 데이터의 개수 
SELECT COUNT(*) from city WHERE countrycode = 'kor' ;

# 한국인 데이터의 인구의 합, 평균, 최대, 최소
SELECT SUM(population) FROM city WHERE countrycode = 'kor' ;
SELECT AVG(population) FROM city WHERE countrycode = 'kor' ; 
SELECT Max(population) FROM city WHERE countrycode = 'kor' ; 
SELECT Min(population) FROM city WHERE countrycode = 'kor' ; 
SELECT SUM(population), AVG(population), 
	MAX(population), MIN(population) FROM city WHERE countrycode = 'kor';

# 충청남도의 도시 이름들의 그룹 
SELECT GROUP_CONCAT(NAME) FROM city WHERE district = 'chungchongnam' ;

# 한국의 중복되지 않는 시도 이름들의 그룹 
SELECT GROUP_CONCAT(DISTINCT district) FROM city WHERE countrycode = 'kor';

# 한국의 시도별 데이터가 몇 개인지
select district, COUNT(*) from city where countrycode='kor' group by district;

# 한국의 시도별 데이터 중 6개 이상의 데이터를 count 수로 내림차순 정렬 
SELECT district, COUNT(*) FROM city WHERE countrycode = 'kor'
	GROUP BY district HAVING COUNT(*) >= 6 ORDER BY COUNT(*) DESC ;