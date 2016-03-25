import re
import logging
import os.path
import sys

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program) 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
    if len(sys.argv) < 3:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    i = 0
 
    output = open(outp, 'w')
    f = open(inp)
    line = f.readline()
    while line:                 
        line = f.readline()
        rule=re.compile(r'[ a-zA-z]') # delete english char and blank 
        result = rule.sub('',line)
        output.write(result + "\n")
        i+=1
        logger.info("Saved " + str(i) + " lines")
    f.close()  
    output.close()
    logger.info("Finished Saved " + str(i) + " lines")


