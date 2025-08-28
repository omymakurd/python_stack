insert into users (first_name,last_name,created_at,updated_at)
values
('Amy','Giver',now(),now()),
('Eli','Byers',now(),now()),
('Big','Bird',now(),now()),
('Kermit','The Frog',now(),now()),
('Marky','Mark',now(),now())
insert into users (first_name,last_name,created_at,updated_at)
values
('Marky','Mark',now(),now())
select * from users
select * from friendships
insert into friendships (user_id,friend_id,created_at,updated_at)
values
(1,6,now(),now()),
(2,1,now(),now()),
(2,3,now(),now()),
(3,2,now(),now()),
(3,5,now(),now()),
(4,3,now(),now()),
(5,1,now(),now()),
(5,6,now(),now()),
(6,2,now(),now()),
(6,2,now(),now())
select u.first_name ,u.last_name,f.first_name as frind_first_name,f.last_name as frind_last_name
from users u
join friendships fs 
on u.id=fs.user_id
left join users f 
on fs.friend_id=f.id 
------------------------------
select f.first_name , f.last_name
from users u 
join friendships fs 
on u.id = fs.user_id
left join users f 
on fs.friend_id=f.id 
where u.id=1
-------------------------------
select count(friendships.id) as total_friendships
from friendships
---------------------------------
select u.first_name,count(f.id) as count_of_frinds
from users u
join friendships fs
on u.id=fs.user_id
left join users f
on  fs.friend_id=f.id 
group by u.first_name
order by count_of_frinds desc
---------------------------------
select u.first_name as user_name, f.first_name as frind_first , f.last_name as frind_last
from users u 
join friendships fs 
on u.id = fs.user_id
left join users f 
on fs.friend_id=f.id 
where u.id=3
ORDER BY f.first_name, f.last_name;
