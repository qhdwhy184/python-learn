from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc


class BidirectionalStreamingServiceServicer(service_pb2_grpc.BidirectionalStreamingServiceServicer):
    def SendMessageStream(self, request_iterator, context):
        for request in request_iterator:
            print(f"Received message: {request.content}")
            yield service_pb2.MessageResponse(response_content=f"Echo: {request.content}")

    def SendMessageNonStream(self, request, context):
        # 这里不需要使用async for，因为这是一个简单的RPC调用
        print(f"Received NonStream message2: {request.content}")
        return service_pb2.MessageResponse(response_content=f"NonStream Echo2: {request.content}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_BidirectionalStreamingServiceServicer_to_server(BidirectionalStreamingServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()