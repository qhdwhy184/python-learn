import asyncio
import time
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc

class BidirectionalStreamingServiceServicer(service_pb2_grpc.BidirectionalStreamingServiceServicer):

    async def SendMessageStream(self, request_iterator, context):
        async for request in request_iterator:
            print(f"Received message: {request.content}")
            yield service_pb2.MessageResponse(response_content=f"Echo: {request.content}")

    async def SendMessageNonStream(self, request, context):
        # 这里不需要使用async for，因为这是一个简单的RPC调用
        print(f"Received NonStream message2: {request.content}")
        return service_pb2.MessageResponse(response_content=f"NonStream Echo2: {request.content}")


async def serve():
    server = grpc.aio.server()
    service_pb2_grpc.add_BidirectionalStreamingServiceServicer_to_server(BidirectionalStreamingServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        print("Server shutting down...")