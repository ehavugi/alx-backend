import {createQueue, kue, Job} from 'kue';

let queue = createQueue();
function createPushNotificationsJobs(jobs, queue){ 
  if (!(jobs instanceof Array)){
     console.error('Jobs is not an array');
     throw new Error('Jobs is not an array');
  }
  // similar to 7-job_creator.js 
  jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_3', jobData);
  
  job.on('enqueue', () => {
    console.log('Notification job created:', job.id);
  });
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Listen for job failure event
  job.on('failed', (err) => {
    console.error(`Notification job ${job.id} failed: ${err}`);
  });

  // Listen for job progress event
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
  
   // save the hob
  job.save();
  });

}

export default createPushNotificationsJobs;
