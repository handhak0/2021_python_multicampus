# 도시이름, 인구와 국가이름을 city와 country 테이블에서 countrycode로  합쳐서 가져와라 

SELECT city.name, city.Population, country.Name FROM city 
	 	INNER JOIN country ON city.countrycode = country.code ;
	 


SELECT city.name, city.Population, country.Name FROM city 
	 	INNER JOIN country ON city.countrycode = country.code 
	 	WHERE city.countrycode = 'kor';
	