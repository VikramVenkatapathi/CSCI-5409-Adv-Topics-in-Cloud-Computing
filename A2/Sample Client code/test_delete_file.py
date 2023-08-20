import grpc
import computeandstorage_pb2
import computeandstorage_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = computeandstorage_pb2_grpc.EC2OperationsStub(channel)

bucketName = "b00936916-s3"
fileName = "sample"
s3_Key = f"{fileName}.txt"

request = computeandstorage_pb2.DeleteRequest()
's3://your-bucket/your-file.txt'

request.s3uri = f"s3://{bucketName}/{s3_Key}"

response = stub.DeleteFile(request)

print("File Deleted")

# python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. computeandstorage.proto
