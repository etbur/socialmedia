<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const webSocket = ref(null);
const posts = ref([]);

const connectWebSocket = () => {
  webSocket.value = new WebSocket('ws://localhost:8000/ws/posts/');
  webSocket.value.onopen = onWebSocketOpen;
  webSocket.value.onmessage = onWebSocketMessage;
  webSocket.value.onerror = onWebSocketError;
  webSocket.value.onclose = onWebSocketClose;
};

const onWebSocketOpen = () => {
  console.log('WebSocket connection opened');
  fetchPosts();
};

const onWebSocketMessage = (event) => {
  console.log('WebSocket message received:', event.data);
  const data = JSON.parse(event.data);
  if (data.action === 'fetch_response') {
    console.log('Received posts:', data.posts);
    posts.value = data.posts;
  } else {
    console.error('Unexpected WebSocket message:', data);
  }
};

const onWebSocketError = (error) => {
  console.error('WebSocket error:', error);
};

const onWebSocketClose = () => {
  console.log('WebSocket connection closed');
};

const fetchPosts = () => {
  webSocket.value.send(JSON.stringify({ action: 'fetch' }));
};

onMounted(() => {
  connectWebSocket();
});

onUnmounted(() => {
  if (webSocket.value) {
    webSocket.value.close();
  }
});
</script>

<template>
  <div class="mx-10 md:mx-0 px-4 sm:px-8 md:px-12 lg:px-16 xl:px-20 mt-8 sm:mt-12 md:mt-16 lg:mt-20 xl:mt-24">
    <h1>Show all posts</h1>
    <div v-for="post in posts" :key="post.id" class="text-red-800">
      <h1>{{ post.title }}</h1>
      <h1>{{ post.description }}</h1>
      <!-- <img :src="post.media" alt="post img" /> -->
      <div v-for="tag in post.tags" :key="tag" class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">
        {{ tag }}
      </div>
    </div>
  </div>
</template>