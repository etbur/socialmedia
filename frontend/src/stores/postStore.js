import { defineStore } from 'pinia';

export const usePostStore = defineStore('postStore', {
  state: () => ({
    posts: [],
  }),
  actions: {
    updatePosts(newPosts) {
      this.posts = newPosts;
    },
  },
});