# city 테이블 조회 
SELECT * FROM city ;

# countrycode가 kor인 데이터만 조회 
SELECT * FROM city WHERE countrycode = 'kor';

# district가 kyonggi인 데이터만 조회 
SELECT * FROM city WHERE district = 'kyonggi' ;

# 경기도의 도시 이름과 인구 데이터만 조회 
SELECT NAME, population FROM city WHERE district = 'kyonggi' ;

# 인구가 50만이 넘는 경기도 도시 데이터 조회 
SELECT * FROM city WHERE district = 'kyonggi' AND population > 500000;

# 나라코드가 한국인 데이터 중 도시데이터 가져오기 (중복 X) 
SELECT DISTINCT district FROM city WHERE countrycode = 'kor' ;

# 전라남도이거나 전라북도이거나 광주인 데이터 가져오기 
SELECT * FROM city WHERE district = 'chollanam' OR district ='chollabuk' OR district = 'kwangju';
SELECT * FROM city WHERE district IN ('chollanam', 'chollabuk', 'kwangju');
