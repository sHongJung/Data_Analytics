USE sakila;

select district from address
where city_id in (
select city_id from city
where city in ('Qalyub',  'Qinhuangdao', 'Qomsheh', 'Quilmes'));


