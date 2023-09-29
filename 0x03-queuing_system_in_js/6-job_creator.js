import {createQueue} from 'kue';

const queue = createQueue();
// Job data definition
const jobData = {
  phoneNumber: '0724583402',
  message: 'Hi there, this is a test message'
};

// create a job

const job = queue.create('push_notification_code', jobData);

// listen on job
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// save a job

job.save(() => {
  console.log(`Notification job created: ${job.id}`);
});
