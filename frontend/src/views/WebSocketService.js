// import { ref } from 'vue';

// const webSocket = ref(null);
// const isConnected = ref(false);
// const isLoading = ref(true);
// const error = ref(null);

// const connectWebSocket = () => {
//   webSocket.value = new WebSocket('ws://localhost:8000/ws/posts/');

//   webSocket.value.onopen = () => {
//     console.log('WebSocket connection established');
//     isConnected.value = true;
//     isLoading.value = false;
//     error.value = null;
//   };

//   webSocket.value.onmessage = (event) => {
//     try {
//       const data = JSON.parse(event.data);
//       console.log('Received data:', data);
//       // Handle the received data here
//     } catch (err) {
//       console.error('Error parsing WebSocket data:', err);
//       error.value = err;
//     }
//   };

//   webSocket.value.onclose = () => {
//     console.log('WebSocket connection closed');
//     isConnected.value = false;
//     isLoading.value = true;
//     error.value = null;
//     setTimeout(connectWebSocket, 5000);
//   };

//   webSocket.value.onerror = (event) => {
//     console.error('WebSocket error:', event);
//     isConnected.value = false;
//     isLoading.value = true;
//     error.value = event;
//   };
// };

// const sendWebSocketMessage = (message) => {
//   if (webSocket.value && webSocket.value.readyState === WebSocket.OPEN) {
//     webSocket.value.send(JSON.stringify(message));
//   }
// };

// export { connectWebSocket, sendWebSocketMessage, webSocket, isConnected, isLoading, error };
import { ref } from 'vue';

const webSocket = ref(null);
const isConnected = ref(false);
const isLoading = ref(true);
const error = ref(null);

const connectWebSocket = () => {
  webSocket.value = new WebSocket('ws://localhost:8000/ws/posts/');

  webSocket.value.onopen = () => {
    console.log('WebSocket connection established');
    isConnected.value = true;
    isLoading.value = false;
    error.value = null;
  };

  webSocket.value.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      console.log('Received data:', data);
      // Handle the received data here
    } catch (err) {
      console.error('Error parsing WebSocket data:', err);
      error.value = err;
    }
  };

  webSocket.value.onclose = () => {
    console.log('WebSocket connection closed');
    isConnected.value = false;
    isLoading.value = true;
    error.value = null;
    setTimeout(connectWebSocket, 5000);
  };

  webSocket.value.onerror = (event) => {
    console.error('WebSocket error:', event);
    isConnected.value = false;
    isLoading.value = true;
    error.value = event;
  };
};

const sendWebSocketMessage = (message) => {
  if (webSocket.value && webSocket.value.readyState === WebSocket.OPEN) {
    webSocket.value.send(JSON.stringify(message));
  }
};

export { connectWebSocket, sendWebSocketMessage, webSocket, isConnected, isLoading, error };