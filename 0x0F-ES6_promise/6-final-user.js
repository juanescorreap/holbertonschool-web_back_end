import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      const list = [];
      for (const value of values) {
        if (value.status === 'rejected') {
          value.value = values.reason.toString().substring(0, 40);
          delete value.reason;
        }
        list.push(value);
      }
      return list;
    });
}
