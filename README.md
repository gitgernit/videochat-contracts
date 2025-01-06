# contracts

Repository containing all the contracts used by multiple services (i.e. gRPC protobuf)  
Intended to be cloned into an existing git repo as a git submodule

## Prerequisites
* git
* Make

## Submodule installation
`git submodule add <url>` to clone & initialize  
`git submodule init` to initialize  
`git submodule update` to update submodules  

## Usage
### Generating Go Code
1. Install the protocol compiler plugins for Go using the following commands:  
    ```shell
    go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
    go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway@latest
    ```
2. Update your PATH so that the protoc compiler can find the plugins:
    ```shell
    export PATH="$PATH:$(go env GOPATH)/bin"
    ```
3. Use Make to generate Go code:
    ```shell
   make generate-go-rooms
    ```

### Generating Python Code
1. Install grpcio-tools package
   ```shell
   pip install grpcio-tools
   ```
   Optionally, use a virtual environment.
2. Use Make to generate Python code:
   ```shell
   make generate-python-rooms
   ```
