<!-- PostFetchPage.vue -->
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const posts = ref([]);
let webSocket;
const isConnected = ref(false);
const isLoading = ref(false);

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString();
};

const connectWebSocket = () => {
  webSocket = new WebSocket('ws://localhost:8000/ws/posts/');

  webSocket.onopen = () => {
    console.log('WebSocket connection established');
    isConnected.value = true;
    isLoading.value = false;
    fetchPosts();
  };

  webSocket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Received data:', data); // Debugging: log received data
    if (data.action === 'fetch_response') {
      posts.value = data.posts;
      console.log('Posts updated:', posts.value); // Debugging: log posts after update
    } else if (data.error) {
      console.error('Error from server:', data.error); // Debugging: log server error
    }
  };

  webSocket.onclose = () => {
    console.log('WebSocket connection closed');
    isConnected.value = false;
    isLoading.value = true;
    setTimeout(connectWebSocket, 5000); // Reconnect after 5 seconds
  };

  webSocket.onerror = (event) => {
    console.error('WebSocket error:', event);
    isConnected.value = false;
    isLoading.value = true;
  };
};

const fetchPosts = () => {
  webSocket.send(JSON.stringify({ action: 'fetch' }));
};

onMounted(() => {
  connectWebSocket();
});

onUnmounted(() => {
  if (webSocket) {
    webSocket.close();
  }
});
</script>

<template>
  <div>
    <h1>Posts</h1>
    <div v-if="isLoading">Loading...</div>
    <div v-else-if="!isConnected">
      There was an error connecting to the WebSocket server.
    </div>
    <table v-else>
      <thead>
        <tr>
          <th>Title</th>
          <th>Content</th>
          <th>Created At</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in posts" :key="post.id" class="text-xl text-black">
          <td>{{ post.title }}</td>
          <td>{{ post.content }}</td>
          <!-- <img :src="post.media" /> -->
          <td>{{ formatDate(post.created_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

