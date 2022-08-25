import redis from 'redis';

const client = redis.createClient();

client.on('error', err => {
  if (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}).on('ready', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, result) => {
    redis.print(`Reply: ${result}`);
  });
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, result) => {
    console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
