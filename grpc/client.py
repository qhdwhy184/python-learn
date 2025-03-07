import grpc
import service_pb2
import service_pb2_grpc

def generate_messages():
    messages = ["First message", "Second message", "Third message"]
    for msg in messages:
        yield service_pb2.Message(content=msg)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.BidirectionalStreamingServiceStub(channel)
        responses = stub.SendMessageStream(generate_messages())
        for response in responses:
            print(f"Received response: {response.response_content}")

        response2 = stub.SendMessageNonStream(service_pb2.Message(content="First message2"))
        print(f"Received response2: {response2.response_content}")


if __name__ == '__main__':
    run()
