# When scaling your service to use multiple machines for data storage, you need a strategy to distribute, store, and retrieve data efficiently. This process typically involves data partitioning (sharding) and ensuring consistent interaction with your data nodes. Here’s a step-by-step guide on how to achieve this:

# Step 1: Data Partitioning (Sharding)
# Sharding involves splitting your data across multiple machines (shards) to balance the load and enhance performance.

# Determine Sharding Key: Choose a key to distribute the data (e.g., user ID).
'''Hashing or Range-based Partitioning: Decide on a partitioning strategy:
Hashing: Use a hash function on the sharding key to distribute data evenly across shards.
Range-based: Divide the data into ranges (e.g., user ID 1-1000 on shard 1, 1001-2000 on shard 2, etc.).
Step 2: Set Up Shards
For illustration, assume you have 4 shards (machines):

Shard 1: Stores data for users with IDs hashed or ranged to this shard.
Shard 2: Stores data for another set of users.
Shard 3: Similarly, stores data for another set.
Shard 4: Similarly, stores data for another set.
Step 3: Implement Data Routing Logic
Central Router Service: A central service (or a routing library) determines which shard to interact with based on the sharding key.'''


# Step 1 -> Central Router Service: A central service (or a routing library) determines which shard to interact with based on the sharding key.


import hashlib

class ShardRouter:
    def __init__(self, shards):
        self.shards = shards

    def _hash_key(self, key):
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % len(self.shards)

    def get_shard(self, key):
        shard_index = self._hash_key(key)
        return self.shards[shard_index]

# Example shards (machines)
shards = ["shard1.example.com", "shard2.example.com", "shard3.example.com", "shard4.example.com"]

router = ShardRouter(shards)


# Step 2-> Data Storage: When saving data, the router determines the correct shard.

def save_user_data(user_id, user_data):
    shard = router.get_shard(user_id)
    # Assume `send_to_shard` is a function to send data to a specific shard
    send_to_shard(shard, user_id, user_data)

def send_to_shard(shard, user_id, user_data):
    # This is a placeholder function
    # Implement logic to connect to the shard and save the data
    print(f"Saving data for user {user_id} to {shard}")

# Example usage
user_id = "12345"
user_data = {"name": "John Doe", "email": "john@example.com"}
save_user_data(user_id, user_data)

# Step 3 -->  Implement Data Retrieval
# When retrieving data, use the same routing logic to fetch data from the correct shard.


def get_user_data(user_id):
    shard = router.get_shard(user_id)
    return fetch_from_shard(shard, user_id)

def fetch_from_shard(shard, user_id):
    # This is a placeholder function
    # Implement logic to connect to the shard and fetch the data
    print(f"Fetching data for user {user_id} from {shard}")
    # Placeholder for actual data retrieval logic
    return {"name": "John Doe", "email": "john@example.com"}

# Example usage
user_id = "12345"
user_data = get_user_data(user_id)
print(user_data)


# for replication we will create master slave like 4 slaves for each shards


                         +--------------------------+
                          |    Load balancer         |
                          +---------------------------+
                                  |
                                  v

                          +--------------------------+
                          |    Application Server     |
                          +---------------------------+
                                  |
                                  v
                          +----------------------+
                          |    ShardRouter       |
                          +----------------------+
                                  |
                +----------------+----------------+----------------+
                |                |                |                |
                v                v                v                v
        +--------------+  +--------------+  +--------------+  +--------------+
        | Master 1     |  | Master 2     |  | Master 3     |  | Master 4     |
        |              |  |              |  |              |  |              |
        +------+-------+  +------+-------+  +------+-------+  +------+-------+
               |                 |                 |                 |
               |                 |                 |                 |
               v                 v                 v                 v
        +--------------+  +--------------+  +--------------+  +--------------+
        | Slave 1A     |  | Slave 2A     |  | Slave 3A     |  | Slave 4A     |
        +--------------+  +--------------+  +--------------+  +--------------+
        | Slave 1B     |  | Slave 2B     |  | Slave 3B     |  | Slave 4B     |
        +--------------+  +--------------+  +--------------+  +--------------+
