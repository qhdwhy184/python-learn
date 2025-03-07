import asyncio
import grpc
import service_pb2
import service_pb2_grpc

async def generate_messages():
    messages = ["First message", "Second message", "Third message"]
    for msg in messages:
        yield service_pb2.Message(content=msg)
        await asyncio.sleep(0.1) # 模拟异步操作

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.BidirectionalStreamingServiceStub(channel)
        responses = stub.SendMessageStream(generate_messages())
        async for response in responses:
            print(f"Received response: {response.response_content}")

        response2 = await stub.SendMessageNonStream(service_pb2.Message(content="First Non stream message"))
        print(f"Received non-stream response: {response2.response_content}")

if __name__ == '__main__':
    asyncio.run(run())