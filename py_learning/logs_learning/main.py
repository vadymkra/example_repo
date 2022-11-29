import logging
import logging.handlers


def password_filter(log: logging.LogRecord) -> int:
    return 0 if "password" in str(log.msg) else 1


def init_logger(name):  # init and setting our main logger
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s :: %(name)s:%(lineno)s :: %(levelname)s :: %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    sh.addFilter(password_filter)
    fh = logging.handlers.RotatingFileHandler(filename="logs/info.log")
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug("logger was initialized")


def main():
    init_logger("app")
    logger = logging.getLogger("app.main")
    logger.info("our app is start successfully")


if __name__ == "__main__":
    main()
