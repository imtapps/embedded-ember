import Ember from 'ember';

export default Ember.Component.extend({
  year: Ember.computed(() => {
    return new Date().getFullYear();
  })
});
