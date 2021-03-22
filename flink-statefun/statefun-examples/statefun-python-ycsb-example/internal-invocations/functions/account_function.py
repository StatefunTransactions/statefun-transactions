from statefun import StatefulFunctions
from statefun import AsyncRequestReplyHandler
from statefun import kafka_egress_record

import logging

from google.protobuf.any_pb2 import Any

from messages_pb2 import Response, Wrapper, State
from messages_pb2 import Read, Update, Transfer

from exceptions import NotFoundException
from exceptions import AlreadyExistsException
from exceptions import UnknownMessageException
from exceptions import NotEnoughCreditException

# Logging config
FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

logger = logging.getLogger()

functions = StatefulFunctions()


@functions.bind("ycsb-example/account_function")
async def account_function(context, request: Wrapper):
    # Get state
    state = context.state('state').unpack(State)

    # messages from outside
    request_id = request.request_id
    message = request.message

    if message.Is(Transfer.DESCRIPTOR):
        transfer = Transfer()
        message.Unpack(transfer)

        read = Read()
        read.id = transfer.outgoing_id

        wrapped = Wrapper()
        wrapped.request_id = request_id
        outgoing_message = Any()
        outgoing_message.Pack(read)
        wrapped.message.CopyFrom(outgoing_message)
        context.pack_and_send("ycsb-example/account_function", transfer.outgoing_id, wrapped)
    elif message.Is(Read.DESCRIPTOR):
        read = Read()
        message.Unpack(read)

        update = Update()
        wrapped = Wrapper()
        wrapped.request_id = request_id
        outgoing_message = Any()
        outgoing_message.Pack(update)
        wrapped.message.CopyFrom(outgoing_message)
        context.pack_and_reply(wrapped)
    elif message.Is(Update.DESCRIPTOR):
        update = Update()
        message.Unpack(update)

        response = Response(request_id=request_id, status_code=200)
        egress_message = kafka_egress_record(topic="responses", key=request_id, value=response)
        context.pack_and_send_egress("ycsb-example/kafka-egress", egress_message)
    else:
        print("Test test test")


from aiohttp import web

handler = AsyncRequestReplyHandler(functions)


async def handle(request):
    req = await request.read()
    res = await handler(req)
    return web.Response(body=res, content_type="application/octet-stream")

app = web.Application()
app.add_routes([web.post('/statefun', handle)])

if __name__ == '__main__':
    web.run_app(app, port=80)
