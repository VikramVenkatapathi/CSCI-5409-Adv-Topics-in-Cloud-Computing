import grpc
import computeandstorage_pb2
import computeandstorage_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')  # Replace with the server address
stub = computeandstorage_pb2_grpc.EC2OperationsStub(channel)

request = computeandstorage_pb2.StoreRequest()
request.data = 'STORE'

response = stub.StoreData(request)

print("S3 URL:", response.s3uri)

# pip install boto3
# pip install grpcio grpcio-tools
# python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. computeandstorage.proto
