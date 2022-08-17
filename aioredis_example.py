import asyncio

from aioredis import from_url

from time import perf_counter


async def main():
    redis = from_url(url='rediss://localhost', decode_responses=True, ssl_keyfile='./redis/tls/client.key',
                     ssl_certfile='./redis/tls/client.crt', ssl_ca_certs='./redis/tls/ca.crt',
                     password='password')

    start = perf_counter()
    size = 100000

    async with redis.client() as client:

        set_tasks = [client.set(f'key{number}', f'value{number}') for number in range(size)]
        get_tasks = [client.get(f'key{number}') for number in range(size)]

        end = perf_counter()

        print(f'prepare took {end-start}s')

        start = perf_counter()

        await asyncio.gather(*set_tasks)

        end = perf_counter()

        print(f'setting took {end-start}s')

        start = perf_counter()

        results = await asyncio.gather(*get_tasks)

        end = perf_counter()

        print(f'getting took {end-start}s')
        print('stored ', len(results), ' keys')


if __name__ == '__main__':
    asyncio.run(main())
