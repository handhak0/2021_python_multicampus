# kor의 name이 shihung을 siheung으로 변경하라 

UPDATE city SET NAME = 'Siheung' 
	WHERE countrycode = 'kor' AND NAME = 'shihung';

# siheung의 population을 153443으로 변경하라 

UPDATE city SET population = 153443 
	WHERE countrycode = 'kor' AND NAME = 'siheung' ;