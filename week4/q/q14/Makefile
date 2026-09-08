.PHONY: all clean

all: stats.txt report.txt

stats.txt: data.csv stats.py
	python stats.py

report.txt: report.md stats.txt build_report.py
	python build_report.py

clean:
	rm -f stats.txt report.txt
