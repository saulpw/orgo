
FILES= bonds.svg \
	   cover.svg \
	   cover.pdf \
	   glycine-card.png \
	   index.html \
	   logo.png \
	   mol1.pdf \
	   mol1.svg \
	   mol2.svg \
	   mol2.pdf \
	   mol3.svg \
	   mol3.pdf \
	   nitric-acid.png \
	   orgo-pieces.jpg \
	   orgo-prototype.jpg \
	   style.css

all: sync

sync:
	s3cmd -P -r sync $(FILES) s3://www.pwanson.com/orgo/

put:
	s3cmd -P -r put $(FILES) s3://www.pwanson.com/orgo/

