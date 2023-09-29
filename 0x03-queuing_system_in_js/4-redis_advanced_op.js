import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function createHash() {
  const hashKey = 'HolbertonSchools';
  const hashValues = {
    'Portland':50,
    'Seattle':80,
    'New York':20,
    'Bogota':20,
    'Cali':40,
    'Paris':2
  };
  
 for (const key in hashValues) {
   if (hashValues.hasOwnProperty(key)) {
      const value = hashValues[key];
      client.hset(hashKey, key, value, redis.print);
   }
 };
 client.hgetall(hashKey, (err, reply)  => {
   if (err){
     console.log(`Error retreiving hash: ${err.message}`);
   } else {
     console.log(reply);
   }
 });
	
}

// create hash
createHash();
