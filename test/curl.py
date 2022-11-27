import requests
import argparse
import json


HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

URL = "http://127.0.0.1:8000"


def curl_get(args):
    print("GET")
    id = f"/{args.id}"
    api_path = f"/{args.path}"
    return requests.get(
        f'{URL}{api_path}{id}', headers=HEADERS)


data_j = {}
def curl_post(args):
    print("PUT")
    with open(f"{args.json}", mode="r") as f:
        data = json.load(f)
    return requests.post(
        f'{URL}/{args.path}', headers=HEADERS, json=data)


def parse_command_line():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_get = subparsers.add_parser(
        "GET",
        help="get method"
    )
    parser_get.add_argument(
        "path",
        help="set api path"
    )
    parser_get.add_argument(
        '--id', 
        type=str,
        default="",
        help="set id"
    )
    parser_get.set_defaults(handler=curl_get)

    parser_post = subparsers.add_parser(
        "POST",
        help="post method"
    )
    parser_post.add_argument(
        "path",
        help="set api path"
    )
    parser_post.add_argument(
        "json",
        help="set data"
    )
    parser_post.set_defaults(handler=curl_post)
    return parser.parse_args()


def main():
    args = parse_command_line()
    print(f"args command: {args}")
    if hasattr(args, 'handler'):
        response = args.handler(args)
    else:
        pass

    print(response)
    print(response.text)


if __name__ == '__main__':
    main()
