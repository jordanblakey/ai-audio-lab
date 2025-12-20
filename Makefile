.PHONY: help

help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

venv: ## Create and activate virtual environment
	@echo "Creating virtual environment..."
	if [ ! -d "venv" ]; then python3 -m venv venv; fi
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

protos: ## Generate gRPC Python code
	@echo "Generating gRPC Python code..."
	. venv/bin/activate && \
		python -m grpc_tools.protoc \
		-I . \
		--python_out=. \
		--pyi_out=. \
		--grpc_python_out=. \
		protos/*.proto

docker-build: ## Build Docker images
	@echo "Building Docker images..."
	docker build -f server/Dockerfile -t grpc-server .
	docker build -f client/Dockerfile -t grpc-client .

docker-system-prune: ## Prune all unused Docker objects
	@echo "Pruning Docker..."
	docker system prune -a --volumes --force
