import sys
import collections
import logging
import socket

logging.basicConfig(level=logging.INFO)


def count_unique_ip_with_collections(filename):
    with open(filename, 'r') as file:
        ip_collection = collections.Counter(line.split()[0] for line in file)
        logging.debug(ip_collection)
    return len(ip_collection)


def count_unique_ip_with_set(filename):
    with open(filename, 'r') as file:
        ip_set = set(line.split()[0] for line in file)
    return len(ip_set)


def count_unique_ip_with_set_and_validation(filename):
    with open(filename, 'r') as file:
        ip_set = set()
        for line in file:
            if line.strip():
                ip = line.split()[0]
                if _is_valid(ip):
                    ip_set.add(ip)
                else:
                    logging.warning(f"Ignoring invalid IP address: {ip}")
        logging.debug(ip_set)
    return len(ip_set)


def _is_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


if __name__ == "__main__":
    logging.info(count_unique_ip_with_set_and_validation(sys.argv[1]))
    logging.debug(count_unique_ip_with_collections(sys.argv[1]))
