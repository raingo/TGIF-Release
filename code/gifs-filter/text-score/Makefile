
opt=-O3 -Wl,--rpath-link=.
#opt=-ggdb
CFLAGS=-I$(HOME)/local/opencv3/include $(opt)
LDFLAGS=-L$(HOME)/local/opencv3/lib/ -lopencv_photo -lopencv_core -lopencv_ml -lopencv_imgproc -lopencv_imgcodecs $(opt)

all: textdetection text-score

erfilter.o: erfilter.cpp erfilter.hpp
	g++ erfilter.cpp -c $(CFLAGS)

text-score.o: text-score.cpp erfilter.hpp group_area.hpp filter.hpp
	g++ text-score.cpp -c $(CFLAGS)

textdetection.o: textdetection.cpp erfilter.hpp group_area.hpp filter.hpp
	g++ textdetection.cpp -c $(CFLAGS)

textdetection: textdetection.o erfilter.o
	g++ textdetection.o erfilter.o -o textdetection $(LDFLAGS)

text-score: text-score.o erfilter.o
	g++ text-score.o erfilter.o -o text-score $(LDFLAGS)

clean:
	rm -f *.o
	rm text-score textdetection
