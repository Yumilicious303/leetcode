
import random 
def generate_random_data():
    # Generate a random integer h between 1 and 100000
    h = random.randint(1, 100000)
    
    # Generate a random array of coworkers
    num_coworkers = random.randint(1, 100000)
    coworkers = []
    for _ in range(num_coworkers):
        # Each coworker is represented by an array of two integers between 1 and 1 billion
        coworker = [random.randint(1, 1000000000), random.randint(1, 1000000000)]
        coworkers.append(coworker)
    
    return h, coworkers

def generate_random_data2():
    # Generate a random integer h between 1 and 100000
    h = random.randint(1, 100)
    
    # Generate a random array of coworkers
    num_coworkers = random.randint(1, 100)
    coworkers = []
    for _ in range(num_coworkers):
        # Each coworker is represented by an array of two integers between 1 and 1 billion
        coworker = [random.randint(1, 100), random.randint(1, 100)]
        coworkers.append(coworker)
    
    return h, coworkers

print(generate_random_data2())