import asyncio

from aioredis import Redis


async def main():
    redis = Redis(decode_responses=True, ssl=True, ssl_keyfile='./redis/tls/client.key',
                  ssl_certfile='./redis/tls/client.crt', ssl_ca_certs='./redis/tls/ca.crt', password='password')

    await redis.set('key', 'value')

    print(await redis.get('key'))


if __name__ == '__main__':
    asyncio.run(main())
