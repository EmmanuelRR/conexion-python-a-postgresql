import logging as log

log.basicConfig(level= log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%p',
                handlers=[log.FileHandler('caa_datos..log'), log.StreamHandler()])
if __name__=='__main__':
    log.debug(f'error a nivel debug')