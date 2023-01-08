from pelutils import log


def run():
    pass

if __name__ == "__main__":
    with log.log_errors:
        log.configure("out/stonks.log")
        run()
