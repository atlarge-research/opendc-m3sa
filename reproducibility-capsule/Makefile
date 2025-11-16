.PHONY: build host-build docker-build run host-run docker-run run-figure4 run-figure6 run-experiment1 run-experiment2 run-experiment3 clean uninstall

M3SA_OPENDC_DIR=../m3sa-opendc/opendc-experiments/opendc-experiments-m3sa
OPENDC_BUILD_DIR=$(M3SA_OPENDC_DIR)/build

USE_DOCKER ?= 1
DOCKER_IMAGE ?= m3sa-capsule
DOCKERFILE ?= $(CURDIR)/Dockerfile
DOCKER_CONTEXT ?= $(abspath ..)
DOCKER_MOUNT := -v $(abspath ..):/workspace/private-opendc-m3sa
DOCKER_WORKDIR := /workspace/private-opendc-m3sa/reproducibility-capsule
DOCKER_RUN := docker run --rm -it $(DOCKER_MOUNT) -w $(DOCKER_WORKDIR) $(DOCKER_IMAGE)

# Host/native execution ----------------------------------------------------
host-run: host-build
	./m3sa-experiment $(RUN_ARGS)

host-build: $(OPENDC_BUILD_DIR)
	cd bin/m3sa && make install
	chmod +x m3sa-experiment

$(OPENDC_BUILD_DIR):
	cd ../m3sa-opendc && ./gradlew :opendc-experiments:opendc-experiments-m3sa:shadowJar

# Docker-backed execution (default) ---------------------------------------
docker-build:
	docker build -f $(DOCKERFILE) -t $(DOCKER_IMAGE) $(DOCKER_CONTEXT)

ifeq ($(USE_DOCKER),1)
build: RUN_ARGS=
build: docker-build
	$(DOCKER_RUN) -lc "make USE_DOCKER=0 host-build"

run: RUN_ARGS=
run: docker-build
	$(DOCKER_RUN) -lc "make USE_DOCKER=0 host-build && ./m3sa-experiment $(RUN_ARGS)"

run-figure4: RUN_ARGS=figure4
run-figure4: run

run-figure6: RUN_ARGS=figure6
run-figure6: run

run-experiment1: RUN_ARGS=experiment1
run-experiment1: run

run-experiment2: RUN_ARGS=experiment2
run-experiment2: run

run-experiment3: RUN_ARGS=experiment3
run-experiment3: run
else
build: RUN_ARGS=
build: host-build

run: RUN_ARGS=
run: host-run

run-figure4: RUN_ARGS=figure4
run-figure4: host-run

run-figure6: RUN_ARGS=figure6
run-figure6: host-run

run-experiment1: RUN_ARGS=experiment1
run-experiment1: host-run

run-experiment2: RUN_ARGS=experiment2
run-experiment2: host-run

run-experiment3: RUN_ARGS=experiment3
run-experiment3: host-run
endif

clean:
	rm -rf results
	rm -f analysis.txt

uninstall:
	cd bin/m3sa && make uninstall
	rm -rf $(OPENDC_BUILD_DIR)
