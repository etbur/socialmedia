<script setup>
import { Icon } from "@iconify/vue";
import { useRoute } from "vue-router";

const route = useRoute();
</script>

<template>
  <div class="flex md:flex-col space-y-4">
    <router-link
      to="/post"
      :class="getClass('/post')"
    >
      <Icon icon="mdi:post-outline" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">New Post</span>
    </router-link>

    <router-link
      to="/design"
      :class="getClass('/design')"
    >
      <Icon icon="mdi:design" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Design</span>
    </router-link>

    <router-link
      to="/game"
      :class="getClass('/game')"
    >
      <Icon icon="mdi:gamepad-variant" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Game</span>
    </router-link>

    <router-link
      to="/voicetotext"
      :class="getClass('/voicetotext')"
    >
      <Icon icon="mdi:voice" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Voice to Text</span>
    </router-link>

    <router-link
      to="/market"
      :class="getClass('/market')"
    >
      <Icon icon="mdi:chart-line" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Marketing</span>
    </router-link>

    <router-link
      to="/job"
      :class="getClass('/job')"
    >
      <Icon icon="mdi:briefcase" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Job</span>
    </router-link>

    <router-link
      to="/ad"
      :class="getClass('/ad')"
    >
      <Icon icon="mdi:announcement" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Ad</span>
    </router-link>

    <router-link
      to="/signlanguage"
      :class="getClass('/signlanguage')"
    >
      <Icon icon="mdi:language" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Sign Language</span>
    </router-link>

    <h1 class="font-semibold text-xl">Other</h1>

    <router-link
      to="/follower"
      :class="getClass('/follower')"
    >
      <Icon icon="mdi:account-multiple" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Follower</span>
    </router-link>

    <router-link
      to="/student"
      :class="getClass('/student')"
    >
      <Icon icon="mdi:school" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Student</span>
    </router-link>

    <button
      class="bg-[#F4F4F4] border-2 border-[#4267B2] border-opacity-10 text-blue-800 px-6 py-1 rounded-xl hover:bg-teal-600 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent hover:text-white"
    >
      <Icon icon="mdi:logout" class="inline-block mr-2" />
      Logout
    </button>
  </div>
</template>

<script>
import { computed } from 'vue';

const getClass = (path) => computed(() => ({
  'bg-[#E2E2E2] px-2 py-1 text-[#C59728] rounded-md': route.path === path,
  'px-2 rounded-md': true, // Default class for router-link
}));

export { getClass };
</script>

<style scoped>

</style>
