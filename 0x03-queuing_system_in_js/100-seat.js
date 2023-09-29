// import all necessary modules
import redis from 'redis';
import {promisify} from 'util';

import kue from 'kue';
import express from 'express';

// Part A
// intialize reserves to 50

const client = redis.createClient();

// use promisified redis methods

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveSeat(number) {
   await setAsync('available_seats', number.toString());
}

// initialize reservable seats to 50
reserveSeat(50);

// initialize reservationEnable to true
let reservationEnabled = true;

// Part B
//initialize kue queue
const queue = kue.createQueue();


// Part C
// express server interface

const app = express();
const port  = 1245;

// route for available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getAsync('available_seats');
 console.log('available seats', numberOfAvailableSeats);
 res.json({numberOfAvailableSeats});
});


// routes tor reserve a seat

app.get('/reserve_seat', async (req, res) => {
  if(!reservationEnabled) {
    return res.json({status: 'Reservation are blocked'});
  }
  
  const job = queue
    .create('reserve_seat')
    .save((err) => {
      if(err) {
        return res.json({status: 'Reservation failed'});
      }
      res.json({status: 'Reservation in process'});
    });
  
  job
    .on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  })
    .on('failed', (errorMessage) => {
      console.error(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });

});


// route for process
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = parseInt(await getAsync('available_seats'), 10);
    console.log('Current seats', currentAvailableSeats); 
    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
    }

    if (currentAvailableSeats >= 1) {
      // Successful reservation
      console.log('successfully reserved one of  ', currentAvailableSeats);
	
      console.log('current available seats ', currentAvailableSeats);
      await reserveSeat(currentAvailableSeats - 1);
      done();
    } else {
      // Not enough seats available
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});


