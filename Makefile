
FILES= bonds.svg \
	   cover.svg \
	   glycine-card.png \
	   index.html \
	   logo.png \
	   mol1.svg \
	   mol2.svg \
	   mol3.svg \
	   nitric-acid.png \
	   orgo-pieces.jpg \
	   orgo-prototype.jpg \
	   style.css

all: sync

sync:
	s3cmd -P -r sync $(FILES) s3://www.pwanson.com/orgo/

put:
	s3cmd -P -r put $(FILES) s3://www.pwanson.com/orgo/

