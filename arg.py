import argparse

def print_me(process='1', batch='1'):
    print("Number of processes : " + str(process))
    print("Number of messages to receive from the Queue: " + str(batch))
  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script is going to create multiple process to send SMS. 
    """)
    parser.add_argument("--process", help="How many processes need to create")
    parser.add_argument("--batch", help="How many messages to receive from the Queue")
    

    args = parser.parse_args()
    print(args.__dict__)
    PROCESS = BATCH = 1
    
    if args.__dict__.get('process') is not None:
        PROCESS = args.process
    if args.__dict__.get('batch') is not None:
       BATCH = args.batch
    print_me(PROCESS, BATCH)
 

     
    