# import grpc
# import computeandstorage_pb2
# import computeandstorage_pb2_grpc

# channel = grpc.insecure_channel('[::]:50051')

# stub = computeandstorage_pb2_grpc.EC2OperationsStub(channel)

# request = computeandstorage_pb2.AppendRequest()

# request.data = "Vikram - Append"

# response = stub.AppendData(request)

# print("Appended!!")
import grpc
import computeandstorage_pb2
import computeandstorage_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')  # Replace with the server address
stub = computeandstorage_pb2_grpc.EC2OperationsStub(channel)

request = computeandstorage_pb2.AppendRequest()
request.data = 'APPEND'

response = stub.AppendData(request)  # Pass the context argument

print("AppendData method called successfully!")
