EVENTS:= $(wildcard events/*.yaml)

all: kpis.yaml countries.csv index.html

kpis.yaml: update-kpis.py $(EVENTS)
	python update-kpis.py

countries.csv: export.py $(EVENTS)
	python export.py > countries.csv;

index.html: countries.csv kpis.yaml template.html
	python build.py
