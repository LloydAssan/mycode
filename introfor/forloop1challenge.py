#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop- CHALLENGE"""

def main():
    
            farms = [{"name": "NE Farm",
                "agriculture":["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
                 {"name": "W Farm",
                     "agriculture": ["pigs", "chickens", "llamas"]},
                 {"name": "SE Farm",
                     "agriculture": ["chickens", "carrots", "celery"]}]
            for i in farms:
                print(i.get('name','Unknown Farm'), end=':\n')

                for agri in i.get('agriculture'):
                    print(' -', agri)

            __name__ == "__main__":
main()

