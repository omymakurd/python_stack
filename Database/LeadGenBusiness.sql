

select sum(billing.amount) as total_revenue
from billing
where billing.charged_datetime >='2012-03-01'
and billing.charged_datetime < '2012-04-01'
-----------------------------------
select billing.client_id, concat(clients.first_name,' ',clients.last_name) as name,  sum(billing.amount) as total_revenue
from billing
join clients
on billing.client_id=clients.client_id
where billing.client_id = 2
-------------------------------------
select concat(clients.first_name,' ',clients.last_name) as name ,clients.client_id,sites.domain_name
from clients
join sites
on clients.client_id = sites.client_id
where clients.client_id = 10
---------------------------------------
select sites.client_id,count(sites.site_id) NOS,MONTHNAME(sites.created_datetime) as mounth_created,YEAR(sites.created_datetime) as year_created
from sites
where client_id=1
GROUP by sites.client_id,MONTHNAME(sites.created_datetime),YEAR(sites.created_datetime) 
-------------------------------------
select sites.client_id,count(sites.site_id) NOS,MONTHNAME(sites.created_datetime) as mounth_created,YEAR(sites.created_datetime) as year_created
from sites
where client_id=20
GROUP by sites.client_id,MONTHNAME(sites.created_datetime),YEAR(sites.created_datetime) 
---------------------------------------
select sites.domain_name ,count(leads.leads_id)
from sites
join leads
on sites.site_id = leads.site_id
where leads.registered_datetime >= '2011-01-01' and leads.registered_datetime <= '2011-02-15'
GROUP by sites.site_id
------------------------------------------
select concat(clients.first_name,' ',clients.last_name) as name,count(leads.leads_id)
from clients
join sites
on clients.client_id = sites.client_id
join leads 
on sites.site_id = leads.site_id
where leads.registered_datetime >= '2011-01-01' and leads.registered_datetime < '2011-12-31'
GROUP by clients.client_id
-------------------------------------------------
select concat(clients.first_name,' ',clients.last_name) as name,count(leads.leads_id),MONTHNAME(leads.registered_datetime)
from clients
join sites
on clients.client_id = sites.client_id
join leads 
on sites.site_id = leads.site_id
where leads.registered_datetime >= '2011-01-01' and leads.registered_datetime < '2011-07-01'
GROUP by clients.client_id , MONTHNAME(leads.registered_datetime)
------------------------------------------
select concat(clients.first_name,' ',clients.last_name) as name,sites.domain_name,count(leads.leads_id)
from clients
join sites
on clients.client_id = sites.client_id
join leads 
on sites.site_id = leads.site_id
where leads.registered_datetime >= '2011-01-01' and leads.registered_datetime <= '2011-12-31'
GROUP by clients.client_id,sites.site_id
order by clients.client_id asc
----------------------------------------
select concat(clients.first_name,' ',clients.last_name) as name,sites.domain_name,count(leads.leads_id)
from clients
join sites
on clients.client_id = sites.client_id
join leads 
on sites.site_id = leads.site_id
GROUP by clients.client_id,sites.site_id
order by clients.client_id asc
----------------------------------------
select concat(clients.first_name,' ',clients.last_name) as client_name, sum(billing.amount) as total_revenue,MONTH(billing.charged_datetime) as month_charged,YEAR(billing.charged_datetime) as year_charged
FROM clients
JOIN billing
on clients.client_id=billing.client_id
group by  clients.client_id,MONTH(billing.charged_datetime),YEAR(billing.charged_datetime)
order by clients.client_id asc
-----------------------------------------------------------------
select concat(clients.first_name,' ',clients.last_name) as client_name, sum(billing.amount) as total_revenue,MONTHNAME(billing.charged_datetime) as month_charged,YEAR(billing.charged_datetime) as year_charged
FROM clients
JOIN billing
on clients.client_id=billing.client_id
group by  clients.client_id,MONTHNAME(billing.charged_datetime),YEAR(billing.charged_datetime)
order by clients.client_id asc
------------------------------------
select concat(clients.first_name,' ',clients.last_name) as client_name ,  GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') as sites
from clients
join sites
on clients.client_id=sites.client_id
group by clients.client_id

-----------------------------------
select * from billing
select * from clients
select * from leads
select * from sites