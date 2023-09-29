import {createQueue} from 'kue';

const blacklistedNumbers  =  ['4153518780', '4153518781'];

const queue = createQueue({ concurrency: 2 });

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0,100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
  // Mark job done
  done();
}

queue.process('push_notification_code_3', 2, (job, done) => {
   const { phoneNumber, message}  = job.data;
   // call send notification job processor
   sendNotification(phoneNumber, message, job, done);
}
);


queue.on('error', (err) => {
  console.log('Queue error:', err);
});
