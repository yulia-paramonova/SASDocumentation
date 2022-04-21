# Features Comparison

## Set up environment

### Install scrapy & scrapy splash

```
pip install scrapy
pip install scrapy-splash
```

### Start scrapy-splash

```
docker run -p 8050:8050 scrapinghub/splash
```

## Start scraping

### Actions

```
scrapy crawl actions -O actions.json
```

### Action Sets

```
scrapy crawl sets -O sets.json
```

## Shell for tests

```
scrapy shell 'http://localhost:8050/render.html?url=https://go.documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/allprodsactions/SAS-Visual-Analytics.htm&timeout=60&wait=31'
```