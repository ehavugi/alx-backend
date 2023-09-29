import {createQueue} from 'kue';

const queue = createQueue();
// Job data definition

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
 // listen on push notification code
 const {phoneNumber, message } = job.data;

 sendNotification(phoneNumber, message);
 // Mark job done
 
 done();
});

queue.on('error', (err) => {
  console.error('Queue error', err);
});
