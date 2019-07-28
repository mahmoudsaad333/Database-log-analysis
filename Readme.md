# Log Analysis Project

> Mahmoud Ahmed

This project is to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
- Python2.7 or later versions
- vagrant
- VirtualBox
```

### Installing

```
1. Install Vagrant and VirtualBox
2. Download the FSND VM Configuration
3. Download the newsdata.sql
4. now place the newsdata.sql and the content of this project in the same folder
```

### Running

1. Launch the Vagrant VM inside Vagrant folder in the downloaded FSND-vm repository using

```
vagrant up
```

2. log in using

```
vagrant ssh
```

3. change directory to /vagrant using

```
cd /vagrant
```

### Preparing database and views

1. load the data using

```
psql -d news -f newsdata.sql
```

2. connect to database

```
psql -d news
```

3. Create view article_view

```
create view article_view as select title,author,count(*) as views from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author 
  order by views desc;
```

4. Create view error_view
```
create view error_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
  then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
  order by "Percent Error" desc;
```

## Deployment

* From the vagrant directory run Report.py using
```
python report.py
```
* for python3
```
 python3 report.py
```
