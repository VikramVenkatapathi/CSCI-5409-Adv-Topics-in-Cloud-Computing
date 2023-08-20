import grpc
from concurrent import futures
from computeandstorage_pb2 import  StoreReply, AppendReply, DeleteReply
from computeandstorage_pb2_grpc import EC2OperationsServicer, add_EC2OperationsServicer_to_server

import boto3

bucketName = "b00936916"
fileName = "sample"
s3_Key = f"{fileName}.txt"

class EC2Operations(EC2OperationsServicer):
    def StoreData(self, request, context):
        data = request.data

        s3_client = boto3.client('s3')
    
        s3_client.put_object(Body=data, Bucket=bucketName, Key=s3_Key)

        s3_URL = f"https://{bucketName}.s3.amazonaws.com/{s3_Key}"

        print("STORE -> received data : ", data)
        response = StoreReply()
        response.s3uri = s3_URL

        return response
    
    def AppendData(self, request, context):
        data = request.data

        s3_client = boto3.client('s3')

        response = s3_client.get_object(Bucket = bucketName, Key = s3_Key)

        existing_Data = response['Body'].read().decode('utf-8')

        print("APPEND -> received data : ", data)
        updated_Data = existing_Data + data

        updated_file_key = f"{fileName}.txt"

        s3_client.put_object(Body = updated_Data, Bucket = bucketName, Key = updated_file_key)

        response = AppendReply()

        return response
    def DeleteFile(self, request, context):
        s3_client = boto3.client('s3')

        s3_client.delete_object(Bucket = bucketName, Key = s3_Key)
    
        response = DeleteReply()
        print("File deleted.")
        return response
def serve():
    server = grpc.server(futures.ThreadPoolExecutor())

    ec2_operations_servicer = EC2Operations()
    add_EC2OperationsServicer_to_server(ec2_operations_servicer, server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server started, listening on port 50051... ")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
