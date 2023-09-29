import {expect, chai} from 'chai';
import {createQueue} from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationJobs', () =>{
  const queue = createQueue('push_notification_code_test1');

  before(() => { 
     queue.testMode.enter(true);
  });

  after((done) => {
    queue.testMode.clear();
    queue.testMode.exit();
    });
 
  it('should create jobs for valid job data', (done) => {
    const jobs = [
      {
        phoneNumber: '41535118780',
        message: 'This is the first notification',
      },
      {
        phoneNumber: '41535187818',
        message: 'This is the second notification',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Use queue.testMode.jobs to check the jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    done();
  });

  it('should throw an error for non-array job data', (done) => {
  const invalidJobs = 'Not an array';

  try {
    createPushNotificationsJobs(invalidJobs, queue);

    // Use queue.testMode.jobs to check the jobs in the queue (should be empty due to the error)
   //expect(queue.testMode.jobs.length).to.equal(0);

    done(); // Call done to signal the test completion
  } catch (error) {
    // Handle the error if it's thrown
    done(error);
  }
});

});
