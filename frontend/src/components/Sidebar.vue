
 <script setup>
import { Icon } from "@iconify/vue";
import { useRoute } from "vue-router";

const route = useRoute();
</script>
 
 <template class="">
  <div class="flex md:flex-col space-y-4  pr-8 h-[500px] overflow-y-scroll">

    <router-link
      to="/post"
      active-class="bg-[#E2E2E2] text-[#C59728]"
      exact-active-class="bg-[#E2E2E2] pl-2 text-[#C59728] py-1"
    >
      <Icon icon="mdi:post-outline" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">New Post</span>
    </router-link>

    <router-link
      to="/design"
      active-class="bg-[#E2E2E2] pl-2 text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] pl-2 text-[#C59728]"
    >
      <Icon icon="mdi:design" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Design</span>
    </router-link>

    <router-link
      to="/game"
      active-class="bg-[#E2E2E2] pl-2 text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] pl-2 text-[#C59728]"
    >
      <Icon icon="mdi:gamepad-variant" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Game</span>
    </router-link>

    <router-link
      to="/voicetotext"
      active-class="bg-[#E2E2E2] pl-2 text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] pl-2 text-[#C59728]"
    >
      <Icon icon="mdi:voice" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Voice to Text</span>
    </router-link>

    <router-link
      to="/market"
      active-class="bg-[#E2E2E2] pl-2 text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] pl-2 text-[#C59728]"
    >
      <Icon icon="mdi:chart-line" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Marketing</span>
    </router-link>

    <router-link
      to="/job"
      active-class="bg-[#E2E2E2] pl-2 text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] pl-2text-[#C59728]"
    >
      <Icon icon="mdi:briefcase" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Job</span>
    </router-link>

    <router-link
      to="/ad"
      active-class="bg-[#E2E2E2]text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2]text-[#C59728]"
    >
      <Icon icon="mdi:announcement" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Ad</span>
    </router-link>

    <router-link
      to="/signlanguage"
      active-class="bg-[#E2E2E2]text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2]text-[#C59728]"
    >
      <Icon icon="mdi:language" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Sign Language</span>
    </router-link>

    <h1 class="font-semibold text-xl">Other</h1>

    <router-link
      to="/follower"
      active-class="bg-[#E2E2E2] text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] text-[#C59728]"
    >
      <Icon icon="mdi:account-multiple" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Follower</span>
    </router-link>

    <router-link
      to="/student"
      active-class="bg-[#E2E2E2] text-[#C59728]"
      exact-active-class="py-1  bg-[#E2E2E2] text-[#C59728]"
    >
      <Icon icon="mdi:school" class="inline-block mr-2" />
      <span class="text-blue-800 hover:text-[#C59728]">Student</span>
    </router-link>

    <button
      class="bg-[#F4F4F4] border-2 border-[#4267B2] border-opacity-10 text-blue-800 px-6 py-1 rounded-xl hover:bg-teal-600 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent hover:text-[#C59728]"
    >
      <Icon icon="mdi:logout" class="inline-block mr-2" />
      Logout
    </button>
  </div>
</template>