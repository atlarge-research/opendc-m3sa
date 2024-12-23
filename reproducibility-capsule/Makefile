.PHONY: build build-docker run run-docker clean
M3SA_OPENDC_DIR=../m3sa-opendc/opendc-experiments/opendc-experiments-m3sa
OPENDC_BUILD_DIR=$(M3SA_OPENDC_DIR)/build

run: build
	./m3sa-experiment

run-experiment1: build
	./m3sa-experiment experiment1

run-experiment2: build
	./m3sa-experiment experiment2

run-experiment3: build
	./m3sa-experiment experiment3

run-docker: build-docker
	sudo docker run -it m3sa

build: $(OPENDC_BUILD_DIR)
	cd bin/m3sa && make install
	chmod +x m3sa-experiment

build-docker:
	sudo docker build -t m3sa .

clean:
	rm -rf results
	rm -f analysis.txt

uninstall:
	cd bin/m3sa && make uninstall
	rm -rf $(OPENDC_BUILD_DIR)

$(OPENDC_BUILD_DIR):
	cd $(M3SA_OPENDC_DIR) && gradle shadowJar

