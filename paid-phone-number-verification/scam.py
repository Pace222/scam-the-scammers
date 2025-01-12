#!/usr/bin/env python3
import requests
import threading
import random

NB_THREADS = 50

URL = '[...]'

DATA = {}

def post_request(tot_requests, i):
    while True:
        try:
            creds = str(random.randint(10000,0x7fffffff)) + ":" + "foobar"
            session = requests.session()
            session.proxies = {'http': f'socks5h://{creds}@localhost:9050', 'https': f'socks5h://{creds}@localhost:9050'}
            response = session.post(URL, data=DATA)
            out = response.json()
            print(f'{sum(tot_requests)}: {out}')

            if response.ok:
                tot_requests[i] += 1

            if out['msg'] == 'Der Einladungscode wurde verwendet':
                break
        except:
            pass


def main():
    threads = []
    tot_requests = [0] * NB_THREADS
    for i in range(NB_THREADS):
        t = threading.Thread(target=post_request, args=(tot_requests, i))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        try:
            t.join()
        except KeyboardInterrupt:
            print(f'{sum(tot_requests)} total requests sent')
            return


if __name__ == '__main__':
    main()


